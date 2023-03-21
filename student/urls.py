from django.urls import path

from django.contrib.auth import views as auth_views
from student.views import register,login_view,homepage,logout_view,concour,inscrire
urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_view,name="login"),
    path('',homepage,name='home'),
    path('logout/',logout_view,name="logout"),
    path('concour/',concour,name="studentpage"),
    path('inscription/<int:concour_id>/', inscrire, name='inscription'),
]





