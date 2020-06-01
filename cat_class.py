# Cat class will inherit from Animal all the behaviours and characteristic
import random
from animal_class import *

# to inherit pass the entire parent class to your subclass
class Cat(Animal):
    'nothing'

    def purr(self, frequency=(random.randint(25,150))):
        return f'PurrrUUURRrrrURURUR and a steady {frequency} frequency'
        # return 'PurrrUUURRrrrURURUR and a steady {} frequency'.format(frequency)
        # return 'PurrrUUURRrrrURURUR and a steady '+ str(frequency) + ' frequency'



# garfield = Cat()
# print(garfield)
#
# print(garfield.eat('Lasanhaaa'))
# print(garfield.sleep())
# print(garfield.potty())