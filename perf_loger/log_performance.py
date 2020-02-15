import datetime
import logging
import time
from functools import wraps

# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('performance-{}.log'.format(time.strftime("%Y%m%d-%H%M%S")))
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('LoggerName,ProcessId,ThreadId,MethodName,StartTime,EndTime,ElapsedTimeInMS')
formatter = logging.Formatter('%(name)s,%(process)d,%(thread)d,%(message)s')
file_handler.setFormatter(formatter)


# Add @log_performance annotation to any function that you would like to measure it's performance
# here is how to use it:
# @log_performance
# def sleep_2_seconds():
#    time.sleep(2)
#     return
def log_performance(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        date_time_start = datetime.datetime.now()
        # execute the original function
        result = func(*args, **kwargs)
        # compute and log the elapsed time in ms
        date_time_end = datetime.datetime.now()
        duration = (date_time_end - date_time_start).total_seconds() * 1000
        logger.info('{0},{1},{2},{3}'.format(func.__qualname__, date_time_start, date_time_end, duration))
        return result

    return function_wrapper
