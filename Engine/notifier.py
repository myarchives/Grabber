import config
import smtplib


def SendMail(token, list):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(config.EMAIL, config.PASSWORD)
            if token == 1:
                subject = 'Grabber: Spreadsheet Updated'
                body = f'Successfully grabbed all items!\nYour total is $ {list[0]}'
                msg = Message(subject, body)
            elif token == 2:
                subject = 'Grabber: Price Dropped!!'
                body = f'The price of "{list[0]}" has dropped from {list[1]} to {list[2]}'
                msg = Message(subject, body)
            elif token == 3:
                subject = 'Grabber: Product Purchased'
                body = f'The requested product has dropped to sale from {list[0]} to {list[1]} and was purchased.'
                msg = Message(subject, body)
            smtp.sendmail(config.EMAIL, config.TO, msg)
        print('Email sent scuccessfully')
    except:
        print('Email failed to send!')


def Message(subj, body):
    return (f'Subject: {subj}\n\n{body}')
