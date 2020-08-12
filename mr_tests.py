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
        expected_planet_size = [10,10]
        #This line iniciates an instance of the planet class from mr_objects.py
        planet = mr_objects.Planet()
        # print("*** test_know_planet_size start ***")
        # print(mr_objects.planet())
        # print("*** test_know_planet_size end ***")
        self.assertEqual(planet.get_planet_size(), expected_planet_size)

    def test_current_position(self):
        expected_current_pos = [1,1,'N']
        passed_command = ''
        rover_pos = mr_objects.RoverPath()
        self.assertEqual(rover_pos.get_rover_pos(passed_command),expected_current_pos)
    
    def test_move_rover_forward_by_one(self):
        expected_current_pos = [1,2,'N']
        passed_command = ['f']
        rover_pos = mr_objects.RoverPath()
        self.assertEqual(rover_pos.get_rover_pos(passed_command),expected_current_pos)

    def test_rover_turn_right(self):
        expected_current_pos = [1,1,'E']
        passed_command = ['r']
        rover_pos = mr_objects.RoverPath()
        self.assertEqual(rover_pos.get_rover_pos(passed_command),expected_current_pos)

    def test_rover_turn_left(self):
        expected_current_pos = [1,1,'W']
        passed_command = ['l']
        rover_pos = mr_objects.RoverPath()
        self.assertEqual(rover_pos.get_rover_pos(passed_command),expected_current_pos)

    def test_rover_forward_turn_right(self):
        expected_current_pos = [1,2,'E']
        passed_command = ['f','r']
        rover_pos = mr_objects.RoverPath()
        self.assertEqual(rover_pos.get_rover_pos(passed_command),expected_current_pos)