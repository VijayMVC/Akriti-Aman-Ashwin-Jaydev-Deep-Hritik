# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')


class CreateUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_user(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("Admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("password123")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_css_selector("h2").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_link_text("Add user").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("deep")
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("passcode")
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("passcode")
        driver.find_element_by_name("_save").click()
        driver.find_element_by_id("id_is_staff").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Log out").click()
        driver.find_element_by_link_text("Log in again").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("deep")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("passcode")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("View site").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
