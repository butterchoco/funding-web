from django.conf.urls import url
from .views import registrationIndex

urlpatterns = [
    url(r'^$', registrationIndex, name='registrationIndex'),
]