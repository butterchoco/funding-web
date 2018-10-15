from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import programIndex
from .models import program_registration
from .forms import program_registration_form
# from django.http import HttpRequest


# Create your tests here.

class TP1_testcase(TestCase):

    # def test_TP1_registration_url_is_exist(self):
    #     response = Client().get('/registration/')
    #     self.assertEqual(response.status_code, 200)

    # def test_using_registration_func(self):
    #     found = resolve('/registration/')
    #     self.assertEqual(found.func, registration)

    # def test_TP1_news_url_is_exist(self):
    #     response = Client().get('/news/')
    #     self.assertEqual(response.status_code, 200)

    # def test_using_news_func(self):
    #     found = resolve('/news/')
    #     self.assertEqual(found.func, news)

    def test_TP1_program_url_is_exist(self):
        response = Client().get('/program/')
        self.assertEqual(response.status_code, 200)

    def test_using_program_func(self):
        found = resolve('/program/')
        self.assertEqual(found.func, programIndex)

    # def test_model_can_create_new_user_registration(self):
    #     user_registration.objects.create(nama='Anonymous', tanggal_lahir='04-04-1999', email='anonymous@gmail.com', password='12wdwa214')
    #     counting_all_available_user_registration = user_registration.objects.all().count()
    #     self.assertEqual(counting_all_available_user_registration, 1)

    # def test_form_user_registration_input_has_placeholder_and_css_classes(self):
    #     form = user_registration_form()
    #     self.assertIn('class="form-control"', form.as_p())

    # def test_user_form_validation_for_blank_items(self):
    #     form = user_registration_form(data={'nama': '', 'tanggal_lahir': '', 'email': '', 'password': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors['nama'], ["This field is required."])
    #     self.assertEqual(form.errors['tanggal_lahir'], ["This field is required."])
    #     self.assertEqual(form.errors['email'], ["This field is required."])
    #     self.assertEqual(form.errors['password'], ["This field is required."])

    # def test_TP1_user_registration_post_success_and_render_the_result(self):
    #     test = 'Anonymous'
    #     response_post = Client().post('/registration/', {'nama': test, 'tanggal_lahir': '04-04-1999', 'email': test + '@gmail.com', 'password': '12g42r14e'})
    #     self.assertEqual(response_post.status_code, 302)

    # def test_TP1_user_registration_post_error_and_render_the_result(self):
    #         response_post = Client().post('/registration/', {'nama': '', 'tanggal_lahir': '14289125', 'email': 'retafvyaf.com', 'password': '#$%^&*()'})
    #         self.assertEqual(response_post.status_code, 302)

    def test_model_can_create_new_program_registration(self):
        program_registration.objects.create(nama='Anonymous', email='anonymous@gmail.com', jumlah_uang='12000')
        counting_all_available_program_registration = program_registration.objects.all().count()
        self.assertEqual(counting_all_available_program_registration, 1)

    def test_form_program_registration_input_has_placeholder_and_css_classes(self):
        form = program_registration_form()
        self.assertIn('class="form-control"', form.as_p())

    def test_program_form_validation_for_blank_items(self):
        form = program_registration_form(data={'nama': '', 'email': '', 'jumlah_uang': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nama'], ["This field is required."])
        self.assertEqual(form.errors['email'], ["This field is required."])
        self.assertEqual(form.errors['jumlah_uang'], ["This field is required."])

    def test_TP1_program_registration_post_success_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/program/', {'nama': test, 'email': test + '@gmail.com', 'jumlah_uang': '12000'})
        self.assertEqual(response_post.status_code, 302)

    def test_TP1_program_registration_post_error_and_render_the_result(self):
            test = 'anonymous' * 400
            self.assertEqual(program_registration.objects.filter(nama=test).count(), 0)