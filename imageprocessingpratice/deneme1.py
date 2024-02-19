import math
class nokta(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def pozisyon(self):
        return self.x,self.y
    def hareket(self,x,y):
        self.x+=x
        self.y+=y
    def mesafe(self,pt):
        dx=pt.x-self.x
        dy=pt.y-self.y
        return math.sqrt(dx**2+dy**2)

class person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("person name:",self.name)
        print("person age:",self.age)
class student(person):
    def __init__(self,name,age,section):
        person.__init__(self,name,age)
        self.section=section
    def displayStudent(self):
        print("student name:", self.name)
        print("student age:", self.age)
        print("student section:",self. section)

def armstrong(number):
    for digit in str(number):
        sum=0
    if number==sum:
        print("armstrong sayıdır")
    else:
        print("sayı armstrong değildir")

