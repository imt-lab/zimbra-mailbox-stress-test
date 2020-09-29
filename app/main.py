import threading
import smtplib
from config import LMTP_SERVER, LMTP_PORT, TO_EMAILS, THREADS


def send_message():
    for i in range(1, 1000):
        server = smtplib.LMTP(LMTP_SERVER, port=LMTP_PORT)
        # Prepare actual message
        from_email = "stresstest@example.com"

        subject = "Hello!"

        body = "This message was sent with LmtpStressTest"
        message = """\
        From: %s
        To: %s
        Subject: %s
        
        %s
        """ % (from_email, ", ".join(TO_EMAILS), subject, body)

        # print(message)

        server.sendmail(from_email, TO_EMAILS, message)
        server.quit()


if __name__ == '__main__':
    try:
        for i in range(1, THREADS):
            t = threading.Thread(target=send_message)
            t.start()
    except Exception as e:
        print(e)
