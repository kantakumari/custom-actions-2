import smtplib, ssl
import os
import sys


port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
githubjob= sys.argv[1]
githubrepo = sys.argv[2]
githubwork = sys.argv[3]
subject = '{p1} job of {p2} had failed'
subject2 = subject.format(p1=githubjob, p2=githubrepo)
body1 = '{c1} job in worflow {c3} of {c2} had Failed'
body2 = body1.format(c1=githubjob, c3=githubwork, c2=githubrepo)
message = f"""\
Subject: {subject2}

{body2}
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME,'kanta.kumari@publicissapient.com',message)
