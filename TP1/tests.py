from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
# from django.http import HttpRequest


# Create your tests here.

class TP1_testcase(TestCase):

    def test_TP1_url_is_exist(self):
        response = Client().get('/tp-1/')
        self.assertEqual(response.status_code, 200)

    def test_using_index_func(self):
        found = resolve('/tp-1/')
        self.assertEqual(found.func, index)