from django.urls import path

from . import views
app_name = 'work'

urlpatterns = [
    
    path('basic_info/',views.basic_info , name = 'profile'),
    path('education/create/',views.education , name = 'education'),
    path('basic_info/education/courses/',views.courses , name = 'courses'),
    path('basic_info/education/courses/docs/',views.other_doc , name = 'other_doc'),
    path('<slug:slug>/', views.profile , name='view_profile'),
]