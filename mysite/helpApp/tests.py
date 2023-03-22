import time
from django.test import TestCase, Client
from .models import Subject,Section
from django.contrib.auth.models import User


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login(self):
        response = self.client.post('/users/login/', {'username': 'testuser', 'password': 'testpass'})
        self.assertRedirects(response, '/')

class ChecksubjectTest(TestCase):
    checksubject_url = '/help/checksubject'

    def test_uses_checksubject_template(self):
        response = self.client.get(self.checksubject_url)
        self.assertTemplateUsed(response, 'helpApp/checksubject.html')

    def test_search_subject(self):
        subject = Subject()
        subject.name = "DATABASE SYSTEMS"
        subject.subject_ID = "010123121"
        subject.save()

        response = self.client.post(self.checksubject_url, data={
            'subject': '010123121'
            })
        #self.assertIn('010123121', response.content.decode(), "Can not POST request.")  # test can post request

        # Test database here.
        subject = Subject.objects.get(subject_ID='010123121')
        self.assertEqual("DATABASE SYSTEMS", subject.name)

        time.sleep(10)
        self.assertIn("DATABASE SYSTEMS", response.content.decode())
