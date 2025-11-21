import random, time

continuation = True
actions = 0
life_duration = random.randint(5, 10)
MAX_HUNGER = 10
MIN_HAPPINESS = 0
MIN_ENERGY = 0

def main_loop(new_pet, continuation, actions, life_duration, MAX_HUNGER, MIN_HAPPINESS, MIN_ENERGY):
    while continuation:
        time.sleep(1)
        new_pet.show_status()
        action = input("\n-- ACCIONES --\n1. Comer\n2. Jugar\n3. Dormir\n4. Ninguna acción\n------------\nIntroduce el número de la siguiente acción de tu mascota: ")
        match int(action):
            case 1:
                print("Tu mascota está comiendo")
                new_pet.eat()
            case 2:
                print("Tu mascota está jugando")
                new_pet.play()
            case 3:
                print("Tu mascota está durmiendo")
                new_pet.sleep()
            case 4:
                print("Tu mascota no está haciendo nada")

        get_bored_probability = random.randint(1,5)
        if get_bored_probability == 1:
            time.sleep(1)
            new_pet.get_bored()

        time.sleep(1)
        new_pet.hunger += 1
        actions += 1
        new_pet.apply_limits()

        if (actions == life_duration):
            print(f"\nTu mascota ha muerto por ser demasiado mayor... 😢\nFIN DEL JUEGO. Has jugado {actions} turnos. Estadísticas finales:")
            new_pet.show_status()
            continuation = False
        elif (new_pet.hunger >= MAX_HUNGER):
            print(f"\nTu mascota ha muerto de hambre... 😢\nFIN DEL JUEGO. Has jugado {actions} turnos. Estadísticas finales:")
            new_pet.show_status()
            continuation = False
        elif (new_pet.happiness <= MIN_HAPPINESS):
            print(f"\nTu mascota ha muerto de tristeza... 😢\nFIN DEL JUEGO. Has jugado {actions} turnos. Estadísticas finales:")
            new_pet.show_status()
            continuation = False
        elif (new_pet.energy <= MIN_ENERGY):
            print(f"\nTu mascota ha muerto de cansancio... 😢\nFIN DEL JUEGO. Has jugado {actions} turnos. Estadísticas finales:")
            new_pet.show_status()
            continuation = False
        