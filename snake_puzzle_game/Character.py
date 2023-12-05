import numpy as np

class Character:
    
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.state = None
        self.position = np.array([width/2 - 10, height/2 - 10, width/2 + 0, height/2 + 0])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

    def move(self, command = None):
        if command == None:
            self.state = None
            
        else:
            self.state = 'move'

            if command == 'up_pressed':
                self.position[1] -= 5
                self.position[3] -= 5

            elif command == 'down_pressed':
                self.position[1] += 5
                self.position[3] += 5

            elif command == 'left_pressed':
                self.position[0] -= 5
                self.position[2] -= 5
                
            elif command == 'right_pressed':
                self.position[0] += 5
                self.position[2] += 5