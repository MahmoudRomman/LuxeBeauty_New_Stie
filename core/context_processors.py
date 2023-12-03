from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from . import models


def penality_notification(request):
    today = timezone.now().date()
    penality_count = models.Penality.objects.filter(name=request.user, date__month=today.month).count()

    # penality_count = 0
    
    context = {
        "penality_count" : penality_count,
    }

    return context



def reward_notification(request):
    today = timezone.now().date()
    reward_count = models.Reward.objects.filter(name=request.user, date__month=today.month).count()

    
    context = {
        "reward_count" : reward_count,
    }

    return context

def mybills_notification(request):
    today = timezone.now().date()
    my_bills = models.Bill2.objects.filter(seller=request.user, date__month=today.month)
    
    mybills_count = 0
    for bill in my_bills:
        mybills_count += bill.pieces_num

    
    context = {
        "mybills_count" : mybills_count,
    }

    return context




def cart_notification(request):
    start_time = timezone.now() - timedelta(minutes=30)

    try:
        queryset = models.Order.objects.get(user=request.user, ordered=False, start_date__gte=start_time)
        total_items = 0
        for order_item in queryset.items.all():
            total_items += order_item.quantity
        
        cart_count = total_items

    except ObjectDoesNotExist:
        cart_count = 0


    context = {
        "cart_count" : cart_count,
    }

    return context