import logging
from datetime import datetime
import time, pytz

from chalice import Blueprint, BadRequestError, UnauthorizedError

from ..constants import *
from ..models.store import StoreStatus, StoreBusinessHours, StoreTimeZone

store_routes = Blueprint('store')
logger = logging.getLogger(__name__)


@store_routes.route('/dummy', methods=['GET'], cors=True)
def dummy():
    # read the csv and do the entries in the database
    print("This is working.")
    return {"status": "working"}


def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end




@store_routes.route('/{id}/report', methods=['POST'], cors=True)
def generate_report(id):
    """Given a store id generate a report of the store for last week."""
    """
    Fetch all the polls of this store done in last week.
    """

    # find the start and end time in local time format
    schedules = StoreBusinessHours.where(store_id=id)
    interval = dict()

    total_polls = 0
    active_polls = 0
    ideal_polls = 0

    for schedule in schedules:
        interval[schedule.dayOfWeek] = schedule
        hours = interval[schedule.dayOfWeek].start_time_local.hour - interval[schedule.dayOfWeek].end_time_local.hour
        ideal_polls += (hours + 24) % 24

    time_zone = StoreTimeZone.find_or_fail(id).time_zone

    polls = StoreStatus.where(store_id=id)
    # take the poll with current timestamp as max timestamp



    max_time_stamp = None
    for poll in polls.all():
        if not max_time_stamp or poll.timestamp > max_time_stamp: max_time_stamp = poll.timestamp

    current_timestamp = datetime.now()

    # shift all the timestamps
    for poll in polls.all():
        poll.timestamp = poll.timestamp + (current_timestamp - max_time_stamp)

    for poll in polls.all():
        # find if timestamp belongs to previous week
        if (current_timestamp - poll.timestamp).days < 7:
            weekday = poll.timestamp.weekday()

            local_timezone = pytz.timezone(time_zone)
            local_time = poll.timestamp.astimezone(local_timezone).time()

            if in_between(local_time, interval[weekday].start_time_local, interval[weekday].end_time_local):
                total_polls += 1
                active_polls += poll.status == 'active'

    print(total_polls, active_polls, ideal_polls)





















