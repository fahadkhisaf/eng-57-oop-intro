# import classes here and intialize objs and run methods
# this speration will maintain you code more organized following speration of concerns

from dog_class import Dog
from cat_class import Cat

# Initialize a Dog object -
max_dog_instance = Dog(name='Max')
ringo_dog_instance = Dog(age=10, name='Ringo')
# initialize a Cat object -
garfield = Cat(name='Garfield the Lasanha Monster')

print(max_dog_instance)
print(garfield)

print(max_dog_instance.name)
print(ringo_dog_instance.name)

# # Call the method .bark() on object
#
print(max_dog_instance.eat('BONE'))
print(max_dog_instance.bark())
print(max_dog_instance.fetch())
print(max_dog_instance.potty())
print(max_dog_instance.bark())
print(max_dog_instance.sleep())
print(max_dog_instance.reproduce())

# print('walk the dog home')
#
# print(max_dog_instance.sleep())
# print(max_dog_instance.sleep())
# print(max_dog_instance.bark("Creepy Stranger!!"))

print('garfield time //////////////////////')
print(garfield.potty())
print(garfield.eat('Lasanhaaa'))
print(garfield.sleep())
print(garfield.potty())
# print(garfield.fetch())
print(garfield.purr())
print(garfield.reproduce())

print('The name of the cat is:')
print(garfield.name)

