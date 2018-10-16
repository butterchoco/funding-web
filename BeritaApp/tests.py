from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import newsIndex
from .models import news_update

# Create your tests here.


class BeritaApp_testcase(TestCase):

    def test_TP1_news_url_is_exist(self):
        response = Client().get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_using_news_func(self):
        found = resolve('/news/')
        self.assertEqual(found.func, newsIndex)

    def test_model_can_create_new_program_registration(self):
        news_update.objects.create(judul='PPW is Fan', konten='Saya senang ppw udah itu aja ya oke deh')
        counting_all_available_program_registration = news_update.objects.all().count()
        self.assertEqual(counting_all_available_program_registration, 1)