class calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mult(self):
        return self.x*self.y
    def divide(self):
        return self.x/self.y

obj = calculator(94,10)
print(obj.add())
print(obj.sub())
print(obj.mult())
print(obj.divide())