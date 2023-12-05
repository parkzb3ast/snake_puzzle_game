import numpy as np

class Enemy:
    
    def __init__(self, spawn_position):
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 10, spawn_position[1] - 10, spawn_position[0] + 0, spawn_position[1] + 0])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
