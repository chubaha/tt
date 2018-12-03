from django import forms
from empoyees.models import Employees


class LoginForm(forms.Form):
    username_auth = forms.CharField(max_length=14, label='Имя пользователя')
    password_auth = forms.CharField(max_length=14, widget=forms.PasswordInput, label='Пароль')

class EditForm(forms.ModelForm):
    date_begin = forms.CharField(label='Дата приема на работу', widget=forms.TextInput(attrs={'class' : 'form-control', 'type' : "date"}))
    class Meta:
        model = Employees
        fields = ['name', 'position','date_begin','salary','parent','photo']

class CreateForm(forms.ModelForm):
    date_begin = forms.CharField(label='Дата приема на работу', widget=forms.TextInput(attrs={'class' : 'form-control', 'type' : "date"}))
    class Meta:
        model = Employees
        fields = ['name', 'position','date_begin','salary','parent', 'photo']