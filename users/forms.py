from django import forms
from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm, ResetPasswordForm, ResetPasswordKeyForm
from ckeditor.fields import RichTextField
from phonenumber_field.formfields import PhoneNumberField
from .models import User


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'login-email-field',
            'placeholder': 'Email'
        })
        self.fields['login'].label = "Электронная почта"

        self.fields['password'].widget.attrs.update({
            'class': 'login-password-field'
        })


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'login-email-field',
            'placeholder': 'Email'
        })
        self.fields['email'].label = "Электронная почта"

        self.fields['password1'].widget.attrs.update({
            'class': 'login-password-field'
        })


class CustomChangePasswordForm(ChangePasswordForm):

    def __init__(self, *args, **kwargs):
        super(CustomChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['oldpassword'].widget.attrs.update({
            'class': 'login-email-field',
            'placeholder': 'Текущий пароль'
        })
        # self.fields['email'].label = "Электронная почта"
        #
        self.fields['password1'].widget.attrs.update({
            'class': 'login-password-field'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'login-password-field'
        })


class CustomResetPasswordForm(ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'login-email-field',
            'placeholder': 'Email'
        })
        self.fields['email'].label = "Электронная почта"


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):

    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordKeyForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'login-password-field'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'login-password-field'
        })


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "avatar",
        )


class UpdateGuideProfileForm(forms.ModelForm):
    class Meta:
        model = User
        bio = RichTextField()
        phone = PhoneNumberField()
        fields = (
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "phone",
        )
