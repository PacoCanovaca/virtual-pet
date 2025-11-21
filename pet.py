import random

class Pet:
    """Clase que crea una nueva mascota
    """
    def __init__(self, name):
        """Método constructor de la clase Pet

        Args:
            name (str): Nombre de la mascota aportado por el usuario
        """
        self.name = name
        self.energy = random.randint(3, 5)
        self.hunger = random.randint(3, 5)
        self.happiness = random.randint(3, 5)
        self.actions = 0

    def show_status(self):
        """Función que muestra por consola el estado actual de la mascota, con todas sus estadísticas
        """
        print(f"\nEstado de {self.name}:")
        print(f"❤️  Felicidad: {self.happiness}\n⚡ Energía: {self.energy}\n🍖 Hambre: {self.hunger}")

    def eat(self):
        """Función de comer de la mascota, lo cual altera sus estadísticas
        """
        print("\n'🍗 Ñam Ñam Ñam'")
        self.energy -= 1
        self.hunger -= 3
        self.happiness += 1

    def sleep(self):
        """Función de dormir de la mascota, lo cual altera sus estadísticas
        """
        print("\n'😴 zzzzzz'")
        self.energy += 4
        self.happiness += 1
    
    def play(self):
        """Función de jugar de la mascota, lo cual altera sus estadísticas
        """
        print("\n'🎾 ¡Yupiii!'")
        self.energy -= 2
        self.hunger += 2
        self.happiness += 2

    def get_bored(self):
        """Función de aburrirse de la mascota, generada automáticamente, la cual altera sus estadísticas
        """
        print("\n'🥱 Qué aburrimiento...'")
        self.happiness -= 2
        self.energy -= 1

    def apply_limits(self):
        """Función que aplica límites a las estadísticas de la mascota, estableciendo máximos y mínimos en sus valores
        """
        self.energy = min(10, self.energy)
        self.hunger = max(self.hunger, 0)
        self.happiness = min(self.happiness, 10)