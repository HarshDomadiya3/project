# insurance/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(email):
    try:
        send_mail(
            'Confirmation Email',
            'Your registration was successful. Welcome to our Insurance System.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error sending email: {e}")
