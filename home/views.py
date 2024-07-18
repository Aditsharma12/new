from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def epics(request):
    return render(request,'epics.html')
def podcast(request):
    return render(request,'podcast.html')
def library(request):
    return render(request,'library.html')
def best(request):
    return render(request,'best.html')
def about(request):
    return render(request,'about.html')
def contacts(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create a new Contact instance
        contact = Contact(email=email, phone=phone, message=message)
        contact.save()

        return render(request,'success.html')  # Replace with your success URL
    return render(request, 'contact.html')