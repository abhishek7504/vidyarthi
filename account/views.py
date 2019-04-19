from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm , ProfileForm ,EducationForm,CoursesForm,Other_docForm
from django.contrib.auth.models import User
# from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
@login_required
def dashboard(reqeust):

    return render(reqeust,'account/dashboard.html',{'section':'dashboard'})

# User = get_user_model()
def register(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
      cd = user_form.cleaned_data
      
      # Create a new user object but avoid saving yet
      new_user = user_form.save(commit=False)
      # set the chosen password
      new_user.set_password(cd['password'])
      #save the user  objects
      new_user.save()
      Profile.objects.create(user=new_user)
      
      return render(request, "account/register_done.html", 
                                                        {'new_user':new_user})
  else:
    user_form = UserRegistrationForm()
  return render(request, "account/register.html", 
                                                  {'user_form':user_form}) 
   
def profile(request):
    
    if request.method == 'POST':
        input_form = ProfileForm(data=request.POST, instance=request.user.profile)
        if input_form.is_valid():
            input_form.save()
        return HttpResponse('Profile updated successfully!')    
    else:
        input_form = ProfileForm(instance=request.user.profile)

    return render(request,'pages/basic.html',{'input_form':input_form})

def education(request, pk):
    education = get_object_or_404(Education, id=pk)
    if request.method =='POST':
      education_form = EducationForm(data=request.POST, instance=education)
      if education_form.is_valid():
        education_form.save()
      return HttpResponse('Education updated successfully!')    
    else:
      education_form = EducationForm(instance=education)
    return render(request,'pages/education.html',{'education_form':education_form})
        
def courses(request, pk):
    # course = get_object_or_404(Courses, id=pk)
    course = Courses.objects.get(id=pk)
    if request.method == 'POST':
      couses_form = CoursesForm(request.POST, instance=course)    
      if courses_form.is_valid():
        couses_form.save()
      return HttpResponse('Course updated successfully!')  
    else:
        couses_form = CoursesForm(instance=course)
    return render(request,'pages/courses.html',{'couses_form':couses_form})

def other_doc(request):

    if request.method == 'POST':
      doc_form = Other_docForm(request.POST)
      if doc_form.is_valid():
        doc_form.save()
    else:
      doc_form = Other_docForm
    return render(request,'pages/doc.html',{'doc_form':doc_form})
