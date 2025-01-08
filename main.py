from selenium.webdriver.common.by import By
import data
import helpers
import pages
import time
from pages import UrbanRoutesPage
from helpers import is_url_reachable, retrieve_phone_code
from data import URBAN_ROUTES_URL, CARD_CODE
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class TestUrbanRoutes:
    @classmethod
    def setup_class (cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if is_url_reachable(data.URBAN_ROUTES_URL):
            #task4
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")
            exit () #exit the program if the server cannot connect

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage (self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_option()
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        assert urban_routes_page.get_from_location() == data.ADDRESS_FROM
        assert urban_routes_page.get_to_location() == data.ADDRESS_TO

    def test_select_plan (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.click_supportive_option()
        time.sleep(2)
        assert urban_routes_page.get_supportive_option() == "tcard active"


    def test_fill_phone_number (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.click_supportive_option()
        urban_routes_page.click_phone_number_option()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.sms_code(sms_code)
        time.sleep(2)
        assert urban_routes_page.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.click_supportive_option()
        urban_routes_page.click_phone_number_option()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms_code = helpers.retrieve_phone_code(self.driver)
        time.sleep(2)
        urban_routes_page.sms_code(sms_code)
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.adding_a_card(data.CARD_NUMBER, data.CARD_CODE)
        self.driver.implicitly_wait(3)
        urban_routes_page.click_link_button()
        urban_routes_page.close_payment_box()
        time.sleep(2)
        assert urban_routes_page.get_card_number() == data.CARD_NUMBER
        assert urban_routes_page.get_card_code() == data.CARD_CODE

    def test_comment_for_driver (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.click_supportive_option()
        urban_routes_page.click_phone_number_option()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.sms_code(sms_code)
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.adding_a_card(data.CARD_NUMBER, data.CARD_CODE)
        self.driver.implicitly_wait(3)
        urban_routes_page.click_link_button()
        urban_routes_page.close_payment_box()
        urban_routes_page.message_to_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        assert urban_routes_page.get_message_to_driver() == data.MESSAGE_FOR_DRIVER


    def test_order_blanket_and_handkerchiefs (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage (self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.click_supportive_option()
        urban_routes_page.click_phone_number_option()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.sms_code(sms_code)
        urban_routes_page.click_confirm_button()
        time.sleep(2)
        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.adding_a_card(data.CARD_NUMBER, data.CARD_CODE)
        self.driver.implicitly_wait(3)
        urban_routes_page.click_link_button()
        urban_routes_page.close_payment_box()
        urban_routes_page.message_to_driver(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.select_blanket_and_handkerchief()
        time.sleep(2)
        status = urban_routes_page.get_switches()
        assert urban_routes_page.get_blanket_and_handkerchief() == "switch"
        assert urban_routes_page.get_switches()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.click_supportive_option()
        urban_routes_page.click_phone_number_option()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.sms_code(sms_code)
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.adding_a_card(data.CARD_NUMBER, data.CARD_CODE)
        self.driver.implicitly_wait(3)
        urban_routes_page.click_link_button()
        urban_routes_page.close_payment_box()
        urban_routes_page.message_to_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_routes_page.select_blanket_and_handkerchief()
        urban_routes_page.select_ice_cream()
        time.sleep(2)
        assert urban_routes_page.get_ice_cream() == "counter-plus disabled"
        assert urban_routes_page.ice_cream_value() == 2

    def test_car_search_model_appears (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_taxi_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.click_supportive_option()
        urban_routes_page.click_phone_number_option()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.sms_code(sms_code)
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.adding_a_card(data.CARD_NUMBER, data.CARD_CODE)
        self.driver.implicitly_wait(3)
        urban_routes_page.click_link_button()
        urban_routes_page.close_payment_box()
        urban_routes_page.message_to_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_routes_page.select_blanket_and_handkerchief()
        urban_routes_page.select_ice_cream()
        urban_routes_page.click_order_button()
        time.sleep(2)
        assert urban_routes_page.get_order_button() == "smart-button"
        assert urban_routes_page.order_pop_up(), "Order popup was not displayed after clicking the order button"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()