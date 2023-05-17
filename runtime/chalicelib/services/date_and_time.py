import pytz

def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end

def convert_to_local_time(timestamp, time_zone):
    local_timezone = pytz.timezone(time_zone)
    local_time = timestamp.astimezone(local_timezone).time()
    return local_time