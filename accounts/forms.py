from django import forms
from django.contrib.auth.forms import UserChangeForm
from allauth.account.forms import SignupForm, PasswordField
from django.contrib.auth import get_user_model
from allauth.account import app_settings


class MyCustomSignupForm(SignupForm):
    username = forms.CharField(
        max_length=8,
        label='이름',
        error_messages= {
            'max_length': '(주의) 닉네임은 최대 8글자입니다.',
        },
        widget=forms.TextInput(
            attrs={
                'class':'account_form_control',
            }
        )
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class':'account_form_control',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'] = PasswordField(
            label='비밀번호',
            autocomplete='new-password',
        )
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'account_form_control'
            }
        )
        if app_settings.SIGNUP_PASSWORD_ENTER_TWICE:
            self.fields['password2'] = PasswordField(
                label= '비밀번호 확인',
            )
            self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'account_form_control'
            }
        )
        

class CustomUserChangeForm(UserChangeForm):
    password = None
    username = forms.CharField(
        max_length=8,
        error_messages= {
            'max_length': '(주의) 닉네임은 최대 8글자입니다.',
        },
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'image',)