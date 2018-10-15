from django.conf.urls import url
from .views import programIndex

urlpatterns = [
    url(r'^$', programIndex, name='programIndex'),
]