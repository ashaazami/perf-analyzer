import datetime
import logging
import os
import time
from functools import wraps

# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
__log_file_name__ = 'performance-{}.log'.format(time.strftime("%Y%m%d-%H%M%S"))
file_handler = logging.FileHandler(__log_file_name__)
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('LoggerName,ProcessId,ThreadId,MethodName,StartTime,EndTime,ElapsedTimeInMS')
formatter = logging.Formatter('%(name)s,%(process)d,%(thread)d,%(message)s')
file_handler.setFormatter(formatter)


def log_performance(func):
    """
    Add @log_performance annotation to any function that you would like to measure it's performance
    here is how to use it:
    @log_performance
    def sleep_2_seconds():
       time.sleep(2)
        return
    """

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


def get_log_filename():
    return os.path.abspath(__log_file_name__)
