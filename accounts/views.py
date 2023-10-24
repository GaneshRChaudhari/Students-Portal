from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User not registered")
            return redirect('registration_page')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
            # return render(request, 'home.html')
        messages.error(request, "Invalid Credentials")
    return render(request, 'login.html')


def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return render(request, 'register.html')

        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.save()
        messages.success(request, "User Registration Completed Successfully!!!")
    return render(request, 'register.html')



@login_required(login_url="/")
def logout_user(request):
    print("request.POST.get('username'):    : ", request.POST.get('username'))
    logout(request)
    messages.success(request, "User Logged Out")
    return redirect('login_user')


@login_required(login_url="/")
def search_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            user = User.objects.filter(username=username).get()
            return HttpResponse(f"User Details: {user}")
    return HttpResponse("User not found")



    


