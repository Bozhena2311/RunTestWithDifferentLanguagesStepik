import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_website_contains_add_to_cart_button(browser):

    browser.get(link)

    time.sleep(10)
    
    assert browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
