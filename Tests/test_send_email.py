from mail_conf import send_email

def test_send_email_report():
        print("sending email")
        send_email()
        print("email sent")