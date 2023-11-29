from django.utils import timezone
from . import models


def get_notification(request):
    today = timezone.now().date()
    count = models.Penality.objects.filter(name=request.user, date__date = today).count()
    
    context = {
        "count" : count,
    }

    return context