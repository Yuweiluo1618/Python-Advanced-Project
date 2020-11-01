#!/bin/python3
# import the module
import psutil
import datetime


def linux_monitor(time):
    """
    :param time: the time inteval in second to active monitor
    """
    # CPU usage info
    cpu_per = psutil.cpu_percent(interval=time)

    # Memory info
    memory_info = psutil.virtual_memory()

    # hard disk info
    hard_disk_info = psutil.disk_usage('/')

    # Network info
    net_info = psutil.net_io_counters()

    # obtain system time
    current_time = datetime.datetime.now().strftime("%F %T")

    # print info
    log_str = f'\t\tTime \t\t\t\t CPU info (core:{psutil.cpu_count(logical=False)}) \t\t\t\t Memory info (total:{memory_info.total / 1024 / 1024 / 1024}G) \t\t\t\t Hard disk info (total: {hard_disk_info.total / 1024 / 1024 / 1024}G) \t\t\t\t Networl info \n'
    log_str += f'{current_time} \t\t\t\t{cpu_per}% \t\t\t\t\t\t\t\t {memory_info.percent}% \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t {hard_disk_info.percent}% t\t\t\t\t\t Rec: {net_info.bytes_recv} / Send: {net_info.bytes_sent}'
    print(log_str)

    # save info to file
    f = open('log.txt', 'a')
    f.write(log_str)
    f.close()


def main():
    """program entrance"""
    while True:
        linux_monitor(10)


if __name__ == "__main__":
    main()
