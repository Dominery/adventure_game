class Vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def plus(self,pos):
        return Vec(self.x+pos.x,self.y+pos.y)
    
    def times(self,factor):
        return Vec(self.x*factor,self.y*factor)

    def __repr__(self):
        return self.__class__.__name__+f'<{self.x},{self.y}>'