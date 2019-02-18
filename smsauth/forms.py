from django import forms
from .models import signup, verify

class signupForm(forms.ModelForm):

    class Meta:
        model = signup
        fields = ('username', 'password', 'phone')

class verifyForm(forms.ModelForm):

     class Meta:
         model = verify
         fields = ('smscode',)
