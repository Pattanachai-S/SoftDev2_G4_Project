from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

# from django.test import Client, TestCase
url = "http://localhost:8000"

class test_Register(unittest.TestCase):
    
    

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://localhost:8000/users/login/")

        usernamme_box = self.browser.find_element(By.NAME, "username")
        usernamme_box.send_keys('testuser123456')

        password_box = self.browser.find_element(By.NAME, "password")
        password_box.send_keys('password-123456')

        password_box.send_keys(Keys.ENTER)
        

    def tearDown(self):
        pass

    def test_hompage(self):
        
        self.browser.get('http://localhost:8000')

        self.assertIn('ตัวช่วยในการลงทะเบียน', self.browser.title)
    
    # def test_login(self):
    #     self.browser.get("http://localhost:8000/users/login/")

    #     usernamme_box = self.browser.find_element(By.NAME, "username")
    #     usernamme_box.send_keys('testuser123456')

    #     password_box = self.browser.find_element(By.NAME, "password")
    #     password_box.send_keys('password-123456')

    #     password_box.send_keys(Keys.ENTER)
    #     self.browser.quit()


    def test_add_subject(self):
        self.browser.get("http://localhost:8000/help/studytimetable")
        self.assertIn('ตารางเรียน', self.browser.title)  # check page is correct

        self.browser.get(url+"/help/settingtimetable")
        self.assertIn('ตั้งค่าตารางเรียน', self.browser.title)

        # 010113138 CIRCUITS AND ELECTRONICS3(3-0)
        search_box = self.browser.find_element(By.NAME, "search-subject")
        search_box.send_keys("010113138")  
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)
        add_btn = self.browser.find_element(By.NAME, "add_btn")
        add_btn.send_keys(Keys.ENTER)

        # 010123103 ALGORITHMS AND DATA STRUCTUR3(2-1)
        time.sleep(1)
        search_box = self.browser.find_element(By.NAME, "search-subject")
        search_box.send_keys("010123103")  
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)
        add_btn = self.browser.find_element(By.NAME, "add_btn")
        add_btn.send_keys(Keys.ENTER)

        # 010123118 COMPUTER NETWORKS3(3-0)
        time.sleep(1)
        search_box = self.browser.find_element(By.NAME, "search-subject")
        search_box.send_keys("010123118")  
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)
        add_btn = self.browser.find_element(By.NAME, "add_btn")
        add_btn.send_keys(Keys.ENTER)

        self.browser.get("http://localhost:8000/help/studytimetable")








if __name__ == '__main__':
    unittest.main()





