import time

from performance.log_performance import log_performance, get_log_filename
from performance.log_visualizer import visualize_performance


@log_performance
def sleep_2_seconds():
    time.sleep(2)
    return


if __name__ == '__main__':
    sleep_2_seconds()
    sleep_2_seconds()
    file = get_log_filename()
    visualize_performance(file)
