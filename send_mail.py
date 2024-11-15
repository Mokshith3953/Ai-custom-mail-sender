import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def mail(email,mess):
   
    # Use your email and the app password if you have 2-Step Verification enabled
    sender_email = "mokshi3953@gmail.com"
    sender_password = "pzcj pzax jvom utlg"  # Use the app password if 2-Step Verification is enabled
    receiver_email = email
    subject = "Sending a mail to user"
    message = (
        mess
    )
    html_message = message

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    print("email is on the way")
    # Attach the message
    msg.attach(MIMEText(message, 'plain'))
    msg.attach(MIMEText(html_message, 'html'))
    try:
        # Connect to the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to your account
        server.login(sender_email, sender_password)
        # Send the email
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
       return -1

#mail("sumanthreddych2004@gmail.com",93454)



