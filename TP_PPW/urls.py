"""TP_PPW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

from LogoutApp import views as logout_views
from ProgramApp import views as program_views
from RegistrationApp import views as regis_views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/news/')),
    url(r'^admin/', admin.site.urls),
    url(r'^program/', include(('ProgramApp.urls', 'ProgramApp'), namespace='donasi_kuy')),
    url(r'^news/', include(('BeritaApp.urls', 'BeritaApp'), namespace='news')),
    url(r'^registration/', include(('RegistrationApp.urls', 'RegistrationApp'), namespace='registration')),
    url(r'^donationList/', include(('donationListApp.urls', 'donationListApp'), namespace='donationList')),
    url(r'^logout/', logout_views.logout, name='logoutapp'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^validate/', program_views.validate, name='validate'),
    url(r'^login/', regis_views.loginIndex, name='login'),
    url(r'^about/', include(('AboutApp.urls', 'AboutApp'), namespace='about')),
]
