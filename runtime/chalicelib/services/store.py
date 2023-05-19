import time

from datetime import datetime, timedelta, time

from ..models.store import StoreStatus, StoreTimeZone, StoreBusinessHours
from .date_and_time import in_between, convert_to_local_time


def shift_to_current_time_stamp(polls):
    """
    shift the static poll data based on current time stamp
    """
    # shifting the data to present timestamp
    max_time_stamp = None
    for poll in polls.all():
        if not max_time_stamp or poll.timestamp > max_time_stamp: max_time_stamp = poll.timestamp

    current_timestamp = datetime.now()

    # shift all the timestamps
    for poll in polls.all():
        poll.timestamp = poll.timestamp + (current_timestamp - max_time_stamp)


def get_schedule_on_day(schedules):
    """returns a list of business hours on all days of the week"""
    schedule_on_day = dict()
    for schedule in schedules:
        schedule_on_day[schedule.dayOfWeek] = schedule
    # if we don't have a schedule for a particular day then make it 24 hours
    for i in range(7):
        if i not in schedule_on_day.keys():
            schedule_on_day[i] = StoreBusinessHours()
            schedule_on_day[i].start_time_local = time(0, 0, 0)
            schedule_on_day[i].end_time_local = time(23, 59, 59)

    return schedule_on_day


def get_needed_polls_last_n_days(n, schedules):
    """
    returns number of business hours of the store in last n days
    i.e the number of needed polls
    """
    schedule_on_day = get_schedule_on_day(schedules)
    needed_polls = 0
    current_timestamp = datetime.now()
    moving_timestamp = current_timestamp

    while (current_timestamp - moving_timestamp).days < n:
        weekday = moving_timestamp.weekday()
        hours = schedule_on_day[weekday].end_time_local.hour - schedule_on_day[weekday].start_time_local.hour
        needed_polls += (hours + 24) % 24
        moving_timestamp -= timedelta(days=1)

    return needed_polls


def get_last_n_days_analysis(id, n):
    """
    Given store id returns the number of uptime and downtime
    hours within the service hours of the store in previous n days.
    """
    schedules = StoreBusinessHours.where(store_id=id)

    try:
        time_zone = StoreTimeZone.find_or_fail(id).time_zone
    except Exception as e:
        time_zone = "America/Chicago"

    polls = StoreStatus.where(store_id=id)

    # schedule_on_day on particular day of the week
    schedule_on_day = get_schedule_on_day(schedules)

    total_polls = 0     # total actual polls done by our platform
    active_polls = 0    # times when store was active
    needed_polls = get_needed_polls_last_n_days(n, schedules)     # total polls which could have been done

    current_timestamp = datetime.now()

    shift_to_current_time_stamp(polls)

    for poll in polls.all():
        if (current_timestamp - poll.timestamp).days < n:
            weekday = poll.timestamp.weekday()
            local_time = convert_to_local_time(poll.timestamp, time_zone)

            if in_between(local_time, schedule_on_day[weekday].start_time_local, schedule_on_day[weekday].end_time_local):
                total_polls += 1
                active_polls += poll.status == 'active'

    return active_polls, total_polls, needed_polls


def generate_report_last_n_days(id, n):
    active_polls, total_polls, needed_polls = get_last_n_days_analysis(id, n)
    if total_polls:
        uptime_hours = needed_polls * (active_polls / total_polls)
        return {
            "uptime": uptime_hours,
            "downtime": needed_polls - uptime_hours
        }
    return {
        "uptime": "No data",
        "downtime": "No data"
    }


def generate_report_last_hour(id):
    """
    Check for the polls
    """
    schedules = StoreBusinessHours.where(store_id=id)

    try:
        time_zone = StoreTimeZone.find_or_fail(id).time_zone
    except Exception as e:
        time_zone = "America/Chicago"

    polls = StoreStatus.where(store_id=id)

    # schedule_on_day on particular day of the week
    schedule_on_day = get_schedule_on_day(schedules)

    total_polls = 0     # total actual polls done by our platform
    active_polls = 0    # times when store was active

    current_timestamp = datetime.now()

    shift_to_current_time_stamp(polls)

    for poll in polls.all():
        if current_timestamp.hour == poll.timestamp.hour and current_timestamp.weekday() == poll.timestamp.weekday():
            weekday = poll.timestamp.weekday()
            local_time = convert_to_local_time(poll.timestamp, time_zone)

            if in_between(local_time, schedule_on_day[weekday].start_time_local, schedule_on_day[weekday].end_time_local):
                total_polls += 1
                active_polls += poll.status == 'active'

    if not total_polls:
        return {
            "uptime": "No data",
            "downtime": "No data"
        }
    return {
        "uptime": 60 * active_polls / total_polls,
        "downtime": 60 * (total_polls - active_polls) / total_polls
    }
