import random, time

name = input("Introduce el nombre de la mascota: ")

class Pet:
    
    def __init__(self, name):
        self.name = name
        self.energy = random.randint(3, 5)
        self.hunger = random.randint(3, 5)
        self.happiness = random.randint(3, 5)
        self.actions = 0

    MAX_HUNGER = 10
    MIN_HAPPINESS = 0
    MIN_ENERGY = 0

continuation = True
new_pet = Pet(name)

while continuation:
    print(name)
    continuation = False


