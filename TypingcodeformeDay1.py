class Cliente:
    def __init__(self, name, age, weight, goal):
        self.name = name
        self.age = age
        self.weight = weight
        self.goal = goal
    def __str__(self):
        return f"el cliente es {self.name}, tiene {self.age} años, pesa {self.weight} kg y su objetivo es {self.goal}"


Julian = Cliente ("Julian", 25, 70, "perder peso")
print(Julian) 