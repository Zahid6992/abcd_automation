import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPurchasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoblaze.com/index.html"

        # define locators
        self.login_locator = (By.ID, "login2")
        self.username_locator = (By.ID, "loginusername")
        self.password_locator = (By.ID, "loginpassword")
        self.login_button_locator = (By.XPATH, "//button[contains(text(),'Log in')]")
        self.click_phone_locator = (By.XPATH, "//a[contains(text(),'Phones')]")
        self.click_laptop_locator = (By.ID, "//a[contains(text(),'Laptops')]")
        self.click_monitor_locator = (By.ID, "//a[contains(text(),'Monitors')]")
        self.goto_phone_details_locator = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")
        self.phone_add_to_card_locator = (By.XPATH, "//a[contains(text(),'Add to cart')]")
        self.got_home_locator = (By.ID, "nava")
        self.goto_laptop_dtails_locator = (By.XPATH, "//a[contains(text(),'Sony vaio i5')]")
        self.goto_cart_page_locator = (By.XPATH, "//a[contains(text(),'Cart')]")
        self.place_order = (By.ID, "//button[contains(text(),'Place Order')]")
        self.place_order_name = (By.ID, "name")
        self.place_order_country = (By.ID, "country")
        self.place_order_city = (By.ID, "city")
        self.place_order_card = (By.ID, "card")
        self.place_order_month = (By.ID, "month")
        self.place_order_year = (By.ID, "year")
        self.click_purchase = (By.XPATH, "//button[contains(text(),'Purchase')]")
        self.click_logout = (By.ID, "logout2")
        self.order_confirm = (By.XPATH, "//h2[contains(text(),'Thank you for your purchase!')]")




    def purchase(self):
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element(*self.login_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.username_locator).send_keys("zahid")
        time.sleep(2)
        self.driver.find_element(*self.password_locator).send_keys("1234qwer")
        time.sleep(2)
        self.driver.find_element(*self.login_button_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.click_phone_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.goto_phone_details_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.phone_add_to_card_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.got_home_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.click_laptop_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.phone_add_to_card_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.got_home_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.goto_phone_details_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.phone_add_to_card_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.got_home_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.goto_cart_page_locator).click()
        time.sleep(2)
        self.driver.find_element(*self.place_order).click()
        time.sleep(2)
        self.driver.find_element(*self.place_order_name).send_keys("zahid")
        time.sleep(2)
        self.driver.find_element(*self.place_order_country).send_keys("Bangladesh")
        time.sleep(2)
        self.driver.find_element(*self.place_order_city).send_keys("Dhaka")
        time.sleep(2)
        self.driver.find_element(*self.place_order_card).send_keys("67282182733")
        time.sleep(2)
        self.driver.find_element(*self.place_order_month).send_keys("Jun")
        time.sleep(2)
        self.driver.find_element(*self.place_order_year).send_keys("2023")
        time.sleep(2)
        self.driver.find_element(*self.click_purchase).click()
        time.sleep(2)
        comfirm_text = self.driver.find_element(*self.order_confirm).text
        expected_text = "Thank you for your purchase!"
        assert comfirm_text == expected_text, f"Text is not matching. Expected: {expected_text}, Actual: {comfirm_text}"
        time.sleep(2)
        self.driver.find_element(*self.click_logout).click()
        time.sleep(2)



