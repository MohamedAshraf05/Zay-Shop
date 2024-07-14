# accounts/forms.py
from django import forms
from .models import UserProfile , Contact


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email' , 'phone' , 'city' , 'address' , 'image' , 'nationality']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject' , 'message' , 'phone' , 'email']