class Animal:
    def __init__(self, name, hunger, diet):
        self.name = name
        self.hunger = hunger
        self.diet = diet
    
    def eat(self, food):
        if food >0 and self.hunger < 25:
            self.hunger +=food

class Dog(Animal):
    def __init__(self, name, breed, hunger, diet)
        self.breed = breed
        super().__init__(name, hunger, diet)