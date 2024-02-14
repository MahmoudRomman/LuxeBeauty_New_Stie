from accounts import models as accounts_models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


content_type = ContentType.objects.get_for_model(accounts_models.Profile)

def create_custom_permission():
    can_make_order_permission = Permission.objects.get_or_create(
        codename='can_make_order',
        name='Can Make Order',
        content_type=content_type,
    )

    permission = Permission.objects.get(codename='can_make_order')


    return permission