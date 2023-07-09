from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import About
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        about = About(name=name, email=email, feedback=feedback, date=datetime.today())
        about.save()
        messages.success(request, "Your feedback has been sent to the developer Himanshu Panday")
    return render(request,'about.html')

def action(request):
    return render(request,'action.html')

def adventure(request):
    return render(request,'adventure.html')

def roleplaying(request):
    return render(request,'roleplaying.html')