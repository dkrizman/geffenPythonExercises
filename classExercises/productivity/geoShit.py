class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def perimeter(self):
        res = (self.length+self.width)*2
        return res
    
    def area(self):
        res = self.length*self.width
        return res
    
class square(rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
class cube(square):
    def __init__(self, length):
        super().__init__(length)
        
    def volume(self):
        res = self.length**3
        return res

if __name__ == "__main__":
    pass