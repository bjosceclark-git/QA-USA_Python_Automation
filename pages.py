from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class UrbanRoutesPage:
    WHERE_FROM = (By.ID, 'from')
    WHERE_TO = (By.ID, 'to')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[@class="button round"]')
    SUPPORTIVE_TARIFF = (By.XPATH, '//div[text()="Supportive"]')
    SUPPORTIVE_TARIFF_ACTIVE = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    PHONE_NUMBER_BUTTON = (By.XPATH, '//div[@class="np-text"]')
    PHONE_NUMBER_INPUT = (By.ID, 'phone')
    PHONE_NUMBER_SUBMIT = (By.XPATH, '//button[text()="Next"]')
    PHONE_CODE_INPUT = (By.ID, 'code')
    PHONE_CODE_RESEND = (By.XPATH, '//div[@class="buttons"]//button[text()="Send the code again"]')
    PHONE_CODE_SUBMIT = (By.XPATH, '//div[@class="buttons"]//button[text()="Confirm"]')
    ADD_PAYMENT = (By.XPATH, '//div[@class="pp-button filled"]')
    ADD_CARD = (By.XPATH, '//div[@class="pp-row disabled"]//div[@class="pp-title"]')
    CARD_NUMBER_INPUT = (By.CSS_SELECTOR, 'div.card-number input#number')
    CARD_CODE_INPUT = (By.CSS_SELECTOR, 'div.card-code input#code')
    TITLE = (By.XPATH, '//div[text()="Adding a card"]')
    CARD_LINK_BUTTON = (By.XPATH, '//div[@class="pp-buttons"]//button[text()="Link"]')
    CARD_OPTION = (By.XPATH, '//div[@class="section active"]//div[text()="Card"]')
    DRIVER_COMMENT = (By.CLASS_NAME, 'pp-title')
    ORDER_SWITCHES = (By.CLASS_NAME, 'r-sw')
    ORDER_SWITCHES_CHECKER = (By.CSS_SELECTOR, '.switch-input')
    ADD_COUNTER = (By.CLASS_NAME, 'counter-plus')
    COUNTER_AMOUNT = (By.CLASS_NAME, 'counter-value')
    ORDER_TAXI = (By.CLASS_NAME, 'smart-button')
    ORDER_SUCCESS_VERIFICATION = (By.CLASS_NAME, 'order-body')
    COMMENT_TO_DRIVER = (By.ID, "comment")

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.WHERE_FROM).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.WHERE_TO).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def verify_to_location(self):
        return self.driver.find_element(*self.WHERE_TO).text

    def verify_from_location(self):
        return self.driver.find_element(*self.WHERE_FROM).text

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.CALL_TAXI_BUTTON)).click()

    def get_active_plan_title(self):
        return self.driver.find_element(*self.SUPPORTIVE_TARIFF_ACTIVE).text

    def check_supportive_tariff(self):
        if self.get_active_plan_title() == 'Supportive':
            pass
        else:
            self.driver.find_element(*self.SUPPORTIVE_TARIFF).click()

    def getting_to_taxi_menu(self, from_text, to_text):
        self.enter_locations(from_text, to_text)
        self.click_call_taxi_button()
        self.check_supportive_tariff()

    def click_phone_number(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone_number)

    def submit_phone_number(self):
        self.driver.find_element(*self.PHONE_NUMBER_SUBMIT).click()

    def phone_number_testing(self, phone_number):
        self.click_phone_number()
        self.enter_phone_number(phone_number)
        self.submit_phone_number()

    def resend_phone_code(self):
        self.driver.find_element(*self.PHONE_CODE_RESEND).click()

    def enter_phone_code(self, phone_code):
        self.driver.find_element(*self.PHONE_CODE_INPUT).send_keys(phone_code)

    def click_phone_code_submit(self):
        self.driver.find_element(*self.PHONE_CODE_SUBMIT).click()

    def verify_phone_number_confirmed(self):
        return self.driver.find_element(*self.PHONE_NUMBER_BUTTON).text

    def phone_code_testing(self, phone_code):
        self.enter_phone_code(phone_code)
        self.click_phone_code_submit()
        self.verify_phone_number_confirmed()

    def click_add_payment(self):
        self.driver.find_element(*self.ADD_PAYMENT).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD).click()

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)

    def enter_card_code(self, card_code):
        self.driver.find_element(*self.CARD_CODE_INPUT).send_keys(card_code)

    def click_title(self):
        self.driver.find_element(*self.TITLE).click()

    def submit_card_info(self):
        self.driver.find_element(*self.CARD_LINK_BUTTON).click()

    def verify_card_submission(self):
        return self.driver.find_element(*self.CARD_OPTION).text

    def card_testing(self, card_number, card_code):
        self.click_add_payment()
        self.click_add_card()
        self.enter_card_number(card_number)
        self.enter_card_code(card_code)
        self.click_title()
        self.submit_card_info()
        self.verify_card_submission()

    def blanket_and_handkerchiefs_order(self):
        self.driver.find_element(*self.ORDER_SWITCHES).click()

    def get_blanket_and_handkerchiefs_option_checked(self):
        switch = self.driver.find_element(*self.ORDER_SWITCHES_CHECKER)
        return switch.get_property('checked')

    def test_blanket_and_handkerchiefs_order(self):
        self.blanket_and_handkerchiefs_order()

    def ice_creams_add(self, loops):
        for counter_add in range(loops):
            self.driver.find_element(*self.ADD_COUNTER).click()

    def ice_creams_check(self):
        return self.driver.find_element(*self.COUNTER_AMOUNT).text

    def ice_creams_test(self, loops):
        self.ice_creams_add(loops)
        self.ice_creams_check()

    def click_order_taxi(self):
        self.driver.find_element(*self.ORDER_TAXI).click()

    def verify_taxi_arrival(self):
        return self.driver.find_element(*self.ORDER_SUCCESS_VERIFICATION).is_displayed()

    def comment_to_driver(self, comment):
        self.driver.find_element(*self.COMMENT_TO_DRIVER).send_keys(comment)

    def check_driver_message(self):
        return self.driver.find_element(*self.COMMENT_TO_DRIVER).get_attribute("value")