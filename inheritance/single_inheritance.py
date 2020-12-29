class Animal:
    def eat(self):
        return "eating..."


class Dog(Animal):
    def bark(self):
        return "barking..."


animal = Animal()
dog = Dog()
print(dog.eat())
print(dog.bark())
print(animal.eat())
