from django.db import models

# Create your models here.


class user_registration(models.Model):
    nama = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=50)