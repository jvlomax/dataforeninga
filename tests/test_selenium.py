from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
from flask import url_for

from main import app
import requests
from threading import Thread

class MyTest(TestCase):

    @classmethod
    def setUpClass(cls):
            app.config["DEBUG"] = False
            #app.config["TESTING"] = True

            cls.thread = Thread(target=app.run, name="app", daemon=True)
            cls.thread.start()
    def setUp(self):
        self.driver = webdriver.Firefox()


    def tearDown(self):
        self.driver.quit()

    def test_server_running(self):
        print("here")
        #driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:5000/index.html")
        assert self.driver.title == "Tromsøstudentenes Dataforening"
    def test_menu(self):
        self.driver.get("http://127.0.0.1:5000/")
       # contact_link = self.driver.find_element_by_link_text("Kontakt Oss")
        board_link = self.driver.find_element_by_link_text("Styret")
       # home_link = self.driver.find_element_by_link_text("Hjem")
        board_link.click()


