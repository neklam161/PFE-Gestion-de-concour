from django.urls import path

from django.contrib.auth import views as auth_views
from student.views import *
urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_view,name="login"),
    path('',homepage,name='home'),
    path('logout/',logout_view,name="logout"),
    path('profile/',profile,name="profile"),
    path('concour/',concour,name="studentpage"),
    path('inscription/<int:concour_id>/', inscrire, name='inscription'),
    path('form_step1/', form_step1, name='form_step1'),
    path('form_step2/', form_step2, name='form_step2'),
    path('form_step3/', form_step3, name='form_step3'),
    path('form_step4/', form_step4, name='form_step4'),
]





