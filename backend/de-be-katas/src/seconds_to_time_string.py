

def seconds_to_time_string(seconds):
    time_string = ""
    if seconds < 60:
        return get_seconds(seconds)
    if seconds < 3600:
        minutes = seconds // 60
        seconds = seconds % 60
        time_string = get_minutes(minutes) + ' ' +get_seconds(seconds)
        return time_string.strip()
    if seconds < 86400:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        time_string = get_hours(hours) + ' ' + get_minutes(minutes) + ' ' + get_seconds(seconds)
        return time_string.strip()
    if seconds < 31536000:
        days = seconds // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        time_string = get_days(days) + ' ' + get_hours(hours) + ' ' + get_minutes(minutes) + ' ' + get_seconds(seconds)
        return time_string.strip()

def get_seconds(seconds):
    if seconds == 0:
        return ""
    if seconds == 1:
        return f"{seconds} second"
    return f"{seconds} seconds"

def get_minutes(minutes):
    if minutes == 0:
        return ""
    if minutes == 1:
        return f"{minutes} minute"
    return f"{minutes} minutes"

def get_hours(hours):
    if hours == 0:
        return ""
    if hours == 1:
        return f"{hours} hour"
    return f"{hours} hours"

def get_days(days):
    if days == 0:
        return ""
    if days == 1:
        return f"{days} day"
    return f"{days} days"