class Student:
  def setName(self):
    print("the Name of student is ",self.name)
  def getName(self):
    self.name=input("Enter the name of student : ")
  def setRollNumber(self):
    print("The roll number of student is ", self.roll)
  def getRollNumber(self):
    self.roll=input("Enter the roll Number of student  :  ")

obj=Student()
obj.getName()
obj.setName()
obj.getRollNumber()
obj.setRollNumber()