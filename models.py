from django.db import models

# Create your models here.

class login(models.Model):
	username=models.Charfield(max_length=20)
	password=models.CharField(max_length=10)
def _str_(self):
	return self.name
