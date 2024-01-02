from collections.abc import Mapping
from django import forms
from . import models
from . import views
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.core.exceptions import ObjectDoesNotExist



class ItemForm(forms.Form):

    name = forms.ChoiceField(
        choices=models.wig_name,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "اسم الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))


    wig_type = forms.ChoiceField(
        choices=models.wig_type,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))



    wig_long = forms.ChoiceField(
        choices=models.wig_long,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "طول الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))



    scalp_type = forms.ChoiceField(
        choices=models.scalp_type,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الفروة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))



    wig_color = forms.ChoiceField(
        choices=models.wig_color,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'style': 'border-color:wightblack; border-radius: 10px;'


    }))


    density = forms.ChoiceField(
        choices=models.density,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'label' : 'select one',
        'style': 'border-color:wightblack; border-radius: 10px;'

        
    }))



    image = forms.ImageField(label_suffix="sdfsdf", widget=forms.FileInput(attrs={
        'class': 'form-control',
        'label_suffix': "Image",
        'style': 'border-color:wightblack; border-radius: 10px; height: 45px;'

    }))


    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل السعر",
        'min' : '400',
        'max' : '7000',
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))

    
    discount_price = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل سعر الخصم",
        'default' :  '0.00',
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))
    

    quantity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل الكمية",
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))
    



class EditItemForm(forms.ModelForm):

    name = forms.ChoiceField(
        choices=models.wig_name,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "اسم الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))


    wig_type = forms.ChoiceField(
        choices=models.wig_type,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))



    wig_long = forms.ChoiceField(
        choices=models.wig_long,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "طول الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))



    scalp_type = forms.ChoiceField(
        choices=models.scalp_type,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الفروة",
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))



    wig_color = forms.ChoiceField(
        choices=models.wig_color,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'style': 'border-color:wightblack; border-radius: 10px;'

    }))


    density = forms.ChoiceField(
        choices=models.density,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'label' : 'select one',
        'style': 'border-color:wightblack; border-radius: 10px;'
        
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class" : "input",
        "type" : "file",
        'style': 'display: none;',
        'id' : 'image-input',
        'name' : 'profile_image',
        'accept' : 'image/*',
        }))



    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل السعر",
        'min' : '400',
        'max' : '7000',
        'style': 'border-color:wightblack; border-radius: 10px;'
        }))
    
    discount_price = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل سعر الخصم",
        'default' :  '0.00',
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))
    

    quantity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل الكمية",
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))
    

    class Meta:
         model = models.Item
         fields = ['name', 'wig_type', 'wig_long', 'scalp_type', 'wig_color', 'density', 'image', 'price', 'discount_price', 'quantity']




class AddLinkForm(forms.Form):
        link_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "150",
        'placeholder': "Stripe اسم لينك الدفع, مثال",
        'style': 'border-color:wightblack; border-radius: 10px;',

        }))

        amount = forms.IntegerField(widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخال مبلغ الدفع",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))


        SAR_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "رابط الدفع السعودى",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))


        AED_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "رابط الدفع الاماراتى",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))





# class BillForm2(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request')
#         super().__init__(*args, **kwargs)



#         self.fields["country"] = CountryField(blank_label="(اختر الدولة)").formfield(
#             widget=CountrySelectWidget(attrs={
#                 'class': 'form-control',
#                 'name' : 'country',
#                 'type' : 'radio',
#                 'style': 'border-color:wightblack; border-radius: 15px;'
#                 }))
        
#         self.fields["address"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'type' : 'text',
#             'size': "200",
#             'placeholder': "ادخل العنوان",
#             'style': 'border-color:wightblack; border-radius: 15px;'
#         }))


#         self.fields["customer_phone"].widget.attrs.update({
#             'class': 'form-control',
#             'size': "31",
#             'placeholder': "ادخل رقم هاتف العميل",
#             'style': 'border-color:wightblack; border-radius: 15px;',
#         })



#         self.fields["customer_name"].widget.attrs.update({
#             'class': 'form-control',
#             'size': "200",
#             'placeholder': "ادخل اسم العميل ثلاثى",
#             'style': 'border-color:wightblack; border-radius: 15px;',
#         })



        

#         if self.request.user.is_authenticated:
#             # data = models.PhoneNumber.objects.filter(user=self.request.user)
#             data = models.PhoneNumberr.objects.filter(user=self.request.user)

            
                
#             choices_list = []
#             choices_list.append(("ادخل رقم هاتف العمل الخاص بك", "ادخل رقم هاتف العمل الخاص بك"))

#             for c in data:
#                 choices_list.append((str(c), str(c)))

#             choices_tuple = tuple(choices_list)
#         else:
#             choices_tuple = {}

             
#         self.fields["seller_phone_number"] = forms.ChoiceField(
#             # choices = choices_tuple,
#             queryset = models.PhoneNumberr.objects.filter(user=self.request.user),

#             required = True,
#             widget = forms.Select(attrs={
#             'class': 'form-control',
#             'type' : 'radio',
#             'style': 'border-color:wightblack; border-radius: 15px;',            
#         }))





    
#     class Meta:
#          model = models.Bill2
#          fields = ['seller', 'country', 'address', 'customer_phone', 'customer_name', 'seller_phone_number']















class BillForm2(forms.Form):
    def __init__(self, current_user, *args, **kwargs):
        super(BillForm2, self).__init__(*args, **kwargs)


        # Query phone numbers for the current user
        user_phone_numbers = models.PhoneNumberr.objects.filter(user=current_user)

        # Create choices for the form based on user phone numbers


        phone_number_choices = []
        phone_number_choices.append((str("ادخل رقم هاتف العمل الخاص بك"), str("ادخل رقم هاتف العمل الخاص بك")))
        for phone_number in user_phone_numbers:
            phone_number_choices.append((phone_number.id, str(phone_number.phone)))     
        # phone_number_choices = [(phone_number.id, str(phone_number.phone)) for phone_number in user_phone_numbers]





        self.fields["seller_phone_number"] = forms.ChoiceField(
            choices = phone_number_choices,
            required = True,
            widget = forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'style': 'border-color:wightblack; border-radius: 15px;',            
        }))



        self.fields["country"] = CountryField(blank_label="(اختر الدولة)").formfield(
            widget=CountrySelectWidget(attrs={
                'class': 'form-control',
                'name' : 'country',
                'type' : 'radio',
                'style': 'border-color:wightblack; border-radius: 15px;'
                }))
    
        self.fields["address"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل العنوان",
            'style': 'border-color:wightblack; border-radius: 15px;'
        }))



        self.fields["customer_phone"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'size': "31",
            'placeholder': "ادخل رقم هاتف العميل",
            'style': 'border-color:wightblack; border-radius: 15px;',
        }))




        self.fields["customer_name"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل اسم العميل ثلاثى",
            'style': 'border-color:wightblack; border-radius: 15px;',
        }))










import datetime


# today = datetime.date.today()
# year = today.year
# month = today.month
# today_in_month = int(today.day)
# list_of_days = []
# list_of_days.append((str("كل الايام"), str("كل الايام")))


# for i in range(1, (today_in_month + 1)):
#     # list_of_days.append(i)
#     list_of_days.append((str(i), str(i)))
# list_of_days = tuple(list_of_days)





class BillFilterForAdmin(forms.Form):
    

    # Add other form fields as needed

    def __init__(self, *args, **kwargs):
        super(BillFilterForAdmin, self).__init__(*args, **kwargs)


    date_choices = []
    date_choices.append((str("كل الايام"), str("كل الايام")))


    for day in range(1, datetime.date.today().day + 1):
        date_choices.append((day, f'{day} - {datetime.date.today().strftime("%B")}'))


    today_day = forms.ChoiceField(
        # choices=list_of_days,
        choices = date_choices,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'label' : 'select one',
        'style': 'border-color:wightblack; border-radius: 10px;',            

        
    }))







# all_users = User.objects.all()

# users_list = []
# for c in all_users:
#     users_list.append((str(c), str(c)))

# users_tuple = tuple(users_list)




class PenalityForm(forms.Form):


    def __init__(self, current_user, *args, **kwargs):
        super(PenalityForm, self).__init__(*args, **kwargs)

        # Exclude the current user from the queryset
        self.fields['name'].queryset = User.objects.exclude(id=current_user.id)



    name = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        # queryset=User.objects.exclude(id=current_user.id), 

        empty_label="اختر أحد المستخدمين ...", 
        widget=forms.Select(attrs={
        'class': 'form-control',
        'style': 'border-color:wightblack; border-radius: 10px;',  
            }))


    message = forms.CharField(widget=forms.Textarea(attrs={
    'class' : 'form-control',
    'required' : True,
    'cols' : 6,
    'placeholder' : 'اكتب هنا نص الخَصم الذى تريد...',
    'style': 'border-color:wightblack; border-radius: 10px;',  
    }))

    days_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
    'class': 'form-control',
    'type' : 'number',
    'placeholder': "ادخل عدد أيام الخصم",
    'min' : '0',
    'max' : '31',
    'style': 'border-color:wightblack; border-radius: 10px;'

    }))



class RewardForm(forms.Form):

    def __init__(self, current_user, *args, **kwargs):
        super(RewardForm, self).__init__(*args, **kwargs)

        # Exclude the current user from the queryset
        self.fields['name'].queryset = User.objects.exclude(id=current_user.id)

    name = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        empty_label="اختر أحد المستخدمين ...", 
        widget=forms.Select(attrs={
        'class': 'form-control',
        'style': 'border-color:wightblack; border-radius: 10px;',  
            }))


    message = forms.CharField(widget=forms.Textarea(attrs={
    'class' : 'form-control',
    'required' : True,
    'cols' : 6,
    'placeholder' : 'اكتب هنا نص المكافأة الذى تريد...',
    'style': 'border-color:wightblack; border-radius: 10px;',  
    }))

    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
    'class': 'form-control',
    'type' : 'number',
    'placeholder': "ادخل قيمة المكافأة",
    'min' : '50',
    'max' : '5000',
    'style': 'border-color:wightblack; border-radius: 10px;'
    }))



class TaskForm(forms.Form):

    def __init__(self, current_user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        # Exclude the current user from the queryset
        self.fields['name'].queryset = User.objects.exclude(id=current_user.id)

    name = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        empty_label="اختر أحد المستخدمين ...", 
        widget=forms.Select(attrs={
        'class': 'form-control',
        'style': 'border-color:wightblack; border-radius: 10px;',  
            }))
    
        
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'required' : True,
        'cols' : 6,
        'placeholder' : 'اكتب هنا نص المهمة الذى تريد...',
        'style': 'border-color:wightblack; border-radius: 10px;',  
        }))







# class OnlineOrder(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request')
#         super().__init__(*args, **kwargs)



#         self.fields["country"] = CountryField(blank_label="(اختر الدولة)").formfield(
#             widget=CountrySelectWidget(attrs={
#                 'class': 'form-control',
#                 'name' : 'country',
#                 'type' : 'radio',
#                 'style': 'border-color:wightblack; border-radius: 15px;'
#                 }))
        
#         self.fields["address"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'type' : 'text',
#             'size': "200",
#             'placeholder': "ادخل العنوان",
#             'style': 'border-color:wightblack; border-radius: 15px;'
#         }))


#         self.fields["customer_phone"].widget.attrs.update({
#             'class': 'form-control',
#             'size': "31",
#             'placeholder': "ادخل رقم هاتف العميل",
#             'style': 'border-color:wightblack; border-radius: 15px;',
#         })



#         self.fields["customer_name"].widget.attrs.update({
#             'class': 'form-control',
#             'size': "200",
#             'placeholder': "ادخل اسم العميل ثلاثى",
#             'style': 'border-color:wightblack; border-radius: 15px;',
#         })

        


#         if self.request.user.is_authenticated:
        
#             data = models.PhoneNumber.objects.filter(user=self.request.user)
            
                
#             choices_list = []
#             choices_list.append(("ادخل رقم هاتف العمل الخاص بك", "ادخل رقم هاتف العمل الخاص بك"))

#             for c in data:
#                 choices_list.append((str(c), str(c)))

#             choices_tuple = tuple(choices_list)
#         else:
#             choices_tuple = {}



             
#         self.fields["seller_phone_number"] = forms.ChoiceField(
#             choices = choices_tuple,
#             required = True,
#             widget = forms.Select(attrs={
#             'class': 'form-control',
#             'type' : 'radio',
#             'label' : 'select one',
#             'style': 'border-color:wightblack; border-radius: 15px;',            
#         }))

#     # Fields for the item to be saved in the database in its controller --> view

#         self.fields["wig_name"] = forms.ChoiceField(
#         choices=models.wig_name,
#         widget=forms.Select(attrs={
#         'class': 'form-control',
#         'type' : 'radio',
#         'placeholder': "اسم الباروكة",
#         'style': 'border-color:wightblack; border-radius: 10px;'
#         }))


#         self.fields["wig_type"] = forms.ChoiceField(
#             choices=models.wig_type,
#             widget=forms.Select(attrs={
#             'class': 'form-control',
#             'type' : 'radio',
#             'placeholder': "نوع الباروكة",
#             'style': 'border-color:wightblack; border-radius: 10px;'

#         }))



#         self.fields["wig_long"] = forms.ChoiceField(
#             choices=models.wig_long,
#             widget=forms.Select(attrs={
#             'class': 'form-control',
#             'type' : 'radio',
#             'placeholder': "طول الباروكة",
#             'style': 'border-color:wightblack; border-radius: 10px;'

#         }))



#         self.fields["scalp_type"] = forms.ChoiceField(
#             choices=models.scalp_type,
#             required=True,
#             widget=forms.Select(attrs={
#             'class': 'form-control',
#             'type' : 'radio',
#             'placeholder': "نوع الفروة",
#             'style': 'border-color:wightblack; border-radius: 10px;'

#         }))



#         self.fields["wig_color"] = forms.ChoiceField(
#             choices=models.wig_color,
#             required=True,
#             widget=forms.Select(attrs={
#             'class': 'form-control',
#             'type' : 'radio',
#             'style': 'border-color:wightblack; border-radius: 10px;'


#         }))


#         self.fields["density"] = forms.ChoiceField(
#             choices=models.density,
#             required=True,
#             widget=forms.Select(attrs={
#             'class': 'form-control',
#             'type' : 'radio',
#             'label' : 'select one',
#             'style': 'border-color:wightblack; border-radius: 10px;'

            
#         }))



#         self.fields["price"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'type' : 'number',
#             'placeholder': "ادخل السعر",
#             'min' : '500',
#             'max' : '7000',
#             'style': 'border-color:wightblack; border-radius: 10px;'

#             }))


#         self.fields["pieces_num"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'type' : 'number',
#             'placeholder': "ادخل الكمية",
#             'style': 'border-color:wightblack; border-radius: 10px;'

#             }))


#     class Meta:
#          model = models.Bill2
#          fields = ['seller', 'country', 'address', 'customer_phone', 'customer_name', 'seller_phone_number',
#                    'wig_type', 'wig_long', 'scalp_type', 'wig_color', 'density', 'price', 'pieces_num']
         








class OnlineOrder(forms.Form):

    def __init__(self, current_user, *args, **kwargs):
        super(OnlineOrder, self).__init__(*args, **kwargs)


        # Query phone numbers for the current user
        if current_user.is_authenticated:
            user_phone_numbers = models.PhoneNumberr.objects.filter(user=current_user)

            # Create choices for the form based on user phone numbers


            phone_number_choices = []
            phone_number_choices.append((str("ادخل رقم هاتف العمل الخاص بك"), str("ادخل رقم هاتف العمل الخاص بك")))
            for phone_number in user_phone_numbers:
                phone_number_choices.append((phone_number.id, str(phone_number.phone)))   
        else:
            phone_number_choices = []              





        self.fields["seller_phone_number"] = forms.ChoiceField(
            choices = phone_number_choices,
            required = True,
            widget = forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'style': 'border-color:wightblack; border-radius: 15px;',            
        }))



        self.fields["country"] = CountryField(blank_label="(اختر الدولة)").formfield(
            widget=CountrySelectWidget(attrs={
                'class': 'form-control',
                'name' : 'country',
                'type' : 'radio',
                'style': 'border-color:wightblack; border-radius: 15px;'
                }))
    
        self.fields["address"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل العنوان",
            'style': 'border-color:wightblack; border-radius: 15px;'
        }))



        self.fields["customer_phone"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'size': "31",
            'placeholder': "ادخل رقم هاتف العميل",
            'style': 'border-color:wightblack; border-radius: 15px;',
        }))




        self.fields["customer_name"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل اسم العميل ثلاثى",
            'style': 'border-color:wightblack; border-radius: 15px;',
        }))


        self.fields["wig_name"] = forms.ChoiceField(
        choices=models.wig_name,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "اسم الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'
        }))


        self.fields["wig_type"] = forms.ChoiceField(
            choices=models.wig_type,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'placeholder': "نوع الباروكة",
            'style': 'border-color:wightblack; border-radius: 10px;'

        }))



        self.fields["wig_long"] = forms.ChoiceField(
            choices=models.wig_long,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'placeholder': "طول الباروكة",
            'style': 'border-color:wightblack; border-radius: 10px;'

        }))



        self.fields["scalp_type"] = forms.ChoiceField(
            choices=models.scalp_type,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'placeholder': "نوع الفروة",
            'style': 'border-color:wightblack; border-radius: 10px;'

        }))



        self.fields["wig_color"] = forms.ChoiceField(
            choices=models.wig_color,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'style': 'border-color:wightblack; border-radius: 10px;'


        }))


        self.fields["density"] = forms.ChoiceField(
            choices=models.density,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'label' : 'select one',
            'style': 'border-color:wightblack; border-radius: 10px;'

            
        }))



        self.fields["price"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخل السعر",
            'min' : '500',
            'max' : '7000',
            'style': 'border-color:wightblack; border-radius: 10px;'

            }))


        self.fields["pieces_num"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخل الكمية",
            'style': 'border-color:wightblack; border-radius: 10px;'

            }))










class LinkValueFilterForm(forms.Form):
    value = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل قيمة الرابط",
        'min' : '10',
        'max' : '7000',
        'style': 'border-color:wightblack; border-radius: 10px;'
        }))






class AddPhoneForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'required' : True,
        'placeholder' : 'أدخل رقم الهاتف شامل مفتاح الدولة...',
        'style': 'border-color:wightblack; border-radius: 10px;',  
        }))
    

class EditPhoneForm(forms.ModelForm):

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'required' : True,
        'placeholder' : 'أدخل رقم الهاتف شامل مفتاح الدولة...',
        'style': 'border-color:wightblack; border-radius: 10px;',  
        }))


    class Meta:
         model = models.Phones
         fields = ['phone']


class AddPhoneNumberForUsersForm(forms.Form):

    def __init__(self, current_user, *args, **kwargs):
        super(AddPhoneNumberForUsersForm, self).__init__(*args, **kwargs)

        # Exclude the current user from the queryset
        self.fields['name'].queryset = User.objects.exclude(id=current_user.id)

    name = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        empty_label="اختر أحد المستخدمين ...", 
        widget=forms.Select(attrs={
        'class': 'form-control',
        'style': 'border-color:wightblack; border-radius: 10px;',  
            }))
    
        
    
    phone = forms.ModelMultipleChoiceField(
        queryset = models.Phones.objects.all(), 
        widget = forms.CheckboxSelectMultiple
    )



    
class EditPhoneNumberForUsersForm(forms.ModelForm):

    
    phone = forms.ModelMultipleChoiceField(
        queryset = models.Phones.objects.all(), 
        widget = forms.CheckboxSelectMultiple
    )

    class Meta:
         model = models.Phones
         fields = ['phone',]






















