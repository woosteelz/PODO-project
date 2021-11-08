from django import forms
from allauth.account.forms import SignupForm, PasswordField, LoginForm
from allauth.account import app_settings


class MyCustomSignupForm(SignupForm):
    username = forms.CharField(
        label='이름',
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
        