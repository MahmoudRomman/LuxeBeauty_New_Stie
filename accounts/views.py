from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
import importlib
from . import forms
from . import models

from core import views as core_views
from core import custom_permissions as core_custom_permissions

from core import models as core_models
from django.contrib import messages


from django.views.decorators.cache import never_cache
from django.views.decorators.clickjacking import xframe_options_deny
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist


from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordChangeView
from django.urls import reverse_lazy




# Create your views here.


@method_decorator(never_cache, name='dispatch')
@method_decorator(xframe_options_deny, name='dispatch')
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        return response
    




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







def register(request):
    if request.method == "POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            job_type = form.cleaned_data.get("job_type")


            if User.objects.filter(email=email).exists():
                messages.warning(request, ".الايميل الذى قمت بتسجيله موجود بالفعل, من فضلك أعد التسجيل بعنوان ايميل أخر")
                # return redirect('user-register')
            elif job_type == "Choose Job Type":
                messages.warning(request, ".من فضلك أختر نوع العمل")
            else:

                form.save()
                
                job_type = form.cleaned_data.get("job_type")
                username = form.cleaned_data.get('username')
                user = User.objects.get(username = username)

                profile = models.Profile.objects.get(staff = user)
                profile.job_type = job_type
                profile.save()

                # if job_type == "Seller":
                #     user.user_permissions.add(core_views.can_make_order_permission)
                #     user.save()

                from django.contrib.auth.models import Permission

                if job_type == "Seller":
                    # try:
                    #     custom_permission = Permission.objects.filter(codename='can_make_order', name='Can Make Order')

                    #     user.user_permissions.add(custom_permission)
                    #     user.save()
                    # except ObjectDoesNotExist:
                    #     custom_permissions.can_make_order_permission
                    #     custom_permission = Permission.objects.get(codename='can_make_order', name='Can Make Order')
                    #     user.user_permissions.add(custom_permission)
                    #     user.save()

                    custom_permission = Permission.objects.filter(codename='can_make_order', name='Can Make Order')
                    if len(custom_permission):
                            custom_permission = Permission.objects.get(codename='can_make_order', name='Can Make Order')

                            user.user_permissions.add(custom_permission.id)

                            user.save()
                    else:
                        permission = core_custom_permissions.create_custom_permission()

                        codename = permission.codename
                        name = permission.name

                        custom_permission = Permission.objects.get(codename=codename, name=name)
                        user.user_permissions.add(custom_permission.id)
                        user.save()


                messages.success(request, f'.لقد قمت بانشاء حساب الان, للأستمرار برجاء تسجيل الدخول {username}')
                return redirect('user-login')
    else:
        form = forms.CreateUserForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


@login_required(login_url='user-login')
def profile(request):
    profile = models.Profile.objects.get(staff=request.user)
    my_phones = core_models.PhoneNumberr.objects.filter(user=request.user)
    if (len(my_phones)):
        # For marketer details
        marketer_phones_details = []
        for phone in my_phones:
            account = core_models.Account.objects.filter(phone=phone.phone)
            if len(account):
                account = core_models.Account.objects.get(phone=phone.phone)
                marketer_phones_details.append({'phone': phone.phone, 'seller': account.seller.username})
            else:
                marketer_phones_details = []
                marketer_phones_details.append({'phone': phone.phone, 'seller': "لا يوجد الى الان"})


        # For seller details
        seller_phones_details = []
        for phone in my_phones:
            account = core_models.Account.objects.filter(phone=phone.phone)
            if len(account):
                account = core_models.Account.objects.get(phone=phone.phone)
                seller_phones_details.append({'phone': phone.phone, 'marketer': account.marketer.username})
            else:
                seller_phones_details.append({'phone': phone.phone, 'marketer': "لا يوجد الى الان"})

    else:
        my_phones = []
        marketer_phones_details = []
        seller_phones_details = []
        


    context = {
        'profile' : profile,
        'my_phones' : my_phones,
        'marketer_phones_details' : marketer_phones_details,
        'seller_phones_details' : seller_phones_details,
    }
    return render(request, 'accounts/profile.html', context)



@login_required(login_url='user-login')
def profile_update(request):
    if request.method == 'POST':
        user_form = forms.UserUpdateForm(request.POST, instance=request.user)
        profile_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        current_user_profile = models.Profile.objects.get(staff=request.user)

        # if profile_form.is_valid():
        #     image = profile_form.cleaned_data.get('image')
        #     profile = models.Profile.objects.get(staff=request.user)
        #     profile.image = image
        #     profile.save()
        #     messages.success(request, "تم حفظ الصورة الشخصية")


        # if user_form.is_valid() and profile_form.is_valid():
        #     job_type = profile_form.cleaned_data.get("job_type")
        #     if job_type == "Choose Job Type":
        #         messages.warning(request, ".من فضلك أختر نوع العمل")
        #     else:
        #         user_form.save()
        #         profile_form.save()
        #         messages.success(request, "تم حفظ التعديلات")
        #         return redirect('user-profile')



        if user_form.is_valid() and profile_form.is_valid():
            job_type = profile_form.cleaned_data.get("job_type")
            if job_type == "Choose Job Type":
                messages.warning(request, ".من فضلك أختر نوع العمل")
            else:
                if job_type != current_user_profile.job_type:
                    my_phones = core_models.PhoneNumberr.objects.filter(user=request.user)
                    if(len(my_phones)):
                        if current_user_profile.job_type == "Seller":
                            messages.warning(request, "عفواً, لا يمكن تغيير نوع العمل, لديك أرقام خاصة تم تعينها لك")
                            return redirect('user-profile-update')
                        else:
                            my_accounts = core_models.Account.objects.filter(marketer=request.user)
                            if (len(my_accounts)):
                                messages.warning(request, "عفواً, لا يمكن تغيير نوع العمل, لديك أرقام خاصة تم تعينها لك و لديك حساب مُسوق خاص بك")
                                return redirect('user-profile-update')

                            else:
                                messages.warning(request, "عفواً, لا يمكن تغيير نوع العمل, لديك أرقام خاصة تم تعينها لك")
                                return redirect('user-profile-update')


                    else:
                        user_form.save()
                        profile_form.save()
                        messages.success(request, "تم حفظ التعديلات")
                        return redirect('user-profile')
                else: 
                    user_form.save()
                    profile_form.save()
                    messages.success(request, "تم حفظ التعديلات")
                    return redirect('user-profile')
    else:
        user_form = forms.UserUpdateForm(instance=request.user)
        profile_form = forms.ProfileUpdateForm(instance=request.user.profile)


    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/profile_update.html', context)


@login_required(login_url='user-login')
def phone_update(request):
    if request.method == 'POST':
        form = forms.AllPhonesForm(request.POST)
        if form.is_valid():
            phones = form.cleaned_data['phone']

            for phone in phones:
                # To check if the entered phone number is already save to the current user or not...
                founded = core_models.PhoneNumberr.objects.filter(user=request.user, phone = phone)
                
                if founded:
                    continue
                else:
                    new_user_phone = core_models.PhoneNumberr.objects.create(user=request.user, phone=phone)
                    new_user_phone.save()


            messages.success(request, ".تم حفظ تعديلات الارقام الخاصة بك")
            return redirect("user-profile")
    else:
        form = forms.AllPhonesForm()


    context = {
        'form' : form,
    }

    return render(request, 'accounts/phone_update.html', context)







@login_required(login_url='user-login')
def remove_phone(request, phone_id):
    phone = core_models.PhoneNumberr.objects.get(user=request.user, phone__id=phone_id)

    if request.method == "POST":
        phone.delete()
        messages.success(request, ".تم ازالة هذا الرقم من ملفك الشخصى")
        return redirect("user-profile")
    
    
    return render(request, 'accounts/phone_deletion_confirm.html')






from django.contrib.auth import logout
from django.shortcuts import redirect

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = forms.CustomPasswordChangeForm
    success_url = reverse_lazy('user-logout')
    # success_url = '/password_change_complete/'


    # def post_change_redirect(self, request, user):
    #     # Log the user out to invalidate the session
    #     logout(user)
    #     return redirect(self.success_url)



 
    
@login_required(login_url='user-login')
def password_change_complete(request):
    return render(request, 'accounts/password_change_complete.html')


    