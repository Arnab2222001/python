class Point:                                    #the class name first latter is always be upper case latter
    def move(self):
        print("move")


    def draw(self):
        print("draw")


point1=Point()#that is a object in this stape we make a object point class
point1.draw()
point1.x=10
point1.y=20
print(point1.x)
print(point1.y)