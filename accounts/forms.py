from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from . import models
from core.models import Phones, PhoneNumberr








class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    error_messages = {
    'invalid_login': (
        "من فضلك ادخل اسم مستخدم وكلمة مرور صحيحة "
        "انتبه الى ان اسم المستخدم وكلمة السر حساسة للحروف والارقام."
    ),
    }

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "ادخل اسم المستخدم",
        'style': 'border-color:wightblack; border-radius: 10px;',
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "ادخل كلمة المرور",
        'style': 'border-color:wightblack; border-radius: 10px;',
    }))








class CreateUserForm(UserCreationForm):

    error_messages = {
        'password_mismatch': "كلمتى المرور التى قمت بادخالهما غير متشابهين",
        'username_taken': "اسم المستخدم هذا موجود بالفعل",
    }


    username = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "text",
        "placeholder" : "ادخل اسم المستخدم",
        'style': 'border-color:wightblack; border-radius: 10px;',
    }), label="Username")


    email = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "email",
        "placeholder" : "ادخل البريد الالكترونى",
        'style': 'border-color:wightblack; border-radius: 10px;',
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "password",
        "placeholder" : "ادخل كلمة السر",
        'style': 'border-color:wightblack; border-radius: 10px;',
    }))


    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "password",
        "placeholder" : "أعد احال كلمة السر مرة أخرى",
        'style': 'border-color:wightblack; border-radius: 10px;',
    }))



    job_type = forms.ChoiceField(
        choices = models.job_type,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'style': 'border-color:wightblack; border-radius: 10px;',
    }))



    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']







from django.contrib.auth import get_user_model



class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Custom Email Label",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            "class": "input",
            "type": "email",
            "placeholder": "ادخل عنوان البريد الالكترونى",
            'style': 'border-color:wightblack; border-radius: 10px;'
            }),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        UserModel = get_user_model()

        if not UserModel.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("لا يوجد حساب مُفعل لهذا البريد الالكترونى , حاول مرة أخرى")
        
        return email






    

class CustomPasswordResetConfirmForm(SetPasswordForm):


    error_messages = {
        'password_mismatch': "كلمتى المرور التى قمت بادخالهما غير متشابهين",
        'password_too_short': "كلمة المرور الجديدة قصيرة للغاية",
    }


    new_password1 = forms.CharField(
        label="New Custom Password Label",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            "class" : "input",
            "type" : "password",
            "placeholder" : "ادخل كلمة السر الجديدة",
            'style': 'border-color:wightblack; border-radius: 10px;',
            }),
    )

    new_password2 = forms.CharField(
        label="Confirm Custom Password Label",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            "class" : "input",
            "type" : "password",
            "placeholder" : "أعد ادخال كلمة السر الجديدة مرة أخرى",
            'style': 'border-color:wightblack; border-radius: 10px;',
            }),
    )

    class Meta:
        model = User
        fields = ("new_password1", "new_password2")




class CustomPasswordChangeForm(PasswordChangeForm):

    error_messages = {
        'password_incorrect': "كلمة السر القديمة الخاصة بك غير صحيحة",
        'password_mismatch': "كلمتى المرور التى قمت بادخالهما غير متشابهين",
        'password_too_short': "كلمة المرور الجديدة قصيرة للغاية",
    }



    old_password = forms.CharField(
        label="Current Password",
        widget=forms.PasswordInput(attrs={
            "class" : "input",
            "type" : "password",
            "placeholder" : "ادخل كلمة السر الحالية",
            'style': 'border-color:wightblack; border-radius: 10px;',
            }))
    
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
            "class" : "input",
            "type" : "password",
            "placeholder" : "ادخل كلمة السر الجديدة",
            'style': 'border-color:wightblack; border-radius: 10px;',
            }))

    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={
            "class" : "input",
            "type" : "password",
            "placeholder" : "أعد ادخال كلمة السر الجديدة مرة أخرى",
            'style': 'border-color:wightblack; border-radius: 10px;',
            }))




    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")




class UserUpdateForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': "كلمتى المرور التى قمت بادخالهما غير متشابهين",
        'username_taken': "اسم المستخدم هذا موجود بالفعل",
    }


    username = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "text",
        "placeholder" : "ادخل اسم المستخدم",
        'style': 'border-color:wightblack; border-radius: 10px;',
    }), label="Username")


    # email = forms.CharField(widget=forms.TextInput(attrs={
    #     "class" : "input",
    #     "type" : "email",
    #     "placeholder" : "ادخل البريد الالكترونى",
    #     'style': 'border-color:wightblack; border-radius: 10px;',
    # }))


    email = forms.EmailField(
        label="Custom Email Label",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            "class": "input",
            "type": "email",
            "placeholder": "ادخل عنوان البريد الالكترونى",
            'style': 'border-color:wightblack; border-radius: 10px;'
            }),
    )
    class Meta:
        model = User
        fields = ['username', 'email']




class ProfileUpdateForm(forms.ModelForm):

    address = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "text",
        "placeholder" : "ادخل العنوان الشخصى",
        'style': 'border-color:wightblack; border-radius: 10px;',
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "text",
        "placeholder" : "ادخل رقم الهاتف الخاص بك",
        'style': 'border-color:wightblack; border-radius: 10px;',
    }))



    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class" : "input",
        "type" : "file",
        'style': 'display: none;',
        'id' : 'image-input',
        'name' : 'profile_image',
        'accept' : 'image/*',
    }))

    job_type = forms.ChoiceField(
        choices = models.job_type,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'style': 'border-color:wightblack; border-radius: 10px;',

        # 'type' : "text",
        # 'id' : "inputField",
        # 'value' : "Choose Job Type",
    }))


 

    class Meta:
        model = models.Profile
        fields = ['address', 'phone', 'image', 'job_type']




class AllPhonesForm(forms.Form):
    phone = forms.ModelMultipleChoiceField(
        queryset=Phones.objects.all(), 
        widget=forms.CheckboxSelectMultiple
    )


