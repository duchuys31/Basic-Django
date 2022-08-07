from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class Regisform(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=50)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput)

    def clean_password2(self):
        if 'password' in self.cleaned_data:
            pass1 = self.cleaned_data['password']
            pass2 = self.cleaned_data['password2']
            if pass1 == pass2 and pass1:
                return pass2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Tên tài khoản có kí tự đặc biệt')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Tài khoản đã tồn tại')

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['email'])
