import time

from performance.log_performance import log_performance


@log_performance
def sleep_2_seconds():
    time.sleep(2)
    return


if __name__ == '__main__':
    sleep_2_seconds()
    time.sleep(1)
    sleep_2_seconds()
