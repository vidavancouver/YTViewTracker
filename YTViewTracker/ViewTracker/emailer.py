import smtplib




sender = "noreply.ytviewtracker@gmail.com"


def main(toEmail, title):
    receivers = toEmail

    message = f"""Your tracking of {title} has finished!
    Thank you for using our service."""
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)         
        print("Successfully sent email")
    except Exception:
        print("Error: unable to send email")