import data
import helpers
from helpers import is_url_reachable


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if is_url_reachable(data.URBAN_ROUTES_URL) is True:
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_set_route(self):
        # Add in S8
        print('function created for set route')
        pass

    def test_select_plan(self):
        # Add in S8
        print('function created for select plan')
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print('function created for fill phone number')
        pass

    def test_fill_card(self):
        # Add in S8
        print('function created for fill card')
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print('function created for comment for driver')
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print('function created for order blanket and handkerchiefs')
        pass

    def test_order_2_ice_creams(self):
        print('function created for order 2 and ice creams')
        for () in ():
            range(2)
            pass
            # add in S8

    def test_car_search_model_appears(self):
        # Add in S8
        print('function created for car search model')
        pass
