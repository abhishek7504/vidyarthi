from django import forms
from .models import Profile,Education,Courses,Other_doc

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'status','mother_name','fathers_name','date_of_birth','phone_number','country','state','city','area')
        exclude = ('user',)

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('__all__')
        exclude = ('Profile',)

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('__all__')
        exclude = ('Profile',)

class Other_docForm(forms.ModelForm):
    class Meta:
        model = Other_doc
        fields = ('__all__')
        exclude = ('Profile',)

