import pytz


def in_between(now, start, end):
    """
    Return if current timestamp is between start and end timestamp
    """
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end


def convert_to_local_time(timestamp, time_zone):
    """
    Given timezone and utc time, convert to local timestamp
    """
    local_timezone = pytz.timezone(time_zone)
    local_time = timestamp.astimezone(local_timezone).time()
    return local_time