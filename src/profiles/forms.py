from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee

class CreateEmployee(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['first','last','short','title','email', 'contact','contact_ext','team','job_title']