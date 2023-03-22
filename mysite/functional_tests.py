from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

# from django.test import Client, TestCase

class test_Register(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        

    def tearDown(self):
        self.browser.quit()

    def test_hompage(self):
        
        self.browser.get('http://localhost:8000')

        self.assertIn('ตัวช่วยในการลงทะเบียน', self.browser.title)


if __name__ == '__main__':
    unittest.main()





