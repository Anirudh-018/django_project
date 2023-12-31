from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import AddJobForm, SignUpForm
from .models import Job
# Create your views here.
def home(request):
    jobs=Job.objects.all()
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
        return render(request,'home.html',{'jobs':jobs})
def logout_users(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def job_desc(request,pk):
    if(request.user.is_authenticated):
        job_record=Job.objects.get(id=pk)
        return render(request,'job.html',{'job_description':job_record})
    else:
        messages.success(request,"Job Not Found")
        return redirect('home')

def delete_job(request,pk):
    if request.user.is_authenticated:
        job=Job.objects.get(id=pk)
        job.delete()
        messages.success(request,"Deleted the job")
        return redirect('home')
    else:
        messages.success(request,"Login first")
        return redirect('home')
def add_job(request):
    form=AddJobForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                print(form)
                add_job=form.save()
                messages.success(request,"Record Added")
                return redirect('home')
        return render(request,'add_job.html',{"form":form})
    else:
        messages.success(request,"Login first")
        return redirect('home')
def update_job(request,pk):
    if request.user.is_authenticated:
        current_job=Job.objects.get(id=pk)
        form=AddJobForm(request.POST or None,instance=current_job)
        if form.is_valid():
            form.save()
            messages.success(request,"Job Updated")
            return redirect('home')
        return render(request,'update_job.html',{'form':form})
    else:
        messages.success(request,"Login first")
        return redirect('home')