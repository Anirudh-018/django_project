from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in succesfully")
            return redirect('home')
        else:
            messages.success(request,'Error logging in')
            return redirect('home')
    else:
        return render(request,'home.html',{})
def login_users(request):
    pass
def logout_users(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')