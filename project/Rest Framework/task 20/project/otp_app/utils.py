from twilio.rest import Client
import random

def send_otp(mobile):
    account_sid = 'AC9777034e2131f7bd4ffc391f952a43b4'
    auth_token = '98948e3d2fcb77fc5d337f87c2a922b6'
    twilio_phone = '+18302290253'

    otp = str(random.randint(100000, 999999))
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Your OTP is {otp}',
        from_=twilio_phone,
        to=mobile
    )
    return otp
