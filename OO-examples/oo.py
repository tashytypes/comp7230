

# defining a class - car
# Class is the blueprint or template from which objects can be created. E.g
# A car has attribute wheels and color, but these are not defined until and object is made from the class
# A class (generic template) -> objects (instances of the class that have attributes and methods specific to the object, e.g. name)
class Car:

    number_of_cars = 0
    # Constructor function - this method (function) is called when you ínstantiate the object.
    def __init__(self, wheels, colour, name):
        self.wheels = wheels # this sets the object's attributes when the object is created from the class.
        self.colour = colour
        self.name = name
        Car.number_of_cars += 1

    def info(self): # self is the instance of the object that allows you to access the objects attributes in methods
        # note: number of cars is a static attribute that is associated with the class, not the object.
        print("Number of cars %s. %s has %s wheels and is %s." % (Car.number_of_cars, self.name, self.wheels, self.colour))

tims_car = Car(6, 'blue', 'Tims car') # instantiated the object -> fancy way of saying creating an object from a Class construction
tims_car.info() # using a class method

tashs_car = Car(4, 'red', "Tashs Car") # instanting another object


tashs_car.info() # Method returns different info because that method uses the values specific to that objecth
