from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from .models import *




class SignupForm(forms.ModelForm):
    user_id = forms.CharField(max_length = 30)
    email = forms.EmailField(max_length=200, help_text='required')
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length = 30)
    middle_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)
    phone_no = forms.CharField(max_length = 30 )

    class Meta:
        model = Customer
        fields = ('user_id', 'email', 'password', 'first_name','middle_name','last_name', 'phone_no')





class LoginForm(forms.Form):
    user_id = forms.CharField(max_length = 30)
    password = forms.CharField(widget=forms.PasswordInput())





class userChangePasswdForm(forms.Form):
    old_password = forms.CharField(widget = forms.PasswordInput(), max_length = 50)
    new_password = forms.CharField(widget = forms.PasswordInput(), max_length = 50)





class DateInputForm(forms.Form):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=True)




class TextInputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))




class StoreSignUp(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Book_store
        fields = ['store_name', 'email', 'password', 'website','phone_no', 'rating', 'address_line1', 'address_line2',
        'city', 'district', 'state', 'zip_code']




class StoreProfile(forms.Form):
    store_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), max_length = 100)
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    website = forms.CharField(max_length = 50)
    phone_no = forms.CharField(max_length = 10)
    rating = forms.IntegerField()
    address_line1 = forms.CharField(max_length = 100)
    address_line2 = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 50)
    district = forms.CharField(max_length = 50)
    state = forms.CharField(max_length = 50)
    zip_code = forms.CharField(max_length = 6)




class storeLoginForm(forms.Form):
    email = forms.CharField(max_length = 50)
    password = forms.CharField(widget=forms.PasswordInput())




class storeChangePasswdForm(forms.Form):
    old_password = forms.CharField(widget = forms.PasswordInput(), max_length = 50)
    new_password = forms.CharField(widget = forms.PasswordInput(), max_length = 50)




class bookAddForm(forms.Form):
    title = forms.CharField(max_length = 50)
    author = forms.CharField(max_length = 50)
    publisher = forms.CharField(max_length = 50)
    genre = forms.CharField(max_length = 20)
    year_of_publish = forms.IntegerField(min_value=1750)
    price = forms.IntegerField()
    no_of_books = forms.IntegerField()

