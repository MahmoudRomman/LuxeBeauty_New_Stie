from accounts import models as accounts_models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


content_type = ContentType.objects.get_for_model(accounts_models.Profile)
# existing_permissions = Permission.objects.filter(content_type=content_type, codename='can_make_order')

# if not existing_permissions.exists():
#     can_make_order_permission = Permission.objects.create(
#         codename='can_make_order',
#         name='Can Make Order',
#         content_type=content_type,
#     )


# can_make_order_permission = Permission.objects.get_or_create(
#     codename='can_make_order',
#     name='Can Make Order',
#     content_type=content_type,
# )


def create_custom_permission():
    can_make_order_permission = Permission.objects.get_or_create(
        codename='can_make_order',
        name='Can Make Order',
        content_type=content_type,
    )

    permission = Permission.objects.get(codename='can_make_order')


    return permission