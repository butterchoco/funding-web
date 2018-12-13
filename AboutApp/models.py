from django.db import models

# Create your models here.

class testi_Model(models.Model):
    name = models.CharField(max_length=200)
    komenModel = models.TextField(max_length=1000)
