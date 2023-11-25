from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Item)
admin.site.register(models.OrderItem)
admin.site.register(models.Order)
# admin.site.register(models.Bill)
# admin.site.register(models.Billl)
admin.site.register(models.Bill2)


admin.site.register(models.Coupon)
admin.site.register(models.Offer)


admin.site.register(models.PhoneNumber)
admin.site.register(models.Phones)

admin.site.register(models.Account)



admin.site.register(models.AddLink)


# New registerd model to add penalites to the users
admin.site.register(models.Penality)




