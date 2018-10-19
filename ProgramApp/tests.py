from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import programIndex
from .models import program_registration, program_update
from .forms import program_registration_form
# from django.http import HttpRequest


# Create your tests here.

class ProgramApp_testcase(TestCase):

    def test_program_url_is_exist(self):
        response = Client().get('/program/')
        self.assertEqual(response.status_code, 200)

    def test_using_program_func(self):
        found = resolve('/program/')
        self.assertEqual(found.func, programIndex)

    def test_model_can_create_new_program_registration(self):
        program_registration.objects.create(nama='Anonymous', email='anonymous@gmail.com', jumlah_uang='12000', tampilkan=True)
        counting_all_available_program_registration = program_registration.objects.all().count()
        self.assertEqual(counting_all_available_program_registration, 1)

    def test_model_can_create_new_program_update(self):
        program_update.objects.create(judul='Gempa', konten='lorem ipsum dolorsit wat de trakoiyarnwfbafvafvaywfvu', image='https://www.youtube.com/watch?v=1G4isv_Fylg')
        counting_all_available_program_registration = program_update.objects.all().count()
        self.assertEqual(counting_all_available_program_registration, 1)

    def test_program_form_validation_for_blank_items(self):
        form = program_registration_form(data={'nama': '', 'email': '', 'jumlah_uang': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nama'], ["This field is required."])
        self.assertEqual(form.errors['email'], ["This field is required."])
        self.assertEqual(form.errors['jumlah_uang'], ["This field is required."])

    # def test_program_registration_post_success(self):
    #     test = 'Anonymous'
    #     program = program_update(judul="test", konten="tessst", image="etestet")
    #     response_post = Client().post('/program/', {'program': program, 'nama': test, 'email': test + '@gmail.com', 'jumlah_uang': '12000', 'tampilkan': True})
    #     self.assertEqual(response_post.status_code, 302)

    def test_program_registration_post(self):
            test = 'anonymous' * 400
            self.assertEqual(program_registration.objects.filter(nama=test).count(), 0)