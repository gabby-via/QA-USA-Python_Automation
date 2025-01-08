import data
import helpers
import time
from helpers import is_url_reachable
from helpers import retrieve_phone_code
from data import URBAN_ROUTES_URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    ADDRESS_FROM = (By.ID, "from")
    ADDRESS_TO = (By.ID, "to")
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    TAXI_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/taxi-active.b0be3054.svg"]')
    CALL_TAXI_LOCATOR = (By.CLASS_NAME, 'button[class="button round"]')
    SUPPORTIVE_ICON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    PHONE_NUMBER_BOX = (By.XPATH, '//div[@class="np-text"]')
    PHONE_NUMBER = (By.ID, "phone")
    NEXT_BUTTON_LOCATOR = (By.CLASS_NAME, 'button[class="button full"]')
    SMS_CODE_LOCATOR = (By.ID, "code")
    CONFIRM_ICON_LOCATOR = (By.XPATH, '//div[@class="buttons"]/button[@type="submit" and contains(text(),"Confirm")]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-text"]')
    ADD_CARD_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]')
    CARD_NUMBER = (By.ID, "number")
    CARD_CODE = (By.NAME, "code")
    LINK_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    CLOSE_PAYMENT_BOX = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    MESSAGE_FOR_DRIVER = (By.ID, "comment")
    BLANKET_AND_HANDKERCHIEF_LOCATOR = (By.CLASS_NAME, 'switch')
    OPTION_SWITCHES_INPUTS = (By.CLASS_NAME, 'switch-input')
    ICE_CREAM_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    ICE_CREAM_VALUE = (By.XPATH, '//div[@class="counter-value"]')
    ORDER_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
    ORDER_POPUP = (By.XPATH, '//div[@class="order-body"]')


    def __init__(self, driver):
        self.driver = driver  # Initialize the driver


    def enter_from_location (self, from_text):
        self.driver.find_element(*self.ADDRESS_FROM).send_keys(from_text)

    def enter_to_location (self, to_text):
        self.driver.find_element(*self.ADDRESS_TO).send_keys(to_text)

    def get_from_location (self):
        return self.driver.find_element(*self.ADDRESS_FROM).get_attribute("value")

    def get_to_location (self):
        return self.driver.find_element(*self.ADDRESS_TO).get_attribute("value")

    def click_custom_option (self):
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_taxi_option (self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.TAXI_ICON_LOCATOR))
        self.driver.find_element(*self.TAXI_ICON_LOCATOR).click()

    def click_call_taxi_button (self):
       self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()

    def click_supportive_option (self):
        self.driver.find_element(*self.SUPPORTIVE_ICON_LOCATOR).click()

    def get_supportive_option (self):
        return self.driver.find_element(*self.SUPPORTIVE_ICON_LOCATOR).get_attribute("class")

    def click_phone_number_option (self):
        self.driver.find_element(*self.PHONE_NUMBER_BOX).click()

    def enter_phone_number (self, number):
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(number)

    def get_phone_number (self):
        return self.driver.find_element(*self.PHONE_NUMBER).get_attribute("value")

    def click_next_button (self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def sms_code (self, sms):
        self.driver.find_element(*self.SMS_CODE_LOCATOR).send_keys(sms)


    def click_confirm_button (self):
        self.driver.find_element(*self.CONFIRM_ICON_LOCATOR).click()

    def click_payment_method (self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def click_add_card (self):
        self.driver.find_element(*self.ADD_CARD_BUTTON_LOCATOR).click()

    def adding_a_card (self, card_number, verification_id):
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_number)
        self.driver.find_element(*self.CARD_CODE).send_keys(verification_id)

    def get_card_number (self):
        return self.driver.find_element(*self.CARD_NUMBER).get_attribute("value")

    def get_card_code (self):
        return self.driver.find_element(*self.CARD_CODE).get_attribute("value")

    def click_link_button (self):
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def close_payment_box (self):
        self.driver.find_element(*self.CLOSE_PAYMENT_BOX).click()

    def message_to_driver (self, message):
        self.driver.find_element(*self.MESSAGE_FOR_DRIVER).send_keys(message)

    def get_message_to_driver (self):
        return self.driver.find_element(*self.MESSAGE_FOR_DRIVER).get_attribute("value")

    def select_blanket_and_handkerchief (self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEF_LOCATOR).click()

    def get_blanket_and_handkerchief (self):
        return self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEF_LOCATOR).get_attribute("class")

    def get_switches (self):
        switches = self.driver.find_elements(*self.OPTION_SWITCHES_INPUTS)
        return switches[0].get_property("checked")

    def select_ice_cream (self):
        ice_cream = 0  # Declare a variable for the loop count
        while (ice_cream < 2):
            self.driver.find_element(*self.ICE_CREAM_LOCATOR).click()
            ice_cream = ice_cream + 1
            print(f'Select {ice_cream} ice creams')
        selected_ice_creams = self.ice_cream_value()
        assert selected_ice_creams == 2, f"Expected 2 ice creams, but got {selected_ice_creams}"

    def get_ice_cream (self):
        return self.driver.find_element(*self.ICE_CREAM_LOCATOR).get_attribute("class")

    def ice_cream_value (self):
        value = self.driver.find_element(*self.ICE_CREAM_VALUE).text
        return int(value)

    def click_order_button (self):
        self.driver.find_element(*self.ORDER_LOCATOR).click()

    def get_order_button (self):
        return self.driver.find_element(*self.ORDER_LOCATOR).get_attribute("class")

    def order_pop_up (self):
        return self.driver.find_element(*self.ORDER_POPUP).is_displayed()
