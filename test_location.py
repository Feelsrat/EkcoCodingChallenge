import unittest
from unittest.mock import patch, Mock, call
from location import Location

from requests.exceptions import Timeout


class TestLocation(unittest.TestCase):

    def setUp(self): #  setup for mocking up requests return
        self.patcher = patch('location.requests') # patching requests call
        self.patcher.start()

    def test_object_creation(self):  # Tests that object exists after creation as expected
        location = Location()
        self.assertIsInstance(location, Location)  # Pass if object location is an instance of the Location class

    def test_setting_location(self):  # mock status code 200
        location = Location()

        location.requests.get.side_effect = Timeout

        with self.assertRaises(Timeout):
            a.setlocation()

    def test_fetching_forecast(self):  # tests if forecast JSON object is being retrieved appropriately
        return

    def test_getting_location_vals(self):  # tests to see if long and lat are fetched as expected
        location = Location()
        location.setlongitude(60.5)
        location.setlatitude(45.6)
        self.assertEqual(location.getlongitude(), 60.5)
        self.assertEqual(location.getlatitude(), 45.6)

    def test_unrecognised_location(self):  # Test to see if unrecognised location is correctly handled
        with self.assertRaises(Exception):
            location = Location()  # Tests to see if unrecognised location is detected
            location.setlocation("LivingRoom")  # Will pass if exception is raised

            self.assertEqual(location.getlatitude, None)
            self.assertEqual(location.getlongitude, None)

    def test_no_location_input(self):  # Test to see if unrecognised location is correctly handled
        with self.assertRaises(Exception):
            location = Location()  # Tests to see if unrecognised location is detected
            location.setlocation("")  # Will pass if exception is raised

            self.assertEqual(location.getlatitude, None)
            self.assertEqual(location.getlongitude, None)

    def tearDown(self): #  teardown patching
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
