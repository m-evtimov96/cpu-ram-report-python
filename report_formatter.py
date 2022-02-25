import io
from matplotlib import pyplot


def format_cpu_and_ram_usage_as_graph(cpu_report, ram_report):
    cpu_usage = [x[1] for x in cpu_report]
    cpu_time = [x[0] for x in cpu_report]
    ram_usage = [x[1] for x in ram_report]
    ram_time = [x[0] for x in ram_report]
    pyplot.plot(cpu_time, cpu_usage, label='CPU %')
    pyplot.plot(ram_time, ram_usage, label='RAM %')
    pyplot.xlabel('Time')
    pyplot.ylabel('Load in %')
    pyplot.title('Cpu and Ram usage for 10 seconds')
    pyplot.legend()

    image_format = 'png'
    report_as_png = io.BytesIO()
    pyplot.savefig(report_as_png, format=image_format)
    report_as_png.seek(0)

    return report_as_png
