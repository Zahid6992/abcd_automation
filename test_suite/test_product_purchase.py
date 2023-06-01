import pytest
import os
import sys
from selenium import webdriver
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.product_purchase_page import ProductPurchasePage


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome("C://Users//Md. Zahid Hasan//Downloads//chromedriver_win32 (4)")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_purchase(driver):
    product_purchase = ProductPurchasePage(driver)
    product_purchase.purchase()