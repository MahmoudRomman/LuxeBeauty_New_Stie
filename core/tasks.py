from celery import shared_task
from project import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.forms.models import model_to_dict


# @shared_task(bind=True)
@shared_task
def send_bill_mail(merge_data, email):
    html_body = render_to_string("core/bill_mail.html", merge_data)
    subject = "Bill From LuxeBeauty Site"
    
    
    email = model_to_dict(email)
    msg = EmailMultiAlternatives(
        subject = subject,
        from_email= settings.EMAIL_HOST_USER,
        to=(email,),
        reply_to=(settings.EMAIL_HOST_USER,),
        )
    
    msg.attach_alternative(html_body, "text/html")
    msg.send()

    print("you are here................")
    return "Task Successfulllllllllly"

    




@shared_task(bind=True)
def print_func(self):
    print("in the prnit func------------------")
    return "Task Successfull in the print_func"



