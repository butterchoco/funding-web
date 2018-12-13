from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', aboutIndex, name='about'),
    url(r'^tambah_komentar', tambah_komentar, name='tambah_komentar')
]
