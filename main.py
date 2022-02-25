from report_formatter import format_cpu_and_ram_usage_as_graph
from report_generator import construct_report_for_10_seconds
from PIL import Image

cpu_report, ram_report = construct_report_for_10_seconds()
formatted_report = format_cpu_and_ram_usage_as_graph(cpu_report, ram_report)
img = Image.open(formatted_report)
# Saving the image to the project folder
img.save('test_report', format='png')
