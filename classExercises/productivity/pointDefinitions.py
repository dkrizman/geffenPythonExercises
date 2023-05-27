import math as m

class point:
    def __init__(self,x,y):
        self.move(x, y)
        self.distance = m.sqrt(self.x**2 + self.y**2)
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0,0)
        

if __name__ == "__main__":
    pass