from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import importlib
from . import forms
from . import models
from core.models import PhoneNumber
from django.contrib import messages
# Create your views here.



def register(request):
    if request.method == "POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            if User.objects.filter(email=email).exists():
                messages.warning(request, ".الايميل الذى قمت بتسجيله موجود بالفعل, من فضلك أعد التسجيل بعنوان ايميل أخر")
                return redirect('user-register')
            else:
                form.save()
                username = form.cleaned_data.get('username')
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
    my_phones = PhoneNumber.objects.filter(user=request.user)

    context = {
        'profile' : profile,
        'my_phones' : my_phones,
    }
    return render(request, 'accounts/profile.html', context)



@login_required(login_url='user-login')
def profile_update(request):
    if request.method == 'POST':
        user_form = forms.UserUpdateForm(request.POST, instance=request.user)
        profile_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
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
    phone_update_form = forms.PhoneUpdate()
    if request.method == "POST":
        phone_update_form = forms.PhoneUpdate(request.POST or None)
        if phone_update_form.is_valid():
            # phone_update_form.save()

            phones = phone_update_form.cleaned_data.get("new_phone")

            for cnt in range(len(phones)):
                # To check if the entered phone number is already save to the current user or not...
                founded = PhoneNumber.objects.filter(user = request.user, phone = int(phones[cnt]))
                # To reload this file --- forms.py file
                importlib.reload(forms)


                if founded:
                    continue
                else:
                    new_user_phone = PhoneNumber.objects.create(user=request.user, phone=int(phones[cnt]))
                    new_user_phone.save()
            # To reload this file --- forms.py file
            importlib.reload(forms)
                
            messages.success(request, ".تم حفظ التعديلات الارقام الخاصة بك")
            return redirect("user-profile")
        
        
    else:
        phone_update_form = forms.PhoneUpdate()




    context = {
        'phone_update_form' : phone_update_form,
    }

    return render(request, 'accounts/phone_update.html', context)





@login_required(login_url='user-login')
def remove_phone(request, phone):
    phone = PhoneNumber.objects.get(user=request.user, phone=phone)


    if request.method == "POST":
        phone.delete()
        # To reload this file --- forms.py file
        importlib.reload(forms)
        messages.success(request, ".تم ازالة هذا الرقم من ملفك الشخصى")
        return redirect("user-profile")
    
    
    return render(request, 'accounts/phone_deletion_confirm.html')



