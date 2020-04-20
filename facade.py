'''
Facade is a part of Gang of Four design pattern and it is categorized under Structural design patterns. 
Before we dig into the details of it, let us discuss some examples which will be solved by this particular Pattern.

So, As the name suggests, it means the face of the building. The people walking past the road can only see this glass face of the building. 
They do not know anything about it, the wiring, the pipes and other complexities. 
It hides all the complexities of the building and displays a friendly face.

Facade discusses encapsulating a complex subsystem within a single interface object. 
This reduces the learning curve necessary to successfully leverage the subsystem. 
It also promotes decoupling the subsystem from its potentially many clients. 
On the other hand, if the Facade is the only access point for the subsystem, 
it will limit the features and flexibility that "power users" may need.

Main Reasons to use a facade pattern:
- hides complexity, should use on highly complex applications
- loosley coupled, so modifications will be easier
- single interface object to access
'''


class Engine:
    
    def __init__(self):
        # how much the motor is spinning in revs per minute
        self.spin = 0

    def start(self, spin):
        self.spin = min(spin, 3000)

class StarterMotor:

    def __init__(self):
        # how much the starter motor is spinning in revs per minute
        self.spin = 0

    def start(self, charge):
        # if there is enough power then spin fast
        if (charge > 50):
            self.spin = 2500

class Battery:

    def __init__(self):
        # % charged, starts flat
        self.charge = 0

class Car:
    # the facade object that deals with the battery, engine and starter motor.

    def __init__(self):
        self.battery = Battery()
        self.starter = StarterMotor()
        self.engine = Engine()

    def turn_key(self):
        self.starter.start(self.battery.charge)
        self.engine.start(self.starter.spin)
        if (self.engine.spin > 0):
            print('Engine started')
        else:
            print('Engine not started')

    def jump(self):
        self.battery.charge = 100
        print('Jumped')