https://learn.madetech.com/katas/mars-rover/

Mars Rover Kata
You’re part of the team that explores Mars by sending remotely controlled vehicles to the surface of the planet. Develop an API that translates the commands sent from earth to instructions that are understood by the rover.

Requirements
You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
The rover receives a character array of commands.
Implement commands that move the rover forward/backward (f,b).
Implement commands that turn the rover left/right (l,r).
Implement wrapping from one edge of the grid to another. (planets are spheres after all)
Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, aborts the sequence and reports the obstacle.
Rules
Be careful about edge cases and exceptions. We can not afford to lose a mars rover, just because the developers overlooked a null pointer.
References
Victor Farcic
Kata Log Rocks: Mars Rover


**Notes ideas**

1, Test we have starting points - a "Position 2d array" this will result in a 2d array of the rovers movements
2, Planet (we know what the plaent looks like ) i.e 10x10 grid  - where the obstacles are
3, check we have recived commands - will be a 2d array of the complete instructions sent form Earth 
4,



#Implementation Code
class Scoreboard:
    
    def score_function(self):
        return self.outcome
    
    def __init__(self):
        self.outcome = 0