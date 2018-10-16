from django.conf.urls import url
from .views import newsIndex

urlpatterns = [
    url(r'^$', newsIndex, name='news'),
]