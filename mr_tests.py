import unittest
import mr_objects


#The test cases
class MarsRoverTest(unittest.TestCase):
    #Test 1
    def test_working(self):
        self.assertTrue(True)

    def test_planet_exists(self):
        self.assertTrue(True)
    

    def test_know_planet_size(self):
        expected_planet_size = 10
        #This line iniciates an instance of the planet class from mr_objects.py
        planet = mr_objects.planet()
        # print("*** test_know_planet_size start ***")
        # print(mr_objects.planet())
        # print("*** test_know_planet_size end ***")
        self.assertEqual(planet.get_planet_size(), expected_planet_size)

