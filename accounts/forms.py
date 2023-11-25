from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
from core.models import PhoneNumber, Phones



class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['address', 'phone', 'image']





def phones_func():
    all_phones_lst = []
    all_phones = Phones.objects.all()
    for phone in all_phones:
        all_phones_lst.append(int(phone.phone))


    # To get only the tanke phone numbers by users...
    phone_taken_lst = []
    phone_taken = PhoneNumber.objects.all()
    for phone in phone_taken:
        phone_taken_lst.append(int(phone.phone))


    # To get the rest of the phone number that not taken by anyone...
    not_taken_phones = list(set(all_phones_lst) - set(phone_taken_lst))


    not_taken_phones_to_show_to_users = []
    for phone in not_taken_phones:
        not_taken_phones_to_show_to_users.append((str(phone), str(phone)))


    phones_tuple = tuple(not_taken_phones_to_show_to_users)

    return phones_tuple




class PhoneUpdate(forms.Form):

    phones_tuple = phones_func()
    
    new_phone = forms.MultipleChoiceField(
        label = '..اختر أرقامك',  
        choices = phones_tuple,
        widget = forms.CheckboxSelectMultiple()) 









# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        # Call the parent class's clean method
        cleaned_data = super().clean()

        # Add custom validation logic if needed
        if 'username' in cleaned_data and 'password' in cleaned_data:
            username = cleaned_data['username']
            password = cleaned_data['password']
            # Add custom validation here if needed
            # For example, check if the username and password meet certain criteria

        return cleaned_data
