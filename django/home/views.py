from django.shortcuts import render

from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def shop1(request):
    return render(request, 'shop1.html') 


def login(request):
    return render(request, 'login.html') 

def laptop(request):
    return render(request, 'laptop.html') 

def cart(request):
    return render(request, 'cart.html') 


def phone(request):
    return render(request,'phone.html')
    
def services(request):
    return render(request, 'services.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 