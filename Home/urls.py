from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

# def home(request):
#     return render(request,'admin.html',{})

urlpatterns = [
    path('admin/',admin.site.urls),
    
]
