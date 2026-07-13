from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import random
# Create your tests here.

def create_code():
    code = random.randint(100000, 999999)
    return str(code)

def send_login_email(user,code):

    account_url = f"http://127.0.0.1:8888/auth/done/?name={user.username}"

    html_content = render_to_string(
        "emails/login_success.html",
        {
            "user": user,
            "account_url": account_url,
            'code':code
        }
    )

    email = EmailMultiAlternatives(
        subject="Login Successful",
        body="shu kodni oling ",
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email,settings.EMAIL_HOST_USER],
    )

    email.attach_alternative(html_content, "text/html")

    email.send()


