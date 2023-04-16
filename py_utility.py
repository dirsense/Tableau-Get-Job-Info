import datetime

def get_diff_time_str(start_time, end_time=None) -> str:
    if start_time is None:
        return '-'
    if end_time is None:
        end_time = datetime.datetime.now()

    diff = end_time - start_time

    s = int(diff.seconds)
    if s >= 60:
        minute, second = divmod(s, 60)
        time_str = '{0:0=1g} m {1:0=1g} s'.format(minute, second)
    else:
        time_str = str(s) + ' sec'
    
    return time_str