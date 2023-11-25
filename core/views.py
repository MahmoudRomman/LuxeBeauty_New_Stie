from typing import Any
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template import context
from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import CreateView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from . import models
from . import forms
from datetime import datetime 
import datetime, calendar
from django.utils import timezone
import string
import random
from django.contrib.auth.models import User



# Create your views here.



def create_slug_code():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=20))





today = datetime.date.today()
month = today.month


def home(request):
    from django.contrib.auth import authenticate
    user = authenticate(username="admin", password="12345")
    print("*"* 100)
    print(user)

    items = models.Item.objects.all().order_by('-date')

    offers = models.Offer.objects.all().order_by('-date')[:3]

    new_arrived_items = models.Item.objects.all().order_by('-date')[:3]

    context = {
        'items' : items,
        'offers' : offers,
        'new_arrived_items' : new_arrived_items,
    }


    
    return render(request, 'core/index.html', context)



@login_required(login_url='user-login')
def store(request):
    if request.method == "POST":
        form = forms.ItemForm()
        
        wig_type = request.POST.get("wig_type")
        wig_long = request.POST.get("wig_long")
        scalp_type = request.POST.get("scalp_type")
        wig_color = request.POST.get("wig_color")
        density = request.POST.get("density")

        if density=='اختر كثافة الباروكة' or wig_color=='اختر لون الباروكة' or scalp_type=='اختر نوع الفروة' or wig_long=='طول الباروكة' or wig_type=='اختر نوع الباروكة':
            data = models.Item.objects.all()
            paginator = Paginator(data, 7)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        else:
            data = models.Item.objects.filter(wig_type = wig_type, wig_long = wig_long,
                                                scalp_type = scalp_type, wig_color = wig_color,
                                                density = density)
            
            paginator = Paginator(data, 7)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        context = {
            'page_obj' : page_obj,
            'form' : form,
        }

        return render(request, 'core/store.html', context)

    else:
        form = forms.ItemForm()
        data = models.Item.objects.all()
        paginator = Paginator(data, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj' : page_obj,
            'form' : form,
        }

        return render(request, 'core/store.html', context)



@login_required(login_url='user-login')
def add_item(request):

    form = forms.ItemForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            wig_type = form.cleaned_data.get("wig_type")
            wig_long = form.cleaned_data.get("wig_long")
            scalp_type = form.cleaned_data.get("scalp_type")
            wig_color = form.cleaned_data.get("wig_color")
            density = form.cleaned_data.get("density")
            price = form.cleaned_data.get("price")
            discount_price = form.cleaned_data.get("discount_price")
            quantity = form.cleaned_data.get("quantity")

            if density=='اختر كثافة الباروكة' or wig_color=='اختر لون الباروكة' or scalp_type=='اختر نوع الفروة' or wig_long=='طول الباروكة' or wig_type=='اختر نوع الباروكة':
                 messages.warning(request, "هناك خطأ من فضلك راجع المدخلات مره أخرى")
            else:

                check_the_item = models.Item.objects.filter(
                    name = name, wig_type = wig_type,
                    wig_long = wig_long, scalp_type = scalp_type,
                    wig_color = wig_color, density = density,
                    )
                if len(check_the_item) == 0:
                    create_slug = create_slug_code()
                    new_item = models.Item.objects.create(
                        name = name,
                        wig_type = wig_type,
                        wig_long = wig_long,
                        scalp_type = scalp_type,
                        wig_color = wig_color,
                        density = density,
                        price = price,
                        discount_price = discount_price,
                        quantity = quantity,

                        slug = create_slug
                        )

                    new_item.save()
                    messages.success(request, "تم اضافة المنتج الجديد بنجاح")
                    return redirect("store")
                else:
                    messages.warning(request, ".هذ المنتج موجود بالفعل يمكنك تعديل السعر او الكمية له")
                    return redirect("store")

    context = {
        'form' : form,
    }

    return render(request, 'core/add_item.html', context)



@login_required(login_url='user-login')
def edit_item_in_store(request, slug):
    item = models.Item.objects.get(slug=slug)

    if request.method == "POST":
        form = forms.EditItemForm(request.POST, instance=item)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            wig_type = form.cleaned_data.get("wig_type")
            wig_long = form.cleaned_data.get("wig_long")
            scalp_type = form.cleaned_data.get("scalp_type")
            wig_color = form.cleaned_data.get("wig_color")
            density = form.cleaned_data.get("density")
            price = form.cleaned_data.get("price")
            discount_price = form.cleaned_data.get("discount_price")
            quantity = form.cleaned_data.get("quantity")
            if density=='اختر كثافة الباروكة' or wig_color=='اختر لون الباروكة' or scalp_type=='اختر نوع الفروة' or wig_long=='طول الباروكة' or wig_type=='اختر نوع الباروكة':
                 messages.warning(request, "هناك خطأ من فضلك راجع المدخلات مره أخرى")
            else:
                models.Item.objects.filter(slug=slug).update(
                    name = name, wig_type = wig_type,
                    wig_long = wig_long, scalp_type = scalp_type,
                    wig_color = wig_color, density = density,
                    price=price, discount_price = discount_price,
                    quantity = quantity)
                
                messages.success(request, "تم تعديل هذا المنتج بنجاح")
                return redirect("store")
    else:
        form = forms.EditItemForm(instance=item)

    context = {
        'form' : form,
    }
    return render(request, 'core/edit_item.html', context)



@login_required(login_url='user-login')
def delete_from_store(request, slug):
    item = models.Item.objects.get(slug=slug)

    if request.method == "POST":
        item.delete()
        messages.success(request, ".تم ازالة هذا المنتج من المخزن")
        return redirect("store")
    
    return render(request, 'core/delete_item_confirm.html')



@login_required(login_url='user-login')
def shop(request):
    if request.method == "POST":
        form = forms.ItemForm()
        
        wig_type = request.POST.get("wig_type")
        wig_long = request.POST.get("wig_long")
        scalp_type = request.POST.get("scalp_type")
        wig_color = request.POST.get("wig_color")
        density = request.POST.get("density")

        if density=='اختر كثافة الباروكة' or wig_color=='اختر لون الباروكة' or scalp_type=='اختر نوع الفروة' or wig_long=='طول الباروكة' or wig_type=='اختر نوع الباروكة':
            data = models.Item.objects.all()
            paginator = Paginator(data, 7)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        else:
            data = models.Item.objects.filter(wig_type = wig_type, wig_long = wig_long,
                                                scalp_type = scalp_type, wig_color = wig_color,
                                                density = density)
            
            paginator = Paginator(data, 7)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        context = {
            'page_obj' : page_obj,
            'form' : form,
        }

        return render(request, 'core/shop.html', context)
    

    else:
        form = forms.ItemForm()
        data = models.Item.objects.all()
        paginator = Paginator(data, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj' : page_obj,
            'form' : form,
        }

        return render(request, 'core/shop.html', context)
    
    


# This function used to set the item to the cart in addition update the product quantity in the store...
# Done perfectly.....
# def add_to_cart(request, slug):
#     # get the item
#     item = get_object_or_404(models.Item, slug=slug)

#     # create an order item or that order or get it if it exists
#     order_item, created = models.OrderItem.objects.get_or_create(
#         item=item,
#         user=request.user,
#         ordered=False
#         )
    
#     order_qs = models.Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the orderitem is in the order
#         if order.items.filter(item__slug = item.slug).exists():
#             if item.quantity > 0:
#                 order_item.quantity += 1
#                 order_item.save()

#                 # Update the quantity for the item in the cart
#                 models.Item.objects.filter(slug=slug).update(quantity = (item.quantity - 1))

#                 messages.success(request, "تم تعديل الكمية لهذا المنتج بنجاح")
#                 return redirect("order_summary")
#             else:
#                 messages.warning(request, "هذا المنتج خارج المخزن")
#                 return redirect("shop")
#         else:
#             if item.quantity > 0:
#                 order.items.add(order_item)
#                 # Update the quantity for the item in the cart
#                 models.Item.objects.filter(slug=slug).update(quantity = (item.quantity - 1))
#                 messages.success(request, "تمت اضافة هذا المنتج الى السلة بنجاح" )
#                 return redirect("order_summary")
#             else:
#                 messages.warning(request, "هذا المنتج خارج المخزن")
#                 return redirect("shop")



#     else: 
#         if item.quantity > 0:

#             # Update the quantity for the item in the cart
#             models.Item.objects.filter(slug=slug).update(quantity = (item.quantity - 1))

#             ordered_date = timezone.now()
#             order = models.Order.objects.create(user=request.user, ordered_date=ordered_date)
#             order.items.add(order_item)
#             messages.success(request, "تمت اضافة هذا المنتج الى السلة بنجاح")
#             redirect("shop")

#             return redirect("order_summary")
#         else:
#             messages.warning(request, "هذا المنتج خارج المخزن")
#             return redirect("shop")


@login_required(login_url='user-login')
def add_to_cart(request, slug):
    # get the item
    item = get_object_or_404(models.Item, slug=slug)

    if item.quantity == 0:
        messages.warning(request, "هذا المنتج خارج المخزن")
        return redirect("shop")
    else:    
        # create an order item or that order or get it if it exists
        order_item, created = models.OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
            )
        
        order_qs = models.Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            # check if the orderitem is in the order
            if order.items.filter(item__slug = item.slug).exists():
                if item.quantity > 0:
                    order_item.quantity += 1
                    order_item.save()

                    # Update the quantity for the item in the cart
                    models.Item.objects.filter(slug=slug).update(quantity = (item.quantity - 1))

                    messages.success(request, "تم تعديل الكمية لهذا المنتج بنجاح")
                    return redirect("order_summary")
                else:
                    messages.warning(request, "هذا المنتج خارج المخزن")
                    return redirect("shop")
            else:
                if item.quantity > 0:
                    order.items.add(order_item)
                    # Update the quantity for the item in the cart
                    models.Item.objects.filter(slug=slug).update(quantity = (item.quantity - 1))
                    messages.success(request, "تمت اضافة هذا المنتج الى السلة بنجاح" )
                    return redirect("order_summary")
                else:
                    messages.warning(request, "هذا المنتج خارج المخزن")
                    return redirect("shop")
        else: 
            # Update the quantity for the item in the cart
            models.Item.objects.filter(slug=slug).update(quantity = (item.quantity - 1))

            ordered_date = timezone.now()
            order = models.Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            messages.success(request, "تمت اضافة هذا المنتج الى السلة بنجاح")
            redirect("shop")

            return redirect("order_summary")

            

@login_required(login_url='user-login')
def remove_single_item_from_cart(request, slug):
    # get the item
    item = get_object_or_404(models.Item, slug=slug)
    
    order_qs = models.Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if the orderitem is in the order
        if order.items.filter(item__slug = item.slug).exists():
            order_item = models.OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]

            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()

                # Update the quantity for the item in the cart
                models.Item.objects.filter(slug=slug).update(quantity = (item.quantity + 1))

                messages.success(request, ".تم تعديل الكمية لهذا المنتج")
                return redirect("order_summary")
            else:
                models.Item.objects.filter(slug=slug).update(quantity = (item.quantity + 1))
                order.items.remove(order_item)
                order_item.save()
                messages.success(request, ".تم ازالة هذا المنتج من السلة")
                return redirect("order_summary")


        else:
            messages.info(request, "!هذا المنتج غير موجود فى السلة")
            return redirect("shop")
    else:
        messages.info(request, "!ليس لديك فاتورة")
        return redirect("shop")
    


@login_required(login_url='user-login')
def remove_from_cart(request, slug):
    # get the item
    item = get_object_or_404(models.Item, slug=slug)
    
    order_qs = models.Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if the orderitem is in the order
        if order.items.filter(item__slug = item.slug).exists():
            order_item = models.OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]

            # Update the quantity for the item in the cart
            models.Item.objects.filter(slug=slug).update(quantity = (item.quantity + order_item.quantity))
            
            order.items.remove(order_item)
            messages.success(request, ".تم ازالة هذا المنتج من السلة")
            return redirect("order_summary")

        else:
            messages.info(request, "!هذا المنتج غير موجود فى السلة")
            return redirect("shop", slug=slug)
    else:
        messages.info(request, "!ليس لديك فاتورة")
        return redirect("shop")






@login_required(login_url='user-login')
def order_summary(request):
    try:
        order = models.Order.objects.get(user=request.user, ordered=False)

        context = {
            'object' : order,
            # 'couponform' : forms.CouponForm(),
            # 'DISPLAY_COUPON_FORM' : True,
        }

        return render(request, 'core/order_summary.html', context)
    except ObjectDoesNotExist:
        messages.warning(request, ".ليس لديك طلب شراء مٌفعل, من فضلك أضف أحد المنتجات الى السلة أولاً")
        return redirect("shop")





# class bill(CreateView):
    
#     model = models.Billl
#     form_class = forms.BillForm
#     template_name = 'core/bill.html'
#     success_url = reverse_lazy('chart_view')
    

#     def form_valid(self, form):
#         order = models.Order.objects.get(user=self.request.user, ordered=False)
#         # order_item = models.OrderItem.objects.get(user=self.request.user, ordered=False)

#         seller_phone_number = form.cleaned_data.get("seller_phone_number")
        

#         phone = models.PhoneNumber.objects.get(phone = str(seller_phone_number))
#         account = models.Account.objects.get(phone_number = phone)
        

#         num = order.get_total_items()


#         form.instance.seller = self.request.user
#         form.instance.pieces_num = num
#         form.instance.account_name = account.account_name


#         # order_item.ordered = True
#         order.ordered = True

#         # order_item.save()
#         order.save()



#         messages.success(self.request, ".تم حفظ الفاتورة بنجاح")
#         return super(bill,self).form_valid(form)    

#     def get_form_kwargs(self):
#         """ Passes the request object to the form class.
#          This is necessary to only display members that belong to a given user"""

#         kwargs = super(bill, self).get_form_kwargs()
#         kwargs['request'] = self.request
#         return kwargs
    
    


from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class LoginRequiredMixin(object):
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())
    

class bill2(CreateView, LoginRequiredMixin):
    model = models.Bill2
    form_class = forms.BillForm2
    template_name = 'core/bill.html'
    success_url = reverse_lazy('chart_view')
    order = None

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(bill2, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    

    def form_valid(self, form):
        order = models.Order.objects.get(user=self.request.user, ordered=False)

        orders_num = order.items.all()
        one_bill = orders_num[0]
        
        seller_phone_number = form.cleaned_data.get("seller_phone_number")

        country = form.cleaned_data.get("country")
        address = form.cleaned_data.get("address")
        customer_phone = form.cleaned_data.get("customer_phone")
        customer_name = form.cleaned_data.get("customer_name")

        

        phone = models.PhoneNumber.objects.get(phone = str(seller_phone_number))

        try:
            # to edit this if the marketing have no account....
            account = models.Account.objects.get(phone_number = phone)


            form.instance.seller = self.request.user
            form.instance.account_name = account.account_name

            form.instance.wig_type = one_bill.item.wig_type
            form.instance.wig_long = one_bill.item.wig_long
            form.instance.scalp_type = one_bill.item.scalp_type
            form.instance.wig_color = one_bill.item.wig_color
            form.instance.density = one_bill.item.density
            form.instance.price = one_bill.item.price
            form.instance.pieces_num = one_bill.quantity




            country = form.cleaned_data.get("country")
            address = form.cleaned_data.get("address")
            customer_phone = form.cleaned_data.get("customer_phone")
            customer_name = form.cleaned_data.get("customer_name")
            orders_num = orders_num[1:]
            for other_orders in orders_num:
                new_bill2 = models.Bill2.objects.create(
                    seller = self.request.user,
                    seller_phone_number = seller_phone_number,
                    country = country,
                    address = address,
                    customer_phone = customer_phone,
                    customer_name = customer_name,
                    account_name = account.account_name,

                    wig_type = other_orders.item.wig_type,
                    wig_long = other_orders.item.wig_long,
                    scalp_type = other_orders.item.scalp_type,
                    wig_color = other_orders.item.wig_color,
                    density = other_orders.item.density,
                    price = other_orders.item.price,
                    pieces_num = other_orders.quantity

                )

                new_bill2.save()

            order_items = order.items.all()
            order_items.update(ordered = True)
            for item in order_items:
                item.save()


            order.ordered = True
            order.save()


            from datetime import datetime

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


            # # Sending mail
            email = EmailMessage(
            subject=f"New Bill From The LuxeBeauty Site Version_2 Which Made By {self.request.user} at {dt_string}",
            body="This one", 
            from_email= settings.EMAIL_HOST_USER,
            to=(settings.EMAIL_HOST_USER,),
            reply_to=(settings.EMAIL_HOST_USER,),
            )

            email.send()


            # New mail to be edited...
            # data = {
            #     "fname" : self.request.user,
            #     "date" : dt_string,
            # }

            # message = get_template('doctor/email.html').render(data)
            # email = EmailMessage(
            #     "About your appointment with Med-Care Center.",
            #     message,
            #     settings.EMAIL_HOST_USER,
            #     [settings.EMAIL_HOST_USER],
            # )

            # email.content_subtype = "html"
            # email.send()



            messages.success(self.request, ".تم حفظ الفاتورة بنجاح")
            return super(bill2,self).form_valid(form)
        except:
            messages.warning(self.request, ".عفواً, لا يوجد مُسوق للرقم الذى قٌمت باختياره")
            return redirect("bill2")



@login_required(login_url='user-login')
def show_bills(request):
    form = forms.BillFilterForAdmin()

    today = datetime.date.today()



    year = today.year
    month = today.month

    # my_bills = models.Bill2.objects.filter(seller=request.user, date__month=month, date__day=str(f"{bills_per_day+1}"))
    data = models.Bill2.objects.filter(date__year = year, date__month = month)
    bills_num_this_month = 0
    for bill in data:
        bills_num_this_month += bill.pieces_num


    if request.method == "POST":
        form = forms.BillFilterForAdmin(request.POST)
        today_day = request.POST.get("today_day")

        if today_day == "كل الايام":
            data = models.Bill2.objects.filter(date__year = year, date__month = month)  
            paginator = Paginator(data, 7)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            data = 0
        else:
            today_day = int(today_day)
            data = models.Bill2.objects.filter(date__year = year, date__month = month, date__day = today_day)
            page_obj = 0
    else:
        data = models.Bill2.objects.filter(date__year = year, date__month = month)
        paginator = Paginator(data, 7)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = 0




    context = {
        'page_obj' : page_obj,
        'data' : data,
        'bills_num_this_month' : bills_num_this_month,
        'form' : form
        }

    return render(request, 'core/show_bills.html', context)








# class show_bills(CreateView):
    
#     model = models.Bill2
#     form_class = forms.BillForm2
#     template_name = 'core/show_bills.html'
#     success_url = reverse_lazy('all_bills')


#     def get_form_kwargs(self):
#         kwargs = super(show_bills, self).get_form_kwargs()
#         kwargs['request'] = self.request
#         return kwargs


#     def get_context_data(self):
#         context = super(show_bills, self).get_context_data()
        

#         data = models.Bill2.objects.all()

#         paginator = Paginator(data, 1)
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
        
#         context = {
#             'page_obj' : page_obj,
#         }
#         return context




@login_required(login_url='user-login')
def banks(request):

    links_data = models.AddLink.objects.all()


    context = {
        'links_data' : links_data,
    }
    return render(request, 'core/banks.html', context)



@login_required(login_url='user-login')
def add_payment_link(request):

    form = forms.AddLinkForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            link_name = form.cleaned_data.get("link_name")
            amount = form.cleaned_data.get("amount")
            SAR_link = form.cleaned_data.get("SAR_link")
            AED_link = form.cleaned_data.get("AED_link")


            
            create_slug = create_slug_code()

            new_link = models.AddLink.objects.create(
                link_name = link_name,
                slug_link = create_slug,
                amount = amount,
                SAR_link = SAR_link,
                AED_link = AED_link,
                )

            new_link.save()
            messages.success(request, "تم اضافة الرابط الجديد بنجاح")
            return redirect("banks_and_payments")



    context = {
        'form' : form,
    }

    return render(request, 'core/add_new_link.html', context)



@login_required(login_url='user-login')
def delete_payment_link(request, slug):
    models.AddLink.objects.filter(slug_link=slug).delete()
    messages.info(request, "item deleted successfully")
    return redirect("banks_and_payments")





today = datetime.date.today()


@login_required(login_url='user-login')
def chart_data(request):

    year = today.year
    month = today.month
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days+1)]
    

    randomlist = []
    today_in_month = int(today.day)

    for bills_per_day in range(today_in_month):
        my_bills = models.Bill2.objects.filter(seller=request.user, date__month=month, date__day=str(f"{bills_per_day+1}"))

        peices = 0
        for bill in my_bills:
            peices += bill.pieces_num
        randomlist.append(peices)


    labels = days
    values = randomlist
    
    chart_data = {
        'label': 'خريطة المبيعات الخاصة بك خلال هذا الشهر',
        'labels': labels,
        'values': values,
        'chart_type': 'bar' # any chart type line, bar, ects
    }
    
    return JsonResponse(chart_data)





@login_required(login_url='user-login')
def chart_view(request):
    my_bills = models.Bill2.objects.filter(seller=request.user, date__month=today.month)

    bills_dict = {} 
    for bill in my_bills:
        if bill.seller_phone_number not in bills_dict:
            bills_dict[str(bill.seller_phone_number)] = int(bill.pieces_num)
        else:
            bills_dict[str(bill.seller_phone_number)] += int(bill.pieces_num)



    final_salary = 2000
    for key, value in bills_dict.items():
        salary = 0
        
        if value < 10:
            salary = 0
        elif value==10 or value<20:
            salary = value*100 
        elif value==20 or value<30:
            salary = value*150 
        elif value==30 or value>30:
            salary = value*200 

        final_salary += salary
    


    total_bills = 0
    for bill in my_bills:
        total_bills += bill.pieces_num


    context = {
        'my_bills' : my_bills,
        'total_bills' : total_bills,

        'bills_dict' : bills_dict,
        'final_salary' : final_salary,
    }
    return render(request, 'core/chart.html', context)




def show_all_penalities(request):
    penalities = models.Penality.objects.all().order_by('-date')

    context = {
        'penalities' : penalities,
    }
    return render(request, 'core/penalities.html', context)




def penality(request):
    form = forms.PenalityForm()

    if request.method == "POST":
        form = forms.PenalityForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            message = form.cleaned_data.get("message")

            create_slug = create_slug_code()

            new_user_penality = models.Penality.objects.create(
                name = name,
                message = message,
                slug_link = create_slug,
            )

            new_user_penality.save()
            messages.success(request, ".تم اضافة الخَصم لهذا المستخدم بنجاح")
            return redirect("show_all_penalities")

    context = {
        'form' : form,
    }
    return render(request, 'core/add_penality.html', context)


def user_penality(request):
    my_penalities = models.Penality.objects.filter(name=request.user).order_by('-date')


    context = {
        'my_penalities' : my_penalities,
    }

    return render(request, 'core/user_penality.html', context)



def delete_penality(request, slug):
    penality = models.Penality.objects.filter(slug_link=slug)
    penality.delete()
    messages.success(request, ".تم ازالة الخَصم لهذا المستخدم بنجاح")
    return redirect("show_all_penalities")
