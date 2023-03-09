from django.test import TestCase, Client
from django.contrib.auth.models import User
import time

# Create your tests here.

class RegisterTest(TestCase):

    register_url = '/users/register'

    #

    def test_uses_register_template(self):
        response = self.client.get(self.register_url)
        self.assertTemplateUsed(response, 'userApp/register.html')


    def test_can_register(self):
        response = self.client.post(self.register_url, data={
            'username': 'user123456',
            'password1': 'password-123456',
            'password2': 'password-123456'
            })
        #self.assertIn('user123456', response.content.decode(), "Can not POST request.")  # test can post request

        # Test database here.
        users = User.objects.filter(username='user123456')
        self.assertNotEqual(users.count(), 0, "Can not save user in database.")  # test is username in database
        queried_user = User.objects.get(username='user123456')
        self.assertEqual('user123456', queried_user.username)
        #self.assertEqual('password-123456', queried_user.password)
        #queried_user.delete()

class LoginTest(TestCase):

    login_url = '/users/login/'

    def test_uses_login_template(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'userApp/login.html')

    def test_can_login(self):
        response = self.client.post(self.login_url, data={
            'username': 'testuser123456',
            'password': 'password-123456'
            })
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(response, '/')  # redirects to home
    

