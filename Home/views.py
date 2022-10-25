from django.shortcuts import render

# Credefate your views here.
def admin(request):
    return render(request,'login.html',{})