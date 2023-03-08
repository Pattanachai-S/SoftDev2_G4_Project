from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class RegisterTest(TestCase):

    register_url = '/users/register'

    def test_uses_register_template(self):
        response = self.client.get(self.register_url)
        self.assertTemplateUsed(response, 'userApp/register.html')


    def test_can_register(self):
        response = self.client.post(self.register_url, data={
            'username': 'user123456',
            'password1': 'password123456',
            'password2': 'password123456'
            })
        self.assertIn('user123456', response.content.decode(), "Can not POST request.")  # test can post request

        # Test database here.
        users = User.objects.filter(username='user123456')
        self.assertNotEqual(users.count(), 0, "Can not save user in database.")  # test is username in database
        queried_user = User.objects.get(username='user123456')
        self.assertEqual(User.username, queried_user.username)
        self.assertEqual(User.password, queried_user.password)

