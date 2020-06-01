# Abstract and create the class dog

from animal_class import *

class Dog(Animal):

    # this is a special method
    # it comes defined either was but we can re-write it
    # this methos stands for initialize class object AKA the constructor in other languages
    # allow us to set attribute to our Dog objects
        # ... Like.. the poor thing doesn't even have a name :(
            # we should give it name... possibly Max :)

    # refers to the instance of the object
    def __init__(self, name = 'Mad Max', age=0):
        # setting attribute name to instances of Dog class
        self.name = name
        self.age = age
        self.paws = 4
        self.fur = 'luxurious black and grey'


    # this is a method that can be used by a Dog instance
    def bark(self, person = ''):
        return 'woof, woof! I see you there ' + person

    def bark_print(self):
        print('woof, woof!')

    def fetch(self):
        return "WHERE THAT BALL AT? --- I'ma get that ball!!"




# This print should not be here.
# In this file you define the class dog and add attributes and method to the class
# that is it.
#print('Filipe is so cool and Shahrukh is AMAZING - such a nice guy who waves to police men')