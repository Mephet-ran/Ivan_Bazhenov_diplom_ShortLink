from django.urls import path
from django.contrib.auth import views
from regist import views as regView

urlpatterns = [
    path('regist/', regView.register, name='reg'),
    path('profile/', regView.profile, name='profile'),
    path('', views.LoginView.as_view(template_name='regist/login.html'), name='login'),
    path('exit/', views.LogoutView.as_view(template_name='regist/exit.html'), name='exit'),
]
123
