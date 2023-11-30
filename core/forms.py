from collections.abc import Mapping
from django import forms
from . import models
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class ItemForm(forms.Form):

    name = forms.ChoiceField(
        choices=models.wig_name,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "اسم الباروكة",
        'style': 'border-color:wightblack; border-radius: 10px;'

#         width: 100%;
#   padding:10px;
#   border-radius:10px;

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



    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل السعر",
        'min' : '500',
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
    }))


    wig_type = forms.ChoiceField(
        choices=models.wig_type,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الباروكة",
    }))



    wig_long = forms.ChoiceField(
        choices=models.wig_long,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "طول الباروكة",
    }))



    scalp_type = forms.ChoiceField(
        choices=models.scalp_type,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "نوع الفروة",
    }))



    wig_color = forms.ChoiceField(
        choices=models.wig_color,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',

    }))


    density = forms.ChoiceField(
        choices=models.density,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'label' : 'select one',
        
    }))



    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل السعر",
        'min' : '500',
        'max' : '7000',
        }))
    
    discount_price = forms.FloatField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل سعر الخصم",
        'default' :  '0.00',
        }))
    

    quantity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "ادخل الكمية",
        }))
    

    class Meta:
         model = models.Item
         fields = ['name', 'wig_type', 'wig_long', 'scalp_type', 'wig_color', 'density', 'price', 'discount_price', 'quantity']




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





class BillForm2(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)



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


        self.fields["customer_phone"].widget.attrs.update({
            'class': 'form-control',
            'size': "31",
            'placeholder': "ادخل رقم هاتف العميل",
            'style': 'border-color:wightblack; border-radius: 15px;',
        })



        self.fields["customer_name"].widget.attrs.update({
            'class': 'form-control',
            'size': "200",
            'placeholder': "ادخل اسم العميل",
            'style': 'border-color:wightblack; border-radius: 15px;',
        })

        


        data = models.PhoneNumber.objects.filter(user=self.request.user)
        
             
        choices_list = []
        for c in data:
            choices_list.append((str(c), str(c)))

        choices_tuple = tuple(choices_list)

             
        self.fields["seller_phone_number"] = forms.ChoiceField(
            choices = choices_tuple,
            required = True,
            widget = forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'label' : 'select one',
            'style': 'border-color:wightblack; border-radius: 15px;',            
        }))



    class Meta:
         model = models.Bill2
         fields = ['seller', 'country', 'address', 'customer_phone', 'customer_name', 'seller_phone_number']





import datetime


today = datetime.date.today()
year = today.year
month = today.month
today_in_month = int(today.day)
list_of_days = []
list_of_days.append((str("كل الايام"), str("كل الايام")))


for i in range(1, (today_in_month + 1)):
    # list_of_days.append(i)
    list_of_days.append((str(i), str(i)))
list_of_days = tuple(list_of_days)





class BillFilterForAdmin(forms.Form):
    today_day = forms.ChoiceField(
        choices=list_of_days,
        required=True,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'label' : 'select one',
        'style': 'border-color:wightblack; border-radius: 10px;',            

        
    }))




all_users = User.objects.all()

users_list = []
for c in all_users:
    users_list.append((str(c), str(c)))

users_tuple = tuple(users_list)




# from ckeditor.widgets import CKEditorWidget

class PenalityForm(forms.Form):
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
    'placeholder' : 'اكتب هنا نص الخَصم الذى تريد...',
    'style': 'border-color:wightblack; border-radius: 10px;',  
    }))

    days = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
    'class': 'form-control',
    'type' : 'number',
    'placeholder': "ادخل عدد أيام الخصم",
    'style': 'border-color:wightblack; border-radius: 10px;'
    }))

    
    

class OnlineOrder(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)



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


        self.fields["customer_phone"].widget.attrs.update({
            'class': 'form-control',
            'size': "31",
            'placeholder': "ادخل رقم هاتف العميل",
            'style': 'border-color:wightblack; border-radius: 15px;',
        })



        self.fields["customer_name"].widget.attrs.update({
            'class': 'form-control',
            'size': "200",
            'placeholder': "ادخل اسم العميل",
            'style': 'border-color:wightblack; border-radius: 15px;',
        })

        


        data = models.PhoneNumber.objects.filter(user=self.request.user)
        
             
        choices_list = []
        for c in data:
            choices_list.append((str(c), str(c)))

        choices_tuple = tuple(choices_list)

             
        self.fields["seller_phone_number"] = forms.ChoiceField(
            choices = choices_tuple,
            required = True,
            widget = forms.Select(attrs={
            'class': 'form-control',
            'type' : 'radio',
            'label' : 'select one',
            'style': 'border-color:wightblack; border-radius: 15px;',            
        }))

    # Fields for the item to be saved in the database in its controller --> view

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


    class Meta:
         model = models.Bill2
         fields = ['seller', 'country', 'address', 'customer_phone', 'customer_name', 'seller_phone_number',
                   'wig_type', 'wig_long', 'scalp_type', 'wig_color', 'density', 'price', 'pieces_num']
         


































