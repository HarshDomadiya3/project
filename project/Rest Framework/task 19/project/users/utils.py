import sendgrid
from sendgrid.helpers.mail import Mail
from django.conf import settings

def send_confirmation_email(to_email, username):
    sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
    subject = "Welcome to Our Platform!"
    content = f"Hi {username},\n\nThank you for registering. We're excited to have you on board!"
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        plain_text_content=content,
    )
    response = sg.send(message)
    return response.status_code
