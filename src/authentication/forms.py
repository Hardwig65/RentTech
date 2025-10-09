from django.core.exceptions import ValidationError
from django.forms import Form
from django import forms

from authentication.models import CustomUser


class RegisterForm(Form):
    username = forms.CharField(
        max_length = 20,
        label = "Username",
        widget=forms.TextInput(attrs={"placeholder": "Введите имя пользователя"})
    )
    password = forms.CharField(
        label = 'Password',
        widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"})
    )
    confirm_password = forms.CharField(
        label = 'Confirm Password',
        widget=forms.PasswordInput(attrs={"placeholder": "Подтвердите пароль"})
    )

    # Проверяем не существует ли уже такой юзер
    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')
        return username

    #Проверка на совпадение паролей
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('Пароли не совпадают.')
        return cleaned_data






class LoginForm(Form):
    username = forms.CharField(
        max_length = 20,
        label = "Username",
        widget=forms.TextInput(attrs={"placeholder": "Введите имя пользователя"})
    )
    password = forms.CharField(
        label = 'Password',
        widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"}))
