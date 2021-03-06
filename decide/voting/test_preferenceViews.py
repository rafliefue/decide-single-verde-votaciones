from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from base.tests import BaseTestCase


class TestPreferenceViews():
  # def setup_method(self, method):
  #   self.driver = webdriver.Chrome()
  #   self.vars = {}
  
  # def teardown_method(self, method):
  #   self.driver.quit()
  def setUp(self):
    #Load base test functionality for decide
    self.base = BaseTestCase()
    self.base.setUp()
    self.usernameDecide = 'admin'
    self.passwordDecide = 'adminpass'

    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    super().setUp()

  def tearDown(self):

    super().tearDown()
    self.driver.quit()

    self.base.tearDown()

  def test_preferenceViews2(self):
    self.driver.get("http://localhost:8000/admin/")
    self.driver.set_window_size(957, 727)
    self.driver.find_element(By.ID, "id_username").send_keys(self.usernameDecide)
    self.driver.find_element(By.ID, "id_password").send_keys(self.passwordDecide)
    self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
    self.driver.find_element(By.LINK_TEXT, "Votings").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("High")
    self.driver.find_element(By.ID, "id_themeVotation").click()
    dropdown = self.driver.find_element(By.ID, "id_themeVotation")
    dropdown.find_element(By.XPATH, "//option[. = 'Testing']").click()
    self.driver.find_element(By.ID, "id_themeVotation").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_question")
    dropdown.find_element(By.XPATH, "//option[. = '¿Es david cervantes?']").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_auths")
    dropdown.find_element(By.XPATH, "//option[. = 'http://localhost:8000']").click()
    self.driver.find_element(By.NAME, "_save").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    self.assertTrue(selected_text == "---------")
    self.driver.find_element(By.ID, "id_preference").click()
    dropdown = self.driver.find_element(By.ID, "id_preference")
    dropdown.find_element(By.XPATH, "//option[. = 'High']").click()
    self.driver.find_element(By.ID, "id_preference").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    self.assertTrue(selected_text == "High")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("Mid")
    self.driver.find_element(By.CSS_SELECTOR, ".field-name").click()
    self.driver.find_element(By.ID, "id_themeVotation").click()
    dropdown = self.driver.find_element(By.ID, "id_themeVotation")
    dropdown.find_element(By.XPATH, "//option[. = 'Testing']").click()
    self.driver.find_element(By.ID, "id_themeVotation").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_question")
    dropdown.find_element(By.XPATH, "//option[. = '¿Es david cervantes?']").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_auths")
    dropdown.find_element(By.XPATH, "//option[. = 'http://localhost:8000']").click()
    self.driver.find_element(By.NAME, "_save").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    self.assertTrue(selected_text == "---------")
    self.driver.find_element(By.ID, "id_preference").click()
    dropdown = self.driver.find_element(By.ID, "id_preference")
    dropdown.find_element(By.XPATH, "//option[. = 'Mid']").click()
    self.driver.find_element(By.ID, "id_preference").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    self.assertTrue(selected_text == "Mid")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("Low")
    self.driver.find_element(By.ID, "id_themeVotation").click()
    dropdown = self.driver.find_element(By.ID, "id_themeVotation")
    dropdown.find_element(By.XPATH, "//option[. = 'Testing']").click()
    self.driver.find_element(By.ID, "id_themeVotation").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_question")
    dropdown.find_element(By.XPATH, "//option[. = '¿Es david cervantes?']").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_auths")
    dropdown.find_element(By.XPATH, "//option[. = 'http://localhost:8000']").click()
    self.driver.find_element(By.NAME, "_save").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    self.assertTrue(selected_text == "---------")
    self.driver.find_element(By.ID, "id_preference").click()
    dropdown = self.driver.find_element(By.ID, "id_preference")
    dropdown.find_element(By.XPATH, "//option[. = 'Low']").click()
    self.driver.find_element(By.ID, "id_preference").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    self.assertTrue(selected_text == "Low")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.LINK_TEXT, "High").click()
    self.assertTrue(self.driver.find_element(By.LINK_TEXT, "High").text == "High")
    self.driver.find_element(By.LINK_TEXT, "Mid").click()
    self.assertTrue(self.driver.find_element(By.LINK_TEXT, "Mid").text == "Mid")
    self.driver.find_element(By.LINK_TEXT, "Low").click()
    self.assertTrue(self.driver.find_element(By.LINK_TEXT, "Low").text == "Low")
    self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(7) > li:nth-child(1) > a").click()
    self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(7) > .selected > a").text == "All")
    self.driver.find_element(By.NAME, "_selected_action").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row2:nth-child(2) .action-select").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row1:nth-child(3) .action-select").click()
    self.driver.find_element(By.NAME, "action").click()
    dropdown = self.driver.find_element(By.NAME, "action")
    dropdown.find_element(By.XPATH, "//option[. = 'Delete selected votings']").click()
    self.driver.find_element(By.NAME, "action").click()
    self.driver.find_element(By.NAME, "index").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(6)").click()
  
