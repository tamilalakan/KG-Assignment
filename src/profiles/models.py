from django.db import models

# Create your models here.

class Employee(models.Model):
	first		= models.CharField(max_length=30)
	last 		= models.CharField(max_length=30)
	short 		= models.CharField(max_length=30)
	title 		= models.CharField(max_length=30)
	email 		= models.EmailField(max_length=40)
	contact 	= models.CharField(max_length=10)
	contact_ext = models.CharField(max_length=5)
	join_date 	= models.CharField(max_length=30)
	large 		= models.CharField(max_length=300)
	medium 		= models.CharField(max_length=300)
	thumbnail 	= models.CharField(max_length=300)
	team 		= models.CharField(max_length=30)
	job_title 	= models.CharField(max_length=30)
	last_login 	= models.CharField(max_length=30)
	loggedIn 	= models.CharField(max_length=30)
	viewers = models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.first +" "+ self.last