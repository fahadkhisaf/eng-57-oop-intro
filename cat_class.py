# Cat class will inherit from Animal all the behaviours and characteristic
import random
from animal_class import *

# to inherit pass the entire parent class to your subclass
class Cat(Animal):

    # POLYMORPHSIM - CALLING ON PARENT METHOD TOO KEEP BOTH FUNCTIONALITIES
    def __init__(self, name='Toby', owner='Filipe'):
        # allows you access to parent class
        # in this case - super() = Animal
        super().__init__('Small domesticated lion', 4) #call parent init method with arguments
        self.name = name
        self.owner = owner







    def purr(self, frequency=(random.randint(25,150))):
        return f'PurrrUUURRrrrURURUR and a steady {frequency} frequency' # return 'PurrrUUURRrrrURURUR and a steady {} frequency'.format(frequency) # return 'PurrrUUURRrrrURURUR and a steady '+ str(frequency) + ' frequency'

    # POLYMORPHSIM - re-defining method reproduce for subclass cat
    def reproduce(self):
        return f"Amazing feline specimen of {self}"














# Manually testing our objects
# garfield = Cat()
# print(garfield)
#
# print(garfield.eat('Lasanhaaa'))
# print(garfield.sleep())
# print(garfield.potty())