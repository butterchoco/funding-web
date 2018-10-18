from django.db import models

# Create your models here.


class news_update(models.Model):
    judul = models.CharField(max_length=100)
    konten = models.TextField(max_length=400)
    image = models.CharField(max_length=200)