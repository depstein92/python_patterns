'''
Typically, when using a factory pattern, objects in the factory should all have the
same interface 
'''

class Shape2DInterface:
    def draw(self): pass

class Shape3DInterface:
    def build(self): pass 

class Circle(Shape2DInterface):
    def draw(self):
        print('Circle.draw')
 
class Square(Shape2DInterface):
    def draw(self):
        print('Square.draw')

class Sphere(Shape3DInterface):
    def build(self):
        print('Sphere.build')

class Cube(Shape3DInterface):
    def build(self):
        print("Cube.build")
                                        
class ShapeFactoryInterface:
    def create_shape(sides): pass
    

class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def create_shape(sides):
        if sides == 1:
           return Circle()
        elif sides == 2:
           return Square()

class Shape3DFactory(ShapeFactoryInterface):
    @staticmethod
    def create_shape(sides):
        if sides == 1:
            return Sphere()
        elif sides > 1:
            return Cube()       
                