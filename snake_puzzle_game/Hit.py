import numpy as np

class Hit:
    
    def __init__(self, position, command):
        self.appearance = 'circle'
        self.speed = 5
        self.position = np.array([position[0]-2.5, position[1]-2.5, position[0]+2.5, position[1]+2.5])
        self.state = None
        self.outline = "#0000FF"

       
    def collision_check(self, enemys):
        for enemy in enemys:
            collision = self.overlap(self.position, enemy.position)
            
            if collision:
                enemy.state = 'die'
                self.state = 'hit'
    
    def overlap(self, ego_position, other_position):
        return ego_position[0] > other_position[0] and ego_position[1] > other_position[1] \
                 and ego_position[2] < other_position[2] and ego_position[3] < other_position[3]