from django.test import TestCase

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
        self.assertIn('user123456', response.content.decode())  # test can post request

        " Test database here "



    def test_register(self):
        pass

