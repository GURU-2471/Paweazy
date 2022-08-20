from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request,"authentication/home.html")

def login(request):
    return render(request,"authentication/login.html")
    
def signin(request):
    return render(request,"authentication/signin.html")

def forgot(request):
    return render(request,"authentication/forgot.html")

def vaccine(request):
    return render(request,"authentication/vaccine.html")

def deworming(request):
    return render(request,"authentication/deworming.html")

def spoton(request):
    return render(request,"authentication/spoton.html")

def signout(request):
    pass


def about(request):
    return HttpResponse("This is About Page")