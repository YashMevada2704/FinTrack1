from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def signin(request):
    if request.method == "POST":
        email =request.POST.get("email")
        password = request.POST.get("password")

       

        return redirect("home")
    
    return render(request,"signin.html")

def signup(request):
    if request.method ==  "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        return redirect("signin")
    
    return render(request,"signup.html")

def home(request):
    return render(request,"home.html")