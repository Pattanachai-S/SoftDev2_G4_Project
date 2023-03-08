from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

from django.test import Client, TestCase

class Register(TestCase):
    
    def test_contact_form_submission(self):
        # Create a test client
        client = Client()

        # Make a POST
        response = client.post('/submit/', {'name': 'groot', 'surname': 'groot@avengers.com', 'username': 'im_groot' , 'password': 'IamGroot'})
        
        #successful form submission
        self.assertEqual(response.status_code, 302)

        # Follow redirect
        response = client.get(response.url)

        # Check result of register...
