from django.contrib.auth.models import User
from django import forms

'''user reg. form'''

class UserRegistrationForm(forms.ModelForm):


    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

    def cleaned_data(self):
        qs = self.cleaned_data.get('username')
        if qs.exists() and qs.count() == 1:
            raise forms.ValidationError('This username already exists')
        return qs    
        
    def clean_password2(self):

        cd = self.cleaned_data
        if cd['password'] != cd['password2'] :
            raise forms.ValidationError('PASSWORD DOESN\'T MATCH')

        return cd['password']  

    '''model view froms'''






