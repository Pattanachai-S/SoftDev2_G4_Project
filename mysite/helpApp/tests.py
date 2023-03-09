import time
from django.test import TestCase
from helpApp.models import Subject,Section

# Create your tests here.
class ChecksubjectTest(TestCase):
    checksubject_url = '/help/checksubject'

    def test_uses_checksubject_template(self):
        response = self.client.get(self.checksubject_url)
        self.assertTemplateUsed(response, 'helpApp/checksubject.html')

    def test_search_subject(self):
        response = self.client.post(self.checksubject_url, data={
            'subject': '010123121'
            })
        #self.assertIn('010123121', response.content.decode(), "Can not POST request.")  # test can post request

        # Test database here.
        subject = Subject.objects.filter(subject_ID='010123121')
        self.assertEqual("DATABASE SYSTEMS", subject.name)

        time.sleep(10)
        self.assertIn("DATABASE SYSTEMS", response.content.decode())
