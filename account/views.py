from django.shortcuts import render, get_object_or_404
from . forms import UserRegistrationForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from work.models import Profile

@login_required
def dashboard(reqeust):

    return render(reqeust,'pages/dashboard.html',{'section':'dashboard'})



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
