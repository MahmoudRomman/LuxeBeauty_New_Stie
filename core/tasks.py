from celery import shared_task
from project import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task(bind=True)
def send_bill_mail(self, merge_data, email):
    html_body = render_to_string("core/bill_mail.html", merge_data)
    subject = "Bill From LuxeBeauty Site"
    
    
    msg = EmailMultiAlternatives(
        subject = subject,
        from_email= settings.EMAIL_HOST_USER,
        # to=(settings.EMAIL_HOST_USER,),
        to=(email,),

        reply_to=(settings.EMAIL_HOST_USER,),
        )
    
    msg.attach_alternative(html_body, "text/html")
    msg.send()

    return "Task Successfull"

    


