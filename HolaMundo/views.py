from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'title': 'home', 'content': 'Lorem Ipsum home content'})

def about(request):
    return render(request, 'about.html', {'title': 'About', 'content': 'Lorem Ipsum  about content'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Contact', 'content': 'Lorem Ipsum contact content'})        