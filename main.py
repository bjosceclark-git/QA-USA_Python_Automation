import data
from helpers import retrieve_phone_code
from data import MESSAGE_FOR_DRIVER
from pages import UrbanRoutesPage
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if is_url_reachable(data.URBAN_ROUTES_URL) is True:
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["google:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        WebDriverWait(cls.driver, 3)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        to_actual_value = urban_routes_page.verify_to_location()
        to_expected_value = data.ADDRESS_TO
        assert to_actual_value in to_expected_value, f"Expected {to_expected_value} but found {to_actual_value}"
        from_actual_value = urban_routes_page.verify_from_location()
        from_expected_value = data.ADDRESS_FROM
        assert from_actual_value in from_expected_value, f"Expected {from_expected_value} but found {from_actual_value}"

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.getting_to_taxi_menu(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        actual_value = urban_routes_page.get_active_plan_title()
        expected_value = "Supportive"
        assert actual_value in expected_value, f"Expected {expected_value} but found {actual_value}"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.getting_to_taxi_menu(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.phone_number_testing(data.PHONE_NUMBER)
        time.sleep(1)
        #phone_code = retrieve_phone_code(self.driver)
        #print(phone_code)
        urban_routes_page.phone_code_testing(retrieve_phone_code(self.driver))
        actual_value = urban_routes_page.verify_phone_number_confirmed()
        expected_value = data.PHONE_NUMBER
        assert actual_value in expected_value, f"Expected {expected_value} but found {actual_value}"

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.getting_to_taxi_menu(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.card_testing(data.CARD_NUMBER, data.CARD_CODE)
        actual_value = urban_routes_page.verify_card_submission()
        expected_value = "Card One"
        assert actual_value in expected_value, f"Expected {expected_value} but found {actual_value}"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.getting_to_taxi_menu(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.comment_to_driver(data.MESSAGE_FOR_DRIVER)
        actual_value = urban_routes_page.check_driver_message()
        expected_value = data.MESSAGE_FOR_DRIVER
        assert actual_value in expected_value, f"Expected {expected_value} but found {actual_value}"

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.getting_to_taxi_menu(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.blanket_and_handkerchiefs_order()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.getting_to_taxi_menu(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.ice_creams_test(2)
        actual_value = urban_routes_page.ice_creams_check()
        expected_value = "2"
        assert actual_value in expected_value, f"Expected {expected_value} but found {actual_value}"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.getting_to_taxi_menu(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        urban_routes_page.comment_to_driver(MESSAGE_FOR_DRIVER)
        time.sleep(2)
        urban_routes_page.click_order_taxi()
        time.sleep(40)
        actual_value = urban_routes_page.verify_taxi_arrival()
        expected_value = "The driver will arrive"
        assert actual_value in expected_value, f"Expected {expected_value} but found {actual_value}"


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()