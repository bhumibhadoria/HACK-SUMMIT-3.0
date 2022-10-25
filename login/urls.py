from django.urls import path
from . import views

urlpatterns = [  
    path('', views.loginaction),  # app homepage
]  