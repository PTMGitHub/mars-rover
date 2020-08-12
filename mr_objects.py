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

        curr_rover_pos = [1,1,'N']

        curr_x = curr_rover_pos[0]
        curr_y = curr_rover_pos[1]
        curr_d = curr_rover_pos[2]

        direction = {0:"N",
        1:"E",
        2:"S",
        3:"W"}
        
        # r = +1
        # l = -1

        # x = 0
        # y = 0

        # f =


        if recieved_command == ['f']:
            # return [1,2,'N']
            if curr_rover_pos[2] == 'N':
                curr_y = curr_y +1
            if curr_rover_pos[2] == 'E':
                curr_x = curr_x +1          
            if curr_rover_pos[2] == 'S':
                curr_y = curr_y -1
            if curr_rover_pos[2] == 'W':
                curr_x = curr_x -1            


        if recieved_command == ['r']:
            # return [1,1,'E']
            if curr_rover_pos[2] == 'N':
                curr_x = curr_x -1
            if curr_rover_pos[2] == 'E':
                curr_x = curr_y -1          
            if curr_rover_pos[2] == 'S':
                curr_x = curr_x +1
            if curr_rover_pos[2] == 'W':
                curr_x = curr_y +1     

        if recieved_command == ['l']:
            return [1,1,'W']
        
        if recieved_command == ['f','r']:
            return [1,2,'E']
        
        curr_rover_pos = [curr_x,curr_y,curr_d]

        return curr_rover_pos

