from django.shortcuts import render, get_object_or_404
from . forms import ProfileForm ,EducationForm,CoursesForm,Other_docForm
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, ProfileQRCode

def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    qrcode, created = ProfileQRCode.objects.get_or_create(profile=profile)   

    return render(request,'pages/view_profile.html',{'profile':profile
                                                    ,'qrcode':qrcode})

@login_required   
def basic_info(request):
    
    if request.method == 'POST':
        input_form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if input_form.is_valid():
            input_form.save()
           
    else:
        input_form = ProfileForm(instance=request.user.profile)

    return render(request,'pages/basic.html',{'input_form':input_form})

@login_required
def education(request):
    new_user = request.user
    profile = Profile.objects.get(user=new_user.pk)
    edu, created = Education.objects.get_or_create(Profile=profile)
    if request.method =='POST':
      education_form = EducationForm(data=request.POST, instance=edu, files=request.FILES)
      if education_form.is_valid():
        education_form.save()
      # return HttpResponse('Education updated successfully!')    
    else:
      education_form = EducationForm(instance=edu)
    return render(request,'pages/education.html',{'education_form':education_form})

@login_required        
def courses(request):
    new_user = request.user
    profile = Profile.objects.get(user=new_user.pk)
    cour, created = Courses.objects.get_or_create(Profile=profile)
    if request.method == 'POST':
      couses_form = CoursesForm(request.POST, instance=cour , files=request.FILES)    
      if couses_form.is_valid():
        couses_form.save()
 
    else:
        couses_form = CoursesForm(instance=cour)
    return render(request,'pages/courses.html',{'couses_form':couses_form})

@login_required
def other_doc(request):
    user = request.user
    profile = Profile.objects.get(user=user.pk)
    doc, created = Other_doc.objects.get_or_create(Profile=profile)
    if request.method == 'POST':
      doc_form = Other_docForm(request.POST,  instance=doc, files=request.FILES)
      if doc_form.is_valid():
        doc_form.save()
         
    else:
      doc_form = Other_docForm(instance=doc)
    return render(request,'pages/doc.html',{'doc_form':doc_form})
