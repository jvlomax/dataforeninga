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


    def test_menu(self):
        self.driver.get("http://127.0.0.1:5000/")
        assert self.driver.title == "Tromsøstudentenes Dataforening | Hjem"
        board_link = self.driver.find_element_by_link_text("Styret")
        board_link.click()
        assert self.driver.title == "Tromsøstudentenes Dataforening | Styret"
        about_link = self.driver.find_element_by_link_text("Om oss")
        about_link.click()
        assert self.driver.title == "Tromsøstudentenes Dataforening | Om oss"
        contact_link = self.driver.find_element_by_link_text("Kontakt oss")
        contact_link.click()
        assert self.driver.title == "Tromsøstudentenes Dataforening | Kontakt oss"
        home_link = self.driver.find_element_by_link_text("Hjem")
        home_link.click()
        assert self.driver.title == "Tromsøstudentenes Dataforening | Hjem"

  #  def test_styret(self):


   # def test_about(self):


#    def test_contact(self):

