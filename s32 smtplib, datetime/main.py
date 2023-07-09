# import smtplib

# my_email = 'jaguattt@gmail.com'
# pw = 'secret!'
# pw_app = 'secret!'

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=pw_app)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs='pedrovictorbr@gmail.com', 
#         msg='Subject:michui\n\nmandando um e-mail pro antilope atraves de uma aplicacao em python')

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() #monday is 0, tuesday is 1, etc.
print(day_of_week)

date_of_birth = dt.datetime(year=1983, month=3, day=2)
print(date_of_birth)

with open('quotes.txt') as quotes:
    quotes_list = quotes.readlines()
    print(quotes_list)