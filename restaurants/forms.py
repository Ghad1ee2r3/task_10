from django import forms
from .models import Restaurant
from .models import Item
from django.contrib.auth.models import User

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        #exclude=['owner',]

        fields = ["name", "description" , "opening_time" , "closing_time", "logo"]
        # '__all__'
        #["name", "description" , "opening_time" , "closing_time", "logo"] '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        #exclude=['restaurant',]
        fields = ["name","description", "price" ]
       #'__all__'

        #widgets = {
        #	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        #	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        #}


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
