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

    def show_status(self):
        print(f"Estado de {self.name}:")
        print(f"❤️  Felicidad: {self.happiness}\n⚡ Energía: {self.energy}\n🍖 Hambre: {self.hunger}")

    def eat(self):
        print("🍗 Ñam Ñam Ñam")
        self.energy -= 1
        self.hunger -= 3
        self.happiness += 1

    def sleep(self):
        print("😴 zzzzzz")
        self.energy += 4
        self.hunger += 1
        self.happiness += 1
    
    def play(self):
        print("🎾 ¡Yupiii!")
        self.energy -= 2
        self.hunger += 2
        self.happiness += 2

    def get_bored(self):
        print("🥱 Qué aburrimiento...")
        self.happiness -= 2
        self.energy -= 1
        self.hunger += 1


continuation = True
new_pet = Pet(name)


while continuation:
    new_pet.show_status()


    # ALEATORIEDAD DE ABURRIMIENTO DESPUÉS DE ELEGIR ACCIÓN Y APLICARLA
    get_bored_probability = random.randint(1,5)
    if get_bored_probability == 1:
        new_pet.get_bored()

    continuation = False


