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
        self.returned_rover_pos = [1,1,'N']

    def get_rover_pos(self):

        return self.returned_rover_pos

