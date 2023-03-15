from django.urls import path
from uni_admin import views
# from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('register/',views.register,name='register'),
    #path('login/',views.login_view,name="login"),
    #path('',views.homepage,name='home'),
    #path('logout/',views.logout_view,name="logout"),
    path('concour/',views.concour_admin,name="concour"),
    path('add_concour/',views.add_con,name="add_concour"),
    path('delete-concour/<int:concour_id>/', views.delete_concour, name='delete_concour'),
]





