from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_login_email(user):

    account_url = f"http://127.0.0.1:8000/done/?name={user.username}/"

    html_content = render_to_string(
        "emails/login_success.html",
        {
            "user": user,
            "account_url": account_url,
        }
    )

    email = EmailMultiAlternatives(
        subject="Login Successful",
        body="Sizning akkauntingizga muvaffaqiyatli kirildi.",
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email,settings.EMAIL_HOST_USER],
    )

    email.attach_alternative(html_content, "text/html")

    email.send()