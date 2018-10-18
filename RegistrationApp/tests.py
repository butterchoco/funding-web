from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import registrationIndex
from .models import user_registration
from .forms import user_registration_form

# Create your tests here.


class RegistrationApp_testcase(TestCase):
    
    def test_Registration_registration_url_is_exist(self):
        response = Client().get('/registration/')
        self.assertEqual(response.status_code, 200)

    def test_using_registration_func(self):
        found = resolve('/registration/')
        self.assertEqual(found.func, registrationIndex)

    def test_model_can_create_new_user_registration(self):
        user_registration.objects.create(nama='Anonymous', tanggal_lahir='1999-02-02', email='anonymous@gmail.com', password='12wdwa214')
        counting_all_available_user_registration = user_registration.objects.all().count()
        self.assertEqual(counting_all_available_user_registration, 1)

    def test_form_user_registration_input_has_placeholder_and_css_classes(self):
        form = user_registration_form()
        self.assertIn('class="form-control"', form.as_p())

    def test_user_form_validation_for_blank_items(self):
        form = user_registration_form(data={'nama': '', 'tanggal_lahir': '', 'email': '', 'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nama'], ["This field is required."])
        self.assertEqual(form.errors['tanggal_lahir'], ["This field is required."])
        self.assertEqual(form.errors['email'], ["This field is required."])
        self.assertEqual(form.errors['password'], ["This field is required."])

    def test_TP1_program_registration_post_success(self):
        test = 'Anonymous'
        response_post = Client().post('/registration/', {'nama': test, 'tanggal_lahir': '1999-02-02', 'email': 'staw@gmail.com', 'password': '16532000'})
        self.assertEqual(response_post.status_code, 302)

    def test_TP1_program_registration_post_error(self):
            test = 'anonymous' * 400
            self.assertEqual(user_registration.objects.filter(nama=test).count(), 0)