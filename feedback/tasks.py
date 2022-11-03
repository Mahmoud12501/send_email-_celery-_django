from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_email_feedback(email,message):
     sleep(20)  # Simulate expensive operation that freezes Django
     send_mail(
            "Your Feedback",
            f"\t{message}\n\nThank you!",
            "support@example.com",
            [email],
            fail_silently=False,
        )