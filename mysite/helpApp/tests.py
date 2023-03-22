import time
from django.test import TestCase, Client
from helpApp.models import Subject,Section
from django.contrib.auth.models import User
from .check_overlap import Overlap



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
        # subject.name = "DATABASE SYSTEMS"
        # subject.subject_ID = "010123121"
        # subject.save()

        response = self.client.get(self.checksubject_url, {
            'search-subject': '010123121'
            })
        self.assertEqual(response.status_code, 200)
        #self.assertIn('010123121', response.content.decode(), "Can not POST request.")  # test can post request

        # Test database here.
        # subject = Subject.objects.get(subject_ID='010123121')
        # self.assertEqual("DATABASE SYSTEMS", subject.name)

        # time.sleep(10)
        self.assertIn("DATABASE SYSTEMS", response.content.decode())


class Check_overlap_test(TestCase):

    s1 = ["010113138", "S.1"] # 010113138 CIRCUITS AND ELECTRONICS3(3-0)         S.1 M 13:00
    s2 = ["010113139", "L.1"] # 010113139 CIRCUITS AND ELECTRONICS LAB1(0-1)     L.1 H 9:00
    s3 = ["010123103", "S.1"] # 010123103 ALGORITHMS AND DATA STRUCTUR3(2-1)     S.1 T 13:00
    s4 = ["010123118", "S.1"] # 010123118 COMPUTER NETWORKS3(3-0)                S.1 W 13:00        อ. 28/3/2566 9:00-12:00
    s5 = ["010123120", "L.1"] # 010123120 EMBEDDED SYSTEM DESIGN LABOR1(0-1)     L.1 W 13:00
    s6 = ["010123121", "S.1"] # 010123121 DATABASE SYSTEMS3(3-0)                 S.1 F 9:00         จ. 27/3/2566 9:00-12:00
    s7 = ["010123134", "S.1"] # 010123134 COMPUTER ORGANIZATION3(3-0)            S.1 M 9:00
    s8 = ["010123135", "S.1"] # 010123135 LINEAR ALGEBRA3(3-0)                   S.1 H 9:00

    e1 = ["010123213", "S.1"] # 010123213 ARTIFICIAL INTELLIGENCE 3(3-0)         final อ. 4/4/2566 9:00-12:00  S.1 T 9:00-12:00
    e2 = ["040203100", "S.1"] # 040203100 GENERAL MATHEMATICS 3(3-0)             final อ. 4/4/2566 9:00-12:00  S.1 M 13:00

    o = Overlap()

    def test_subject_can_submit(self):
        self.assertFalse(self.o.is_subject_overlap(self.s1, self.s2))
        self.assertFalse(self.o.is_subject_overlap(self.s6, self.s7))
        self.assertFalse(self.o.is_subject_overlap(self.s4, self.s6))

    def test_subject_time_overlap(self):
        # study time overlap
        self.assertTrue(self.o.is_subject_overlap(self.s4, self.s5))  
        self.assertTrue(self.o.is_subject_overlap(self.s1, self.e2))

    def test_subject_exam_overlap(self):
        # exam time overlap
        self.assertTrue(self.o.is_subject_overlap(self.e1, self.e2))




class Add_subject_test(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
