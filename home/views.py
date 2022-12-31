from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import search
# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
def water(request):
    return render(request, 'water.html')
def desert(request):
    return render(request, 'desert.html')
def forest(request):
    return render(request, 'forest.html')
def monuments(request):
    return render(request, 'monuments.html')
 

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

def search(request):
    return render(request,'search.html')
    # return HttpResponse('this is search')