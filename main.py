import pet, loop, random

name = input("Introduce el nombre de la mascota: ")

Pet = pet.Pet

new_pet = Pet(name)
print(f"Ha nacido {name}, tu nueva mascota")

continuation = True
actions = 0
life_duration = random.randint(5, 10)
MAX_HUNGER = 10
MIN_HAPPINESS = 0
MIN_ENERGY = 0

loop = loop.main_loop(new_pet, continuation, actions, life_duration, MAX_HUNGER, MIN_HAPPINESS, MIN_ENERGY)

