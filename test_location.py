import unittest
from location import Location


class TestLocation(unittest.TestCase):

    def test_object_creation(self):  # Tests that object exists after creation as expected
        location = Location()
        self.assertIsInstance(location, Location)  # Pass if object location is an instance of the Location class

    def test_setting_location(self):  # This test might fail sometimes due to API throttling
        location = Location()  # Tests to see if long and lat are set correctly
        location.setlocation("Dublin")
        self.assertIsNotNone(location.getlatitude())  # Check to see if longitude and latitude are set correctly.
        self.assertIsNotNone(location.getlongitude())  # When object is instantiated both variables are null.

    def test_fetching_forecast(self):  # tests if forecast JSON object is being retrieved appropriately
        location = Location()
        location.setlongitude(50.0)
        location.setlatitude(50.0)
        obj = location.getforecast()
        self.assertIsNotNone(obj)  # If object exists and is not null then API call is successful

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


if __name__ == '__main__':
    unittest.main()
