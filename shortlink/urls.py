from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('short/', views.createLinkPage, name='short'),

]
