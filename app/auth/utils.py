from flask_mail import Message
from flask import current_app
from random import randint
import datetime

otp_storage = {}  # Simple in-memory dict for demo

def generate_and_store_otp(email):
    otp = str(randint(100000, 999999))
    expires = datetime.datetime.now() + datetime.timedelta(minutes=5)
    otp_storage[email] = {
        'otp': otp,
        'expires': expires
    }

    # msg = Message("Your OTP Code", recipients=[email])
    # msg.body = f"Your OTP code is: {otp}"
    # mail.send(msg)

    otp_storage[email] = {
        'otp': otp,
        'expires': expires
    }

    return otp
