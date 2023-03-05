from django.urls import path
from student import views
# from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name="login"),
    path('',views.homepage,name='home'),
    path('logout/',views.logout_view,name="logout"),
    path('concour/',views.student_homepage,name="studentpage")
]





