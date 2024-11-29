import data
import helpers
from helpers import is_url_reachable
from data import URBAN_ROUTES_URL


class TestUrbanRoutes:
    @classmethod
    def setup_class (cls):
        if is_url_reachable(URBAN_ROUTES_URL):
            #task4
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")
            exit () #exit the program if the server cannot connect

    def test_set_route(self):
     # Add in S8
        print("Function created for set route")
        pass  # placeholder for future implementation


    def test_select_plan (self):
     # Add in S8
        print("Function created for set route")
        pass # placeholder for future implementation



    def test_fill_phone_number (self):
     # Add in S8
        print ("Function created for set route")
        pass #placeholder for future implementation


    def test_fill_card (self):
     # Add in S8
        print ("Function created for set route")
        pass # placeholder for future implementation


    def test_comment_for_driver (self):
      # Add in S8
        print ("Function created for set route")
        pass # placeholder for future implementation



    def test_order_blanket_and_handkerchiefs (self):
      # Add in S8
        print ("Function created for set route")
        pass #placeholder for future implementation


    def test_order_2_ice_creams(self):
        # Add in S8
        iterations = 2  # Declare a variable for the loop count
        for i in range(iterations):
            # Add in S8
            print("Function created for set route")
            pass  # Placeholder for future implementation


    def test_car_search_model_appears (self):
     # Add in S8
        print ("Function created for set route")
        pass #placeholder for future implementation
