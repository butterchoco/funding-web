from django.db import models
# Create your models here.


class program_registration(models.Model):
    # program = models.ManyToManyField("program_update", through="program_update", through_fields="test")
    program = models.ForeignKey("program_update", on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    jumlah_uang = models.IntegerField()
    tampilkan = models.BooleanField()


class program_update(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)
