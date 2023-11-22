from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . import views
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid login details")
            return redirect('login')

    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME ALREADY TAKEN")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "EMAIL ALREADY TAKEN")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            email=email, password=password)
                user.save()
                print("USER CREATED")
                return redirect('login')
        else:
            print("PASSWORD NOT MATCHED")
            messages.info(request, "PASSWORD NOT MATCHED")
            return redirect('register')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')