class Vet:
    animals = []  # rename it to "animals" before submission in Judge.
    space = 5  # rename it to "space" before submission in Judge.

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if Vet.space == 0:
            return "Not enough space"

        Vet.space -= 1
        Vet.animals.append(animal_name)
        self.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if animal_name not in Vet.animals:
            return f"{animal_name} not in the clinic"

        Vet.space += 1
        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
