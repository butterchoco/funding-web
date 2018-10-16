from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import newsIndex

# Create your tests here.


class BeritaApp_testcase(TestCase):

    def test_TP1_news_url_is_exist(self):
        response = Client().get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_using_news_func(self):
        found = resolve('/news/')
        self.assertEqual(found.func, newsIndex)