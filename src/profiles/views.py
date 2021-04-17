from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.sessions.models import Session 
# Create your views here.

from .models import Employee
from .forms import CreateEmployee
def home(request):
	obj = Employee.objects.all()
	return render(request,'profiles/home.html',{'obj':obj})

def loginpage(request):
	error = ""
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password1')
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			error = "error"

	return render(request,'profiles/login.html',{'error':error})


def logoutpage(request):
	logout(request)
	return redirect('home')

def profileview(request,i):
	if request.user.is_superuser:
		if request.method == 'POST' :
			form_emp = CreateEmployee(request.POST)
			if form_emp.is_valid():
				form_detail = Employee.objects.get(email=i)
				form_detail.first = request.POST.get('first')
				form_detail.last = request.POST.get('last')
				form_detail.short = request.POST.get('short')
				form_detail.title = request.POST.get('title')
				form_detail.email = request.POST.get('email')
				form_detail.contact = request.POST.get('contact')
				form_detail.contact_ext = request.POST.get('contact_ext')
				form_detail.team = request.POST.get('team')
				form_detail.job_title = request.POST.get('job_title')
				form_detail.save()
				rusk = 'success'
				print(form_emp)
			else:
				print('error')
				rusk = 'error'
			return render (request,'profiles/home.html',{'rs':rusk})

		else:
			if '@' not in i:
				rusk = ''
				user_detail = Employee.objects.get(id=i)
				user_detail.viewers += 1
				user_detail.save()
			else:
				rusk = 'edit'
				user_detail = Employee.objects.get(email=i)
		print("Waste")
		label, data = ['jan','feb','mar','apr','may'], [1,10,8,5,2]
		return render (request,'profiles/pro_view.html',{'us':user_detail,'rs':rusk,'label':label,'data':data})

	else:
		return redirect('login')
