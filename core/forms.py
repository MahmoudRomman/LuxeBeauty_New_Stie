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



    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={
        'class': 'form-control',
        'label_suffix': "Image",
        'style': 'border-color:wightblack; border-radius: 10px; height: 45px;'

    }))


    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل السعر",
        'min' : '50',
        'max' : '15000',
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))

    
    discount_price = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل سعر الخصم ان وُجد",
        'default' :  '0.00',
        'min' : '10',
        'style': 'border-color:wightblack; border-radius: 10px;'

        }))
    

    quantity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'min' : '1',
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
            'placeholder': "ادخل قيمة رابط الدفع",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))


        SAR_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "رابط الدفع بالريال السعودى",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))


        AED_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "رابط الدفع بالرهك الاماراتى",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))

        USD_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "رابط الدفع بالدولار الامريكى",
            'style': 'border-color:wightblack; border-radius: 10px;',

        }))



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
            'name' : 'seller_phone_number',
        }))



        self.fields["country"] = CountryField(blank_label="(اختر الدولة)").formfield(
            widget=CountrySelectWidget(attrs={
                'class': 'form-control',
                'name' : 'country',
                'type' : 'radio',
                'style': 'border-color:wightblack; border-radius: 15px;',
                'name' : 'country',
                }))
    
        self.fields["address"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل العنوان",
            'style': 'border-color:wightblack; border-radius: 15px;',
            'name' : 'address',

        }))



        self.fields["customer_phone"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'size': "31",
            'placeholder': "ادخل رقم هاتف العميل",
            'style': 'border-color:wightblack; border-radius: 15px;',
            'name' : 'customer_phone',
        }))




        self.fields["customer_name"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل اسم العميل ثلاثى",
            'style': 'border-color:wightblack; border-radius: 15px;',
            'name' : 'customer_name',
        }))

        self.fields["payment_method"] = forms.ChoiceField(
            choices = models.payment_method,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'style': 'border-color:wightblack; border-radius: 15px;',
            'name' : 'payment_method',
        }))

        self.fields["selling_price"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخل سعر البيع للقطعة الواحدة بالريال السعودى",
            'min' : '0',
            'max' : '15000',
            'style': 'border-color:wightblack; border-radius: 15px;',
            'name' : 'selling_price',
            }))





class SellerBillFiter(forms.Form):
    bill_search = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "500",
        'placeholder': "البحث عن فاتورة",
        'style': 'border-color:wightblack; border-radius: 15px;',
    }))




class ItemRefundForm(forms.Form):
    # slug_code = forms.CharField(required=True, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'type' : 'text',
    #     'size': "18",
    #     'placeholder': "البحث عن فاتورة",
    #     'style': 'border-color:wightblack; border-radius: 15px;',
    # }))

    pieces_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'min' : '0',
        'placeholder': "ادخل الكمية المراد استرجاعها بشرط ألا تزيد عن عدد القطع المُباعة" ,
        'style': 'border-color:wightblack; border-radius: 15px;',
        }))






import datetime


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
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'seller_phone_number',         
        }))



        self.fields["country"] = CountryField(blank_label="(اختر الدولة)").formfield(
            widget=CountrySelectWidget(attrs={
                'class': 'form-control',
                'name' : 'country',
                'type' : 'radio',
                'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
                'name' : 'country',         

                }))
    
        self.fields["address"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل العنوان",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'address',         

        }))



        self.fields["customer_phone"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'size': "31",
            'placeholder': "ادخل رقم هاتف العميل",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'customer_phone',      
        }))




        self.fields["customer_name"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل اسم العميل ثلاثى",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'customer_name',         

        }))


        self.fields["wig_name"] = forms.ChoiceField(
        choices=models.wig_name,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "اسم الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        'name' : 'wig_name',         
        }))


        self.fields["wig_type"] = forms.ChoiceField(
            choices=models.wig_type,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'placeholder': "نوع الباروكة",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'wig_type',         
        }))



        self.fields["wig_long"] = forms.ChoiceField(
            choices=models.wig_long,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'placeholder': "طول الباروكة",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'wig_long',         
        }))



        self.fields["scalp_type"] = forms.ChoiceField(
            choices=models.scalp_type,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'placeholder': "نوع الفروة",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'scalp_type',         
        }))



        self.fields["wig_color"] = forms.ChoiceField(
            choices=models.wig_color,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'wig_color',         
        }))


        self.fields["density"] = forms.ChoiceField(
            choices=models.density,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'label' : 'select one',
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'density',         
        }))



        self.fields["price"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخل السعر",
            'min' : '500',
            'max' : '7000',
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'price',         
            }))


        self.fields["pieces_num"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخل الكمية",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'pieces_num',         
            }))
        
        self.fields["payment_method"] = forms.ChoiceField(
            choices = models.payment_method,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'payment_method',         
        }))
    

        self.fields["selling_price"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخل سعر البيع للقطعة الواحدة بالريال السعودى",
            'min' : '0',
            'max' : '7000',
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
            'name' : 'selling_price',         
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
        'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))
    

class EditPhoneForm(forms.ModelForm):

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'required' : True,
        'placeholder' : 'أدخل رقم الهاتف شامل مفتاح الدولة...',
        'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))


    class Meta:
         model = models.Phones
         fields = ['phone']


class AddPhoneNumberForUsersForm(forms.Form):

    def __init__(self, current_user, *args, **kwargs):
        super(AddPhoneNumberForUsersForm, self).__init__(*args, **kwargs)

        # Exclude the current user from the queryset
        # self.fields['name'].queryset = User.objects.exclude(id=current_user.id)



        # users = User.objects.exclude(id=current_user.id)
        # users = User.objects.exclude(is_staff=True)


        # self.fields['name'].queryset = users.filter(user_permissions__codename='can_make_order')

    name = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        empty_label="اختر أحد المستخدمين ...", 
        widget=forms.Select(attrs={
        'class': 'form-control',
        'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))
    
        
    
    phone = forms.ModelMultipleChoiceField(
        queryset = models.Phones.objects.all(), 
        widget = forms.CheckboxSelectMultiple
    )



    
# The following two forms is used to edit the phones for the different users 
    
# 1- This one is used to show the phones that the user take
class EditPhoneNumberForUsersForm(forms.ModelForm):

    
    phone = forms.ModelMultipleChoiceField(
        queryset = models.Phones.objects.all(), 
        widget = forms.CheckboxSelectMultiple
    )

    class Meta:
         model = models.PhoneNumberr
         fields = ['phone',]

# 2- And this one is used to make the actual updates
class ActualEditPhoneNumberForUsersForm(forms.Form):

    
    phone = forms.ModelMultipleChoiceField(
        queryset = models.Phones.objects.all(), 
        widget = forms.CheckboxSelectMultiple
    )




class CreateAccountForm(forms.Form):

    def __init__(self, current_user, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)

        # Exclude the current user from the queryset
        # self.fields['marketer'].queryset = User.objects.exclude(id=current_user.id)
        # self.fields['seller'].queryset = User.objects.exclude(id=current_user.id)

    marketer = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        empty_label="اختر اسم المُسوق ...", 
        widget=forms.Select(attrs={
        'class': 'form-control',
        'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))
    
    seller = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        empty_label="اختر اسم البائع ...", 
        widget=forms.Select(attrs={
        'class': 'form-control',
        'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))
    
    
    phone = forms.ModelChoiceField(
        queryset = models.Phones.objects.all(),
        empty_label="اختر أحد أرقام الهواتف  ...", 
        widget=forms.Select(attrs={
        'class': 'form-control',
        'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))



    account_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل اسم الحساب",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))

    tiktok_account_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "ادخل رابط حساب التيك توك",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))
    
    instagram_account_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "ادخل رابط حساب الانستجرام",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))



class EditAccountForm(forms.ModelForm):
    account_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل اسم الحساب",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))

    tiktok_account_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "ادخل رابط حساب التيك توك",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))
    
    instagram_account_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "ادخل رابط حساب الانستجرام",
            'style': 'border-color:wightblack; border-radius: 10px; height:50px',  
        }))
    
    class Meta:
        model = models.Account
        fields = ['account_name', 'tiktok_account_link', 'instagram_account_link']






from django import forms
from django.core.validators import MinValueValidator

class DateInput(forms.DateInput):
    input_type = 'month'


class BankAccountForm(forms.ModelForm):
    country = CountryField(blank_label="Choose a country").formfield(
            widget=CountrySelectWidget(attrs={
                'class': 'form-control',
                'name' : 'country',
                'type' : 'radio',
                'style': 'border-color:wightblack; border-radius: 15px;'
                }))
    class Meta:
        model = models.BankAccount
        # fields = ['bank_name', 'country', 'IBAN', 'account_number', 'swift_code', 'beneficiary_name', 'card_number', 'validation_date', 'ccv_or_cvc']
        fields = ['bank_name', 'country', 'IBAN', 'account_number', 'swift_code', 'beneficiary_name']
        labels = {
            'bank_name' : "Bank Name",
            'country' : "Choose Country",
            'IBAN' : "IBAN",
            'account_number' : "Account Number",
            'swift_code' : "Swift Code",
            'beneficiary_name' : "Beneficiary Name",

        }



        widgets = {
            'bank_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'style': 'border-color:wightblack; border-radius: 15px;',
                'placeholder': 'Enter Bank Name',
                }),


            'IBAN': forms.TextInput(attrs={
                'class': 'form-control', 
                'style': 'border-color:wightblack; border-radius: 15px;',
                'placeholder': 'Enter IBAN',
                }),


            'account_number': forms.TextInput(attrs={
                'class': 'form-control', 
                'style': 'border-color:wightblack; border-radius: 15px;',
                'placeholder': 'Enter Account Number',
                }),


            'swift_code': forms.TextInput(attrs={
                'class': 'form-control', 
                'style': 'border-color:wightblack; border-radius: 15px;',
                'placeholder': 'Enter Swift Code',
                }),


            'beneficiary_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'style': 'border-color:wightblack; border-radius: 15px;',
                'placeholder': 'Enter Beneficiary Name',
                }),
        }






    
    




class EditBill(forms.ModelForm):
    class Meta:
        model = models.Bill2
        fields = '__all__'
        
    def __init__(self, current_user, *args, **kwargs):
        super(EditBill, self).__init__(*args, **kwargs)


        # Query phone numbers for the current user
        user_phone_numbers = models.PhoneNumberr.objects.filter(user=current_user)
        # Create phones choices based on the user phones
        phone_number_choices = []
        phone_number_choices.append((str("ادخل رقم هاتف العمل الخاص بك"), str("ادخل رقم هاتف العمل الخاص بك")))
        for phone_number in user_phone_numbers:
            # phone_number_choices.append((str(phone_number.phone), str(phone_number.phone)))   
            phone_number_choices.append((str(phone_number.phone), str(phone_number.phone)))   

              



        self.fields["seller_phone_number"] = forms.ChoiceField(
            choices = phone_number_choices,
            required = True,
            widget = forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'seller_phone_number',         
        }))



        self.fields["country"] = CountryField(blank_label="(اختر الدولة)").formfield(
            widget=CountrySelectWidget(attrs={
                'class': 'form-control',
                'name' : 'country',
                'type' : 'radio',
                'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
                'name' : 'country',         
        }))
        
    
        self.fields["address"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل العنوان",
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'address',         
        }))


        self.fields["customer_phone"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'size': "31",
            'placeholder': "ادخل رقم هاتف العميل",
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'customer_phone',      
        }))


        self.fields["customer_name"] = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type' : 'text',
            'size': "200",
            'placeholder': "ادخل اسم العميل ثلاثى",
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'customer_name',         
        }))


        self.fields["wig_name"] = forms.ChoiceField(
        choices=models.wig_name,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "اسم الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
        'name' : 'wig_name',         
        }))


        self.fields["wig_type"] = forms.ChoiceField(
            choices=models.wig_type,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'placeholder': "نوع الباروكة",
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'wig_type',         
        }))


        self.fields["wig_long"] = forms.ChoiceField(
            choices=models.wig_long,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'placeholder': "طول الباروكة",
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'wig_long',         
        }))



        self.fields["scalp_type"] = forms.ChoiceField(
            choices=models.scalp_type,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'placeholder': "نوع الفروة",
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'scalp_type',         
        }))



        self.fields["wig_color"] = forms.ChoiceField(
            choices=models.wig_color,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'wig_color',         
        }))


        self.fields["density"] = forms.ChoiceField(
            choices=models.density,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'label' : 'select one',
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'density',         
        }))



        self.fields["price"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخل السعر",
            'min' : '500',
            'max' : '7000',
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'price',         
            }))


        self.fields["pieces_num"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخل الكمية",
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'pieces_num',         
        }))
        
        self.fields["payment_method"] = forms.ChoiceField(
            choices = models.payment_method,
            required=True,
            widget=forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'payment_method',         
        }))
    

        self.fields["selling_price"] = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type' : 'number',
            'placeholder': "ادخل سعر البيع للقطعة الواحدة بالريال السعودى",
            'min' : '0',
            'max' : '7000',
            'style': 'border-color:wightblack; border-radius: 10px; height: 50PX',
            'name' : 'selling_price',         
        }))


