from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime    
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone
from django_countries.fields import CountryField


# from accounts.models import User






# Create your models here.


wig_name = (
    ('باروكة شعر طبيعى', 'باروكة شعر طبيعى'),
    ('مقدمة باروكة شعر طبيعى', 'مقدمة باروكة شعر طبيعى'),

)

wig_type = (
    ("اختر نوع الباروكة", "اختر نوع الباروكة"),
    ('جذور امامية', 'جذور امامية'),
    ('جذور كامله', 'جذور كامله'),
    ('جذور دائرية 360', 'جذور دائرية 360'),
    ('لا شىء', 'لا شىء'),
)


wig_long = (
    ("طول الباروكة", "طول الباروكة"),
    ('انش10', 'انش10'),
    ('انش12', 'انش12'),
    ('انش14', 'انش14'),
    ('انش16', 'انش16'),
    ('انش18', 'انش18'),
    ('انش20', 'انش20'),
    ('انش22', 'انش22'),
    ('انش24', 'انش24'),
    ('انش26', 'انش26'),
    ('انش28', 'انش28'),
    ('انش30', 'انش30'),
    ('انش32', 'انش32'),
    ('انش34', 'انش34'),
    ('انش36', 'انش36'),
    ('انش38', 'انش38'),
    ('انش40', 'انش40'),
)


scalp_type = (
    ("اختر نوع الفروة", "اختر نوع الفروة"),
    ('دانتيل سويسرى', 'دانتيل سويسرى'),
    ('حرير', 'حرير'),

)


wig_color = (
    ("اختر لون الباروكة", "اختر لون الباروكة"),
    ('أسود طبيعى', 'أسود طبيعى'),
    ('بنى داكن', 'بنى داكن'),
    ('بنى فاتح', 'بنى فاتح'),
    ('اشقر', 'اشقر'),
    ('مخصل', 'مخصل'),

)


density = (
    ('اختر كثافة الباروكة', 'اختر كثافة الباروكة'),
    ('130', '130'),
    ('150', '150'),
    ('200', '200'),
    ('250', '250'),

)


payment_method = (
    ('اختر طريقة الدفع', 'اختر طريقة الدفع'),
    ('tabby', 'tabby'),
    ('tamara', 'tamara'),
    ('Stripe', 'Stripe'),
    ('PayTabs', 'PayTabs'),
    ('Apple Pay', 'Apple Pay'),
    ('Bank Account Pay', 'Bank Account Pay'),
    ('Upon receipt', 'Upon receipt'),
)



class Item(models.Model):
    name = models.CharField(max_length=150, choices=wig_name, null=False)
    wig_type = models.CharField(max_length=150, choices=wig_type, null=False)
    wig_long = models.CharField(max_length=150, choices=wig_long, null=False)
    scalp_type = models.CharField(max_length=150, choices=scalp_type, null=False)
    wig_color = models.CharField(max_length=150, choices=wig_color, null=False)
    density = models.CharField(max_length=150, choices=density, null=False)
    
    price = models.IntegerField(default=1500, validators=[MaxValueValidator(15000), MinValueValidator(50)])

    # Added new...
    image = models.ImageField(default="no_product_img.png", upload_to="core_images", null=True, blank=True)

    
    quantity = models.PositiveIntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    discount_price = models.FloatField(default=0.00, blank=True, null=True)
    slug = models.SlugField()

    num_of_sales = models.PositiveIntegerField(default=1)
    


    def __str__(self):
        return f"{self.id} -- {self.slug}"

    
    # def get_absolute_url(self):
    #     return reverse("core:product", kwargs={"slug": self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={"slug":self.slug})
    
    # def get_remove_from_cart_url(self):
    #   return reverse("core:remove-from-cart", kwargs={"slug":self.slug})
    



class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.item.price * self.quantity
    
    def get_total_discount_item_price(self):
        # return self.item.discount_price * self.quantity
        return (self.item.price - self.item.discount_price) * self.quantity
    
    
    def get_amount_saved(self):
        # return (self.item.price - self.item.discount_price) * self.quantity
        return (self.item.discount_price) * self.quantity
    

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        else:
            return self.get_total_item_price()
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    done_ordered_time = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey('Bill2', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total

    def get_total_items(self):
        total_items = 0
        for order_item in self.items.all():
            total_items += order_item.quantity
        return total_items
    






class Bill2(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    seller_phone_number = models.CharField(max_length=31, null=True, blank=True)
    country = CountryField(multiple=False, blank_label="(select country)")
    address = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=31)
    date = models.DateTimeField(auto_now_add=True)
    account_name = models.CharField(max_length=150, null=True, blank=True)

    # payment method
    payment_method = models.CharField(max_length=150, choices=payment_method, null=False)

    #Item details
    wig_type = models.CharField(max_length=150, choices=wig_type, null=False)
    wig_long = models.CharField(max_length=150, choices=wig_long, null=False)
    scalp_type = models.CharField(max_length=150, choices=scalp_type, null=False)
    wig_color = models.CharField(max_length=150, choices=wig_color, null=False)
    density = models.CharField(max_length=150, choices=density, null=False)
    price = models.IntegerField(default=1500)
    # selling_price added Newlly...
    selling_price = models.PositiveIntegerField(default=0)

    pieces_num = models.PositiveIntegerField(default=0)
    account = models.ForeignKey("Account", on_delete=models.CASCADE)

    bill_pdf = models.FileField(upload_to='bills_pdf_documents/', default='billl_default_pdf.pdf')

    slug_code = models.SlugField()

    class Meta:
        # verbose_name = 'Bills'
        verbose_name_plural = 'All Bills'

    def __str__(self):
        return f"{self.seller}"
    
    
    def total_price(self):
        total = self.price * self.pieces_num
        return total
    

    def calculate_total_price(self):
        return self.pieces_num * self.selling_price
    










class Refund(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    seller_phone_number = models.CharField(max_length=31, null=True, blank=True)
    country = CountryField(multiple=False, blank_label="(select country)")
    address = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=31)
    date = models.DateTimeField(auto_now_add=True)
    account_name = models.CharField(max_length=150, null=True, blank=True)

    # payment method
    payment_method = models.CharField(max_length=150, null=False)

    #Item details
    wig_type = models.CharField(max_length=150, choices=wig_type, null=False)
    wig_long = models.CharField(max_length=150, choices=wig_long, null=False)
    scalp_type = models.CharField(max_length=150, choices=scalp_type, null=False)
    wig_color = models.CharField(max_length=150, choices=wig_color, null=False)
    density = models.CharField(max_length=150, choices=density, null=False)
    price = models.IntegerField()

    # selling_price added Newlly...
    selling_price = models.PositiveIntegerField(default=0)
    pieces_num = models.PositiveIntegerField(default=0)

    total_price = models.IntegerField()
    account = models.ForeignKey("Account", on_delete=models.CASCADE)

    # slug_code = models.SlugField()

    class Meta:
        # verbose_name = 'Bills'
        verbose_name_plural = 'All Refunds'

    def __str__(self):
        return f"{self.seller}"
    

    def calculate_total_price(self):
        return self.pieces_num * self.selling_price
    
    

    



class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField(default=0.00)

    def __str__(self):
        return self.code
    


class Offer(models.Model):
    offer = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.offer
    


class Phones(models.Model):
    phone = models.CharField(max_length=31)
    date = models.DateTimeField(auto_now_add=True)
    slug_link = models.SlugField()

    
    def __str__(self):
        return f"{self.phone}"






class PhoneNumberr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phones, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    slug_link = models.SlugField()


    def __str__(self):
        return f"{self.user.username} - {self.phone.phone}"
    
    




class Account(models.Model):
    account_name = models.CharField(max_length=200)
    tiktok_account_link = models.URLField(max_length=1000, null=False, blank=False)
    instagram_account_link = models.URLField(max_length=1000, null=False, blank=False)

    marketer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='account_marketer_name')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='account_seller_name')

    # phonenumber = models.ForeignKey(PhoneNumberr, on_delete=models.CASCADE, null=True, blank=True)


    phone = models.ForeignKey(Phones, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug_link = models.SlugField()


    def __str__(self):
        return f"{self.account_name}"
    



# the model of the add new link to show in the banks and pyament page
class AddLink(models.Model):
    link_name = models.CharField(max_length=150, null=True, blank=True)
    slug_link = models.CharField(max_length=150, unique=True, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    SAR_link = models.URLField(max_length=500, null=True, blank=True)
    USD_link = models.URLField(max_length=500, null=True, blank=True)
    AED_link = models.URLField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.slug_link



class BankAccount(models.Model):
    bank_name = models.CharField(max_length = 100, null=False, blank=False)
    country = CountryField(multiple=False, blank_label="(select country)")

    IBAN = models.CharField(max_length = 200, null=False, blank=False)
    account_number = models.CharField(max_length = 200, null=False, blank=False)
    swift_code = models.CharField(max_length = 200, null=False, blank=False)
    beneficiary_name = models.CharField(max_length = 200, null=False, blank=False)

    # validation_date = models.DateField()
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    slug_link = models.CharField(max_length=150, unique=True, null=False, blank=False)





    def __str__(self):
        return f"{self.bank_name}"
    









class Penality(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    days_num = models.IntegerField(default=0, validators=[MaxValueValidator(31), MinValueValidator(0)])
    slug_link = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} -- {self.date}"
    




class Reward(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    price = models.IntegerField(default=50, validators=[MaxValueValidator(5000), MinValueValidator(50)])
    slug_link = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} -- {self.date}"
    


class Tasks(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    ordered_date = models.DateTimeField(null=True, blank=True)
    done_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    done_task_is_read = models.BooleanField(default=False)  # To delete the notification for the done tasks after the admin read it...
    slug_link = models.SlugField()


    def __str__(self):
        return f"{self.name} -- {self.ordered_date}"
    
    def get_duration(self):
        # time_difference = your_model_instance.end_date - your_model_instance.start_date
        time_difference = self.done_date - self.ordered_date


        # Extract hours and minutes from the timedelta
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes = remainder // 60

        if time_difference.days > 0:
            # If the difference is greater than one day, include days in the output
            formatted_difference = f"{time_difference.days} يوم, {hours} ساعة, {minutes} دقيقة"
        elif hours > 0:
            # If the difference is greater than one hour, display hours and minutes
            formatted_difference = f"{hours} ساعة, {minutes} دقيقة"
        else:
            # If the difference is less than one hour, display only minutes
            formatted_difference = f"{minutes} دقيقة"

        return formatted_difference
    








class AllBillsPDF(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='monthly_bills_pdf/', default='billl_default_pdf.pdf')
    date = models.DateField(null=False, blank=False)
    slug_code = models.SlugField()
    
    
    def __str__(self):
        return self.title