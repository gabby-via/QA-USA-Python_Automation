import data
import helpers
import time
from helpers import is_url_reachable
from helpers import retrieve_phone_code
from data import URBAN_ROUTES_URL
from selenium import webdriver
from selenium.webdriver.common.by import By

# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    ADDRESS_FROM = (By.ID, "from")
    ADDRESS_TO = (By.ID, "to")
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    TAXI_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/taxi-active.b0be3054.svg"]')
    CALL_TAXI_LOCATOR = (By.CLASS_NAME, 'button[class="button round"]')
    SUPPORTIVE_ICON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
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
    BLANKET_AND_HANDKERCHIEF_LOCATOR = (By.XPATH, '//div[@class="switch"]')
    ICE_CREAM_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    ORDER_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')


    def __init__(self, driver):
        self.driver = driver  # Initialize the driver


    def enter_from_location (self, from_text):
        self.driver.find_element(*self.ADDRESS_FROM).send_keys(from_text)

    def enter_to_location (self, to_text):
        self.driver.find_element(*self.ADDRESS_TO).send_keys(to_text)

    def click_custom_option (self):
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_taxi_option (self):
        self.driver.find_element(*self.TAXI_ICON_LOCATOR).click()

    def click_call_taxi_button (self):
       self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()

    def click_supportive_option (self):
        self.driver.find_element(*self.SUPPORTIVE_ICON_LOCATOR).click()

    def click_phone_number_option (self):
        self.driver.find_element(*self.PHONE_NUMBER_BOX).click()

    def enter_phone_number (self, number):
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(number)

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

    def click_link_button (self):
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def close_payment_box (self):
        self.driver.find_element(*self.CLOSE_PAYMENT_BOX).click()

    def message_to_driver (self, message):
        self.driver.find_element(*self.MESSAGE_FOR_DRIVER).send_keys(message)


    def select_blanket_and_handkerchief (self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEF_LOCATOR).click()

    def select_ice_cream (self):
        ice_cream = 0  # Declare a variable for the loop count
        while (ice_cream < 2):
            self.driver.find_element(*self.ICE_CREAM_LOCATOR).click()
            ice_cream = ice_cream + 1
            print(f'Select {ice_cream} ice creams')

    def click_order_button (self):
        self.driver.find_element(*self.ORDER_LOCATOR).click()
