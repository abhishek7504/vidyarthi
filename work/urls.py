from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('account/basic_info/',views.profile , name = 'profile'),
    path('account/basic_info/education/',views.education , name = 'education'),
    path('account/basic_info/education/courses/',views.courses , name = 'courses'),
    path('account/basic_info/education/courses/docs',views.other_doc , name = 'other_doc'),
]