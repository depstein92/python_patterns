'''
Interfaces in Python are different then statically typed langauges,
because Python has the capability to have multiple inheritence, 
unlike C#/.Net that would need an interface. 


At a high level, an interface acts as a blueprint for designing classes. 
Like classes, interfaces define methods. Unlike classes, these methods are abstract. 
An abstract method is one that the interface simply defines. It doesn’t implement the methods. 
This is done by classes, which then implement the interface and give concrete meaning to the interface’s abstract methods

More on interfaces:
https://realpython.com/python-interface

Really you only want to inherit the methods of the interface,
while each derived class has its own propertys
'''


class ShapeInterface():
    def draw(self): pass

class Circle(ShapeInterface):
    def draw(self):
        print('Circle.draw') 

class Square(ShapeInterface):
    def draw(self):
        print('Square.draw') 

class ShapeFactory:
    @staticmethod
    def get_shape(type):
        if type == 'circle':
            return Circle()
        elif type == 'square':
            return Square()
        else:
            raise ValueError('Value not found')
                
 
                  