from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CreateUserForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',)
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number']


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")

# class AccountUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', 'username',)
#
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         try:
#             account = User.objects.exclude(pk=self.instance.pk).get(email=email)
#         except User.DoesNotExist:
#             return email
#         raise forms.ValidationError('Email "%s" is already in use.' % account)
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         try:
#             account = User.objects.exclude(pk=self.instance.pk).get(username=username)
#         except User.DoesNotExist:
#             return username
#         raise forms.ValidationError('Username "%s" is already in use.' % username)