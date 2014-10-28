from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
from flask import url_for
import configs
from main import app, db
import requests
from threading import Thread

class MyTest(TestCase):

    @classmethod
    def setUpClass(cls):
            app.config.from_object(configs.TestConfig)
            #db.create_all()
            #app.config["TESTING"] = True
            cls.server_address = "127.0.0.1:3664"
            app.config["SERVER_NAME"] = cls.server_address
            cls.thread = Thread(target=app.run, name="app", daemon=True)
            cls.thread.start()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        print("before create all")
        db.create_all()
        print("after create all")
    def tearDown(self):
        self.driver.quit()
        db.drop_all()

    def test_menu(self):
        print(self.server_address)
        self.driver.get("http://{}".format(self.server_address))
        print(self.driver.title)
        assert self.driver.title == "Tromsøstudentenes Dataforening | Hjem"
        board_link = self.driver.find_element_by_link_text("Styret")
        board_link.click()
        print(self.driver.title)

        assert self.driver.title == "Tromsøstudentenes Dataforening | Styret"
        about_link = self.driver.find_element_by_link_text("Om oss")
        about_link.click()
        print(self.driver.title)
        assert self.driver.title == "Tromsøstudentenes Dataforening | Om oss"
        contact_link = self.driver.find_element_by_link_text("Kontakt oss")
        contact_link.click()
        print(self.driver.title)
        assert self.driver.title == "Tromsøstudentenes Dataforening | Kontakt oss"
        home_link = self.driver.find_element_by_link_text("Hjem")
        home_link.click()
        print(self.driver.title)
        assert self.driver.title == "Tromsøstudentenes Dataforening | Hjem"

  #  def test_styret(self):


   # def test_about(self):


#    def test_contact(self):
"""
    def test_member(self):
        self.driver.get("http://{}/{}".format(self.server_address, "dashboard/members.html"))
        #self.driver.get("http://{}".format(self.server_address))
        add_member_button = self.driver.find_element_by_id("addMemberBtn")
        add_member_button.click()
        modal_element = self.driver.find_element_by_id("newMemberModal")
        modal = self.driver.switch_to.frame(modal_element)

        f_nameInput = modal.find_element_by_id("firstNameInput")
        print(f_nameInput)
        l_nameInput = modal.find_element_by_id("lastNameInput")
        positionSelect = modal.find_element_by_id("positionSelect")
        f_nameInput.click()
        f_nameInput.send_keys("John")
        l_nameInput.send_keys("Doe")

"""