from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse


@shared_task(bind=True)
def fun(self):
    # operations
    print("You are in Fun function")
    return "done"



from celery import shared_task
from django.core.mail import send_mail
	
@shared_task(bind=True)
def send_mail_func(self):
    mail_subject="hello celery"
    message="subscribe TheCodeSpace Youtube channel."
    to_email = "mahmoud.sayyedahmed900@gmail.com"
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
        )
    return "Task Successfull"


