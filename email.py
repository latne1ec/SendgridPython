import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='api_key')
from_email = Email("evan@teamlevellabs.com")
subject = "Hello World from the SendGrid Python Library!"
to_email = Email("evan.latner@gmail.com")
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

