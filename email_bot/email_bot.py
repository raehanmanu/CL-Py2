import smtplib
from email.message import EmailMessage
import logging
import os

def read_emails(file_path):
    recievers = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            print(line)
            if line:
                name, email = line.split(",")
                recievers.append((name, email))
    print("recievers:", recievers)
    return recievers

def send_email(recipient_name, recipient_email):
    smtpServer = "smtp.gmail.com"
    smtpPort = 587
    senderEmail = "" #enter your email address here
    senderPassword = os.environ.get("EMAIL_PASSWORD") #set a environment variable EMAIL_PASSWORD with your email password


    print("password:", senderPassword)

    msg = EmailMessage()
    msg["Subject"] = "Test Email"
    msg["From"] = senderEmail
    msg["To"] = recipient_email
    msg.set_content("Hello this is a test email")

    try:
        with smtplib.SMTP(smtpServer, smtpPort) as server:
            server.starttls()
            server.login(senderEmail, senderPassword)
            server.send_message(msg)
        return True, "Email sent to {}".format(recipient_email)
    
    except Exception as a:
        return False, "Failed to send email to {}: {}".format(recipient_email, str(a))
    


def main():

    logging.basicConfig(filename="./email_log.txt", level=logging.INFO, 
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        force=True)
    # print("reached 1")
    recipients = read_emails("emails.txt")
    print("recipients:", recipients)
    # print("reached 2")

    for name, email in recipients:
        success, message = send_email(name, email)
        print("success:", success, "message:", message)
        if success:
            # print("reached 3")
            logging.info(message)
        else:
            # print("reached 4")

            logging.error(message)

    logging.shutdown()


if __name__ == "__main__":
    main()