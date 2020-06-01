class Animal():

    def __init__(self, species_argument, limbs):
        self.species_parameter = species_argument
        self.limbs = limbs

    def eat(self, food):
        return 'Nom, nom, non, nom ' + food.lower()

    def sleep(self):
        return 'zzZZzzZZz ZZzzzZZzz'

    def potty(self):
        return "UHHHHH!!! AHAHHHH! 0_o UUHHH!!  ..... O_O .. :) o.o ..  "

    def reproduce(self, partner='... sorry you are alone at this one'):
        return f"offspring of {self} and {partner}"













# create animal instance
# animal_1 = Animal()
#
# print(animal_1)
# print(animal_1.eat('KFC'))