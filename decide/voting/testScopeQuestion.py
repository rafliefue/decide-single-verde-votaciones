import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTestScopeQuestion(StaticLiveServerTestCase):
  # def setup_method(self, method):
  #   self.driver = webdriver.Chrome()
  #   self.vars = {}
  
  # def teardown_method(self, method):
  #   self.driver.quit()
  
  def setUp(self):
    #Load base test functionality for decide
    self.usernameDecide = 'admin'
    self.passwordDecide = 'adminpass'
    self.base = BaseTestCase()
    self.base.setUp()

    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    super().setUp()

  def tearDown(self):
    super().tearDown()
    self.driver.quit()

    self.base.tearDown()

  def test_testScopeQuestion(self):
    self.driver.get("http://localhost:8000/admin/login/?next=/admin/")
    self.driver.set_window_size(957, 727)
    self.driver.find_element(By.ID, "id_username").send_keys(self.usernameDecide)
    self.driver.find_element(By.ID, "id_password").send_keys(self.passwordDecide)
    self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
    self.driver.find_element(By.LINK_TEXT, "Questions").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_desc").send_keys("Â¿SerÃ­as capaz de mentir a la cara?")
    self.driver.find_element(By.ID, "id_scopes").click()
    dropdown = self.driver.find_element(By.ID, "id_scopes")
    dropdown.find_element(By.XPATH, "//option[. = 'Other']").click()
    self.driver.find_element(By.ID, "id_scopes").click()
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    self.driver.find_element(By.ID, "id_options-1-number").click()
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("Si")
    self.driver.find_element(By.ID, "id_options-1-option").click()
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("No")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_desc").send_keys("Â¿CÃ³mo se llamaba el cantante de Queen?")
    self.driver.find_element(By.ID, "id_scopes").click()
    dropdown = self.driver.find_element(By.ID, "id_scopes")
    dropdown.find_element(By.XPATH, "//option[. = 'Entertainment']").click()
    self.driver.find_element(By.ID, "id_scopes").click()
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("0")
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("2")
    self.driver.find_element(By.ID, "id_options-0-number").click()
    element = self.driver.find_element(By.ID, "id_options-0-number")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-1-number").click()
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    self.driver.find_element(By.ID, "id_options-2-number").click()
    self.driver.find_element(By.ID, "id_options-2-number").send_keys("3")
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("Freddy Mercury")
    self.driver.find_element(By.ID, "id_options-1-option").click()
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("Melendi")
    self.driver.find_element(By.ID, "id_options-2-option").click()
    self.driver.find_element(By.ID, "id_options-2-option").send_keys("El Koala")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_desc").click()
    self.driver.find_element(By.ID, "id_desc").send_keys("Â¿CuÃ¡l es el Ãºnico mamÃ­fero capaz de poner huevos?")
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    self.driver.find_element(By.ID, "id_options-1-number").click()
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    self.driver.find_element(By.ID, "id_options-2-number").click()
    self.driver.find_element(By.ID, "id_options-2-number").send_keys("3")
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("LeÃ³n")
    self.driver.find_element(By.ID, "id_options-1-option").click()
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("Ballena")
    self.driver.find_element(By.ID, "id_options-2-option").click()
    self.driver.find_element(By.ID, "id_options-2-option").send_keys("Ornitorrinco")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row1:nth-child(1) a").click()
    self.driver.find_element(By.ID, "id_scopes").click()
    dropdown = self.driver.find_element(By.ID, "id_scopes")
    dropdown.find_element(By.XPATH, "//option[. = 'Science']").click()
    self.driver.find_element(By.ID, "id_scopes").click()
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_desc").send_keys("Â¿A quÃ© equipo pertenece el jugador Ferran Torres?")
    self.driver.find_element(By.ID, "id_scopes").click()
    dropdown = self.driver.find_element(By.ID, "id_scopes")
    dropdown.find_element(By.XPATH, "//option[. = 'Sports']").click()
    self.driver.find_element(By.ID, "id_scopes").click()
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    self.driver.find_element(By.ID, "id_options-1-number").click()
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    self.driver.find_element(By.ID, "id_options-2-number").click()
    self.driver.find_element(By.ID, "id_options-2-number").send_keys("3")
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("Osasuna")
    self.driver.find_element(By.ID, "id_options-1-option").click()
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("Manchester City")
    self.driver.find_element(By.ID, "id_options-2-option").click()
    self.driver.find_element(By.ID, "id_options-2-option").send_keys("PSG")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_desc").send_keys("Â¿En que aÃ±o se descubriÃ³ AmÃ©rica?")
    self.driver.find_element(By.ID, "id_scopes").click()
    dropdown = self.driver.find_element(By.ID, "id_scopes")
    dropdown.find_element(By.XPATH, "//option[. = 'History']").click()
    self.driver.find_element(By.ID, "id_scopes").click()
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    self.driver.find_element(By.ID, "id_options-1-number").click()
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    self.driver.find_element(By.ID, "id_options-2-number").click()
    self.driver.find_element(By.ID, "id_options-2-number").send_keys("3")
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("1236")
    self.driver.find_element(By.ID, "id_options-1-option").click()
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("1492")
    self.driver.find_element(By.ID, "id_options-2-option").click()
    self.driver.find_element(By.ID, "id_options-2-option").send_keys("1831")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_desc").send_keys("Â¿QuiÃ©n escribio el libro donde se narraban las aventuras de Don Quijote?")
    self.driver.find_element(By.ID, "id_scopes").click()
    dropdown = self.driver.find_element(By.ID, "id_scopes")
    dropdown.find_element(By.XPATH, "//option[. = 'Literature']").click()
    self.driver.find_element(By.ID, "id_scopes").click()
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    self.driver.find_element(By.ID, "id_options-1-number").click()
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    self.driver.find_element(By.ID, "id_options-2-number").click()
    self.driver.find_element(By.ID, "id_options-2-number").send_keys("3")
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("Unamuno")
    self.driver.find_element(By.ID, "id_options-1-option").click()
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("Cervantes")
    self.driver.find_element(By.ID, "id_options-2-option").click()
    self.driver.find_element(By.ID, "id_options-2-option").send_keys("GarcÃ­a Lorca")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_desc").send_keys("Â¿En quÃ© continente estÃ¡ situada Madrid?")
    self.driver.find_element(By.ID, "id_scopes").click()
    dropdown = self.driver.find_element(By.ID, "id_scopes")
    dropdown.find_element(By.XPATH, "//option[. = 'Geography']").click()
    self.driver.find_element(By.ID, "id_scopes").click()
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    self.driver.find_element(By.ID, "id_options-1-number").click()
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    self.driver.find_element(By.ID, "id_options-2-number").click()
    self.driver.find_element(By.ID, "id_options-2-number").send_keys("3")
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("Asia")
    self.driver.find_element(By.ID, "id_options-1-option").click()
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("Europa")
    self.driver.find_element(By.ID, "id_options-2-option").click()
    self.driver.find_element(By.ID, "id_options-2-option").send_keys("Ã�frica")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.LINK_TEXT, "Literature").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").click()
    self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").text == "Literature")
    self.driver.find_element(By.LINK_TEXT, "Entertainment").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").click()
    self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").text == "Entertainment")
    self.driver.find_element(By.LINK_TEXT, "Geography").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").click()
    self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").text == "Geography")
    self.driver.find_element(By.LINK_TEXT, "History").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").click()
    self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").text == "History")
    self.driver.find_element(By.LINK_TEXT, "Science").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").click()
    self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").text == "Science")
    self.driver.find_element(By.LINK_TEXT, "Sports").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").click()
    self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").text == "Sports")
    self.driver.find_element(By.LINK_TEXT, "Other").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").click()
    self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".field-scopes").text == "Other")
    self.driver.find_element(By.LINK_TEXT, "All").click()
    self.driver.find_element(By.ID, "action-toggle").click()
    self.driver.find_element(By.NAME, "action").click()
    dropdown = self.driver.find_element(By.NAME, "action")
    dropdown.find_element(By.XPATH, "//option[. = 'Delete selected questions']").click()
    self.driver.find_element(By.NAME, "action").click()
    self.driver.find_element(By.NAME, "index").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4)").click()

