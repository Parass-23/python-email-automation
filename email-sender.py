import smtplib
from email.message import EmailMessage
from getpass import getpass

sender_email = input("Enter your email: ")
receiver_email = input("Enter receiver email: ")
subject = input("Enter subject: ")
message = input("Enter message: ")

email = EmailMessage()
email["From"] = sender_email
email["To"] = receiver_email
email["Subject"] = subject
email.set_content(message)

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()

        password = getpass("Enter your email app password: ")
        server.login(sender_email, password)

        server.send_message(email)

    print("Email sent successfully!")

except Exception as e:
    print("Something went wrong:", e)