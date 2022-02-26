import smtplib
import ssl
from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def send_report_via_email(report, sender_email, receiver_email):

    mail = MIMEMultipart()
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(report.read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % 'graph.png')
    mail['Subject'] = 'Cpu and Ram report'
    mail.attach(part)

    port = 465
    smtp_server = 'smtp.gmail.com'
    sender_password = input('Please enter sender email password:')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, mail.as_string())
            print('Report was sent to the provided email.')
        except Exception as exc:
            print('An error occurred.')
