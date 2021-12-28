#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException

# ...
BASE_URL = "http://localhost:8080/VALU3S"
def ensure_driver():
    '''Get Chrome/Firefox driver from Selenium Hub'''
    try:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(15)
    return driver


def before_all(context):
    context.driver = ensure_driver()
    context.base_url = "http://localhost:8080/VALU3S"


def after_all(context):
    context.driver.quit()