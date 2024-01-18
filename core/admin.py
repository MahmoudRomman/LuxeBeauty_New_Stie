from django.contrib import admin
from . import models
# Register your models here.


class BillModelAdmin(admin.ModelAdmin):
    list_display = ('seller', 'country', 'customer_name', 'customer_phone')  # Fields to display in the list view
    # list_filter = ('customer_name', 'customer_phone')  # Fields for filtering
    search_fields = ('customer_name', 'customer_phone', 'slug_code')  # Fields for searching


class RefundModelAdmin(admin.ModelAdmin):
    list_display = ('seller', 'country', 'customer_name', 'customer_phone', 'pieces_num')  # Fields to display in the list view
    # list_filter = ('customer_name', 'customer_phone')  # Fields for filtering
    search_fields = ('customer_name', 'customer_phone')  # Fields for searching

# admin.site.register(YourModel, YourModelAdmin)

admin.site.register(models.Item)
admin.site.register(models.OrderItem)
admin.site.register(models.Order)
# admin.site.register(models.Bill)
# admin.site.register(models.Billl)
admin.site.register(models.Bill2, BillModelAdmin)

# Added new...
admin.site.register(models.Refund, RefundModelAdmin)

admin.site.register(models.Coupon)
admin.site.register(models.Offer)


# admin.site.register(models.PhoneNumber)
admin.site.register(models.Phones)

admin.site.register(models.Account)



admin.site.register(models.AddLink)
admin.site.register(models.BankAccount)



# New registerd model to add penalites to the users
admin.site.register(models.Penality)
admin.site.register(models.Reward)
admin.site.register(models.Tasks)


admin.site.register(models.PhoneNumberr)

