from django.conf.urls import url
from .views import newsIndex, newsDetails

urlpatterns = [
    url(r'^$', newsIndex, name='news'),
    url(r'(?P<id>[-\w]+)/$', newsDetails, name='newsDetails')
]