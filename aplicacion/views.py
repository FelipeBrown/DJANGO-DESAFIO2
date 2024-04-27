from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request , 'home.html' ,{'hola':'hola'} )

def about(request):
    return render (request , 'about.html' ,{'hola':'hola'} )

def contact(request):
    return render (request , 'contact.html' ,{'hola':'hola'} )