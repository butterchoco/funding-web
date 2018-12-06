from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import aboutIndex
##from .models import news_update

# Create your tests here.


class BeritaApp_testcase(TestCase):

    def test_TP1_about_url_is_exist(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_using_about_func(self):
        found = resolve('/about/')
        self.assertEqual(found.func, aboutIndex)

##    def test_model_can_create_new_program_registration(self):
##        news_update.objects.create(judul='PPW is Fan', konten='Saya senang ppw udah itu aja ya oke deh')
##        counting_all_available_program_registration = news_update.objects.all().count()
##        self.assertEqual(counting_all_available_program_registration, 1)
