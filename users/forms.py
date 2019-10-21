from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, RegexValidator

from .models import *


class UserAddForm(forms.Form):
    name = forms.CharField(max_length=150, required=True, initial=None,
                           validators=[
                               RegexValidator('^[a-z A-Z]*$', message="Name Url must be a combination of Alphabets")],
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'id': 'name',
                                   'placeholder': 'Enter User Name'})
                           )
    email = forms.EmailField(max_length=150, required=True, initial=None,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'type': 'email',
                                     'id': 'email',
                                     'placeholder': 'Enter User Email'})
                             )
    password = forms.CharField(max_length=128,
                               required=True,
                               initial=None,
                               validators=[RegexValidator('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                                                          message="Minimum eight characters, at least one letter and one number")],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'password',
                                       'id': 'password',
                                       'placeholder': 'Enter password'})
                               )

    def clean_name(self):
        name = self.cleaned_data['name']
        minlength = 5
        if len(name) < minlength or name is None:
            raise forms.ValidationError('Length will be minimum 5 Characters')
        if name is None:
            raise forms.ValidationError('')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
            try:
                validate_email(email)
            except ValidationError as e:
                print("Bad email, details:", e)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email
        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email Address Is Already In Use.')


class UserUpdateForm(forms.Form):
    name = forms.CharField(max_length=150, required=True, initial=None,
                           validators=[
                               RegexValidator('^[a-z A-Z]*$', message="Name Url must be a combination of Alphabets")],
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'id': 'name',
                                   'placeholder': 'Type User Name'})
                           )

    password = forms.CharField(max_length=128,
                               required=True,
                               initial=None,
                               validators=[RegexValidator('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                                                          message="Minimum eight characters, at least one letter and one number")],
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'type': 'password',
                                       'id': 'password',
                                       'placeholder': 'Type password'})
                               )

    def clean_name(self):
        name = self.cleaned_data['name']
        minlength = 2
        if len(name) < minlength or name is None:
            raise forms.ValidationError('Length will be minimum two Characters')
        if name is None:
            raise forms.ValidationError('')
