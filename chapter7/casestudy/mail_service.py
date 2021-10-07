import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, headers=None):
    headers = {} if headers is None else headers
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['TO']
        email['TO'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()

send_email("A model subject", "The message contents", 'from@example.com', 'to1@example.com', 'to2@example.com')