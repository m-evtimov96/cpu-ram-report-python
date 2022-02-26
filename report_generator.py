from datetime import datetime, timedelta
from time import sleep
import psutil


def generate_used_cpu_percentage():
    cpu_load_percentage = psutil.cpu_percent(0.1, False)
    return cpu_load_percentage


def generate_used_ram_percentage():
    ram_load_percentage = psutil.virtual_memory().percent
    return ram_load_percentage


def construct_report_for_10_seconds():
    cpu_report = []
    ram_report = []
    report_limit = 10
    end_time = datetime.now() + timedelta(seconds=report_limit + 1)
    print(f'Please wait {report_limit} seconds for the report to generate.')
    while datetime.now() < end_time:
        cpu_report.append((datetime.now(), generate_used_cpu_percentage()))
        ram_report.append((datetime.now(), generate_used_ram_percentage()))
        sleep(0.1)

    return cpu_report, ram_report
