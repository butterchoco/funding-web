from django.db import models

# Create your models here.


class news_update(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)