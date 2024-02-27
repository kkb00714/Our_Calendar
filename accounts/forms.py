from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Register(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='유효한 이메일 주소를 입력해 주세요.')
    nickname = forms.CharField(max_length=10, help_text='유효한 닉네임을 입력해 주세요.')
    phone = forms.CharField(max_length=11, required=False, help_text='선택 사항입니다.')
    address = forms.CharField(max_length=255, required=False, help_text='선택 사항입니다.')
    birthday = forms.DateField(required=False, help_text='선택 사항입니다.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'nickname', 'phone', 'address', 'birthday')
        