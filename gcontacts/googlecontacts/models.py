from django.db import models


# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, default="")

class Adminusers(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

