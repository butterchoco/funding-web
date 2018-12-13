<<<<<<< HEAD
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', aboutIndex, name='about'),
    path(r'^testi_json/', testi_json, name='regisInJson'),
]
=======
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', aboutIndex, name='about'),
    url(r'^tambah_komentar', tambah_komentar, name='tambah_komentar')
]
>>>>>>> f4a7cff61f49d7c2f3a284dcdcccc966e9f9bd86
