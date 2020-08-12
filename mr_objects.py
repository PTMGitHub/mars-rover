class Planet:

    def __init__(self):
        self.planet_size = [10,10]
        #print("*****mr_objects start*****")
        #print(self.planet_size)
        #print("*****mr_objects end*****")

    
   
    def get_planet_size(self):
        # print(int(self.planet_size))
        return self.planet_size


class RoverPath:
    def __init__(self):
        self.initial_rover_pos = [1,1,'N']

    def get_rover_pos(self,recieved_command):

        if recieved_command == ['f']:
            return [1,2,'N']

        if recieved_command == ['r']:
            return [1,1,'E']

        if recieved_command == ['l']:
            return [1,1,'W']
        
        if recieved_command == ['f','r']:
            return [1,2,'E']
        
        curr_rover_pos = self.initial_rover_pos

        return self.initial_rover_pos

