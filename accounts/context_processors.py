from . import models



def check_user_job_type(request):
    if request.user.is_authenticated:
        current_user = models.Profile.objects.get(staff=request.user)
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