from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Services(request):
    return render(request, 'services.html')

def Blognews(request):
    return render(request, 'blognews.html')

def Gallery(request):
    return render(request, 'gallery.html')

def Contact(request):
    return render(request, 'contact.html')


