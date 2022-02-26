from report_formatter import format_cpu_and_ram_usage_as_graph
from report_generator import construct_report_for_10_seconds
# from PIL import Image

# generating cpu and ram reports as lists
from report_sender import send_report_via_email

cpu_report, ram_report = construct_report_for_10_seconds()

# formatting both reports as graph in .png format
formatted_report = format_cpu_and_ram_usage_as_graph(cpu_report, ram_report)

# sending the report via email
send_report_via_email(formatted_report, 'Fr33Bot96@gmail.com', 'm.evtimov196@gmail.com')


# Saving the image to the project folder
# img = Image.open(formatted_report)
# img.save('test_report.png', format='PNG')
