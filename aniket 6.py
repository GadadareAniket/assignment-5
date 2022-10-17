class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqsum(self):
        return (((self.x)**2),((self.y)**2),((self.z)**2))
    def summ(self):
        return (((self.x)**2)+((self.y)**2)+((self.z)**2))
x = int(input("enter first number:"))
y = int(input("enter second number:"))
z = int(input("enter third number:"))

a = point(x,y,z)

print("square of numbers are:",a.sqsum())
print("sum of squares are:",a.summ())