from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', aboutIndex, name='about'),
    path(r'^testi_json/', testi_json, name='regisInJson'),
]
