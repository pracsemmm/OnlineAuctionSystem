from django import forms
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo,Product

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password','first_name','last_name')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('user_phone_no','user_age','type_of_user')

class ProductForm(forms.ModelForm):
    class Meta():
        model=Product
        exclude = ['add_time']
