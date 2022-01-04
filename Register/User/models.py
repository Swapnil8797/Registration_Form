from django.db import models

# Create your models here.
class Userdetails(models.Model):
	username = models.CharField(max_length=255)
	mobile_no = models.IntegerField()
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=255)
	Select_User = models.CharField(max_length=255)