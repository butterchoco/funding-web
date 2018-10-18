from django.db import models
# Create your models here.


class program_registration(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    jumlah_uang = models.IntegerField()
    tampilkan = models.BooleanField()


class program_update(models.Model):
    judul = models.CharField(max_length=50)
    konten = models.TextField(max_length=500)
    image = models.CharField(max_length=200)