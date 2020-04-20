'''
The Builder Design Pattern helps us to slice the operations of building an object. 
It focuses on constructing a complex object step by step. 
It also enforces a process to create an object as a finished product. 
That means an object has to be massaged by some instructed steps before it is ready and can be used by others.
Generally, It allows you to encapsulate the complex create logic.

Builder pattern is very much like factory pattern. 
The key difference between a builder and factory is that a builder 
is useful when you need to do lots of things to build an object
'''

from copy import deepcopy

class Car:
    def __init__(self):
        self.__wheels  = list()
        self.__engine  = None
        self.__body    = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)

    def clone(self):
        return deepcopy(self)

# === Car parts ===
class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # The algorithm for assembling a car
    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car


class BuilderInterface:
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass


class JeepBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body


class NissanBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 100
        return engine

    def getBody(self):
        body = Body()
        body.shape = "hatchback"
        return body
    
 # ==Build Car==
 
d = Director()
d.setBuilder(JeepBuilder())
d.getCar().specification()
   