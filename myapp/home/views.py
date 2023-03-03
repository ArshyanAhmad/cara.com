from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def base(request):
    return render(request, "base.html")

def shop(request):
    return render(request, "shop.html")

def cart(request):
    return render(request, "cart.html")

def sproduct(request):
    return render(request, "sproduct.html")

def contact(request):
    if(request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name = name, email = email, desc = desc, phone = phone ,date = datetime.today())
        contact.save()
        messages.success(request, 'Your Form Has Been Submit 😄!')

    return render(request, "contact.html")
