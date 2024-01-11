from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from . import models
from accounts import models as accounts_models


def penality_notification(request):

    if request.user.is_authenticated:
        today = timezone.now().date()
        penality_count = models.Penality.objects.filter(name=request.user, date__month=today.month).count()
    else:
        penality_count = 0

    context = {
        "penality_count" : penality_count,
    }

    return context



def reward_notification(request):
    if request.user.is_authenticated:
        today = timezone.now().date()
        reward_count = models.Reward.objects.filter(name=request.user, date__month=today.month).count()
    else:
        reward_count = 0    

    context = {
        "reward_count" : reward_count,
    }

    return context

def mybills_notification(request):
    if request.user.is_authenticated:
        today = timezone.now().date()
        my_bills = models.Bill2.objects.filter(seller=request.user, date__month=today.month)
    
        mybills_count = 0
        for bill in my_bills:
            mybills_count += bill.pieces_num
    else:
        mybills_count = 0
    
    context = {
        "mybills_count" : mybills_count,
    }

    return context




def cart_notification(request):
    if request.user.is_authenticated:
        start_time = timezone.now() - timedelta(minutes=30)

        try:
            queryset = models.Order.objects.get(user=request.user, ordered=False, start_date__gte=start_time)
            total_items = 0
            for order_item in queryset.items.all():
                total_items += order_item.quantity
            
            cart_count = total_items

        except ObjectDoesNotExist:
            cart_count = 0
    else:
        cart_count = 0

    context = {
        "cart_count" : cart_count,
    }

    return context







def ordered_task_notification(request):
    if request.user.is_authenticated:
        ordered_task_count = models.Tasks.objects.filter(status=False).count()
    else:
        ordered_task_count = 0    

    context = {
        "ordered_task_count" : ordered_task_count,
    }

    return context



def done_task_notification(request):
    if request.user.is_authenticated:
        done_task_count = models.Tasks.objects.filter(status=True,  done_task_is_read=False).count()
    else:
        done_task_count = 0    

    context = {
        "done_task_count" : done_task_count,
    }

    return context



def user_ordered_task_notification(request):
    if request.user.is_authenticated:
        user_ordered_task_count = models.Tasks.objects.filter(name=request.user, status=False).count()
    else:
        user_ordered_task_count = 0    

    context = {
        "user_ordered_task_count" : user_ordered_task_count,
    }

    return context




def check_user_job_type(request):
    if request.user.is_authenticated:
        current_user = accounts_models.Profile.objects.get(staff=request.user)
        if current_user.job_type == "Seller":
            is_seller = True
        else:
            is_seller = False
    else:
        is_seller = True

    context = {
        'is_seller' : is_seller,
    }
    return context