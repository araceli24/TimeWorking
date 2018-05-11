from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from django.contrib.auth.models import User
from selenium.webdriver.firefox.options import Options
import pytest
#def test_example (selenium, live_server):
 #   selenium.get(live_server.url)
  #  import time; time.sleep(3)

# def test_site_login(selenium, live_server):
#      driver=selenium.get(live_server.url)


@pytest.fixture(scope='module')
def browser(request):
    options = Options()
    #options.add_argument('-headless')
    browser_ = webdriver.Firefox(firefox_options=options)
    yield browser_
    browser_.quit()

  
@pytest.mark.django_db
def test_login(browser, live_server):
  User.objects.create_user(username='Ara', password='adminadmin')
  browser.get(live_server.url)
  username=browser.find_element_by_name("username")
  password=browser.find_element_by_name("password")

  username.send_keys("Ara")
  password.send_keys("adminadmin")

  browser.find_element_by_name("btnSubmit").click()
  browser.find_element_by_name("project_new").click()

  name=browser.find_element_by_id("id_name")
  select=Select(browser.find_element_by_name('user'))
  description=browser.find_element_by_id("id_description")

  name.send_keys("NESTLE")
 
  select.select_by_value('1')
  description.send_keys("Chocolate de calidad")
  browser.find_element_by_id("btnSave").click()
  browser.find_element_by_id("inicio").click()


  
