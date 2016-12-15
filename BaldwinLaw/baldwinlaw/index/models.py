from django.db import models
class Attorney(models.Model):
	name=models.CharField(max_length=200)
	telephone=models.CharField(max_length=20)
	email=models.CharField(max_length=100)
	image=models.ImageField(upload_to= 'image/', null=True, blank=True)


# Create your models here.
