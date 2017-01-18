from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.forms import ModelForm
from students.models import SMSVerification, Student

class SMSVerification(ModelForm):
    name = forms.CharField(label="Name", 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'Name'}))
    mobile_number = forms.IntegerField(label="Mobile", 
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'mobile_number'}))
    # class Meta:
    #   model = Mobile
    #   fields = ('name','mobile_number')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Name", 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'Name'}))
    password = forms.CharField(label="PIN", 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'PIN'}))
    # class Meta:
    #   model = Student
    #   fields = ('name', 'pin')
class addClassForm(ModelForm):
    class_name = forms.CharField(label="Class",  
                               widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'Class Name'}))
    # class Meta:
    #   model = Student
    #   fields = ('class_name',)