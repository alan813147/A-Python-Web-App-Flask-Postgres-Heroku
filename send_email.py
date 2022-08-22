import smtplib
from email.mime.text import MIMEText

def send_mail(customer, waiter, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '456c9115c05635'
    password = '0b9ece90b91d54'
    message = f'<h3>New Feedback Submisson</h3><ul><li>Customer: {customer}</li>\
        <li>Waiter: {waiter}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>'
    
    sender_email = "email1@example.com"
    receiver_email = "email2example.com"
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Alan Pvt Kitchen Feedback'
    msg['From'] = sender_email
    msg['TO'] = receiver_email

    #send email
    with smtplib.SMTP(smtp_server,port) as server :
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())