class Animal:
    def eat(self):
        return "eating..."


class Dog(Animal):
    def bark(self):
        return "barking..."


class Cat(Dog):
    def meow(self):
        return "meowing..."


cat = Cat()
dog = Dog()
dog2 = Dog()
animal = Animal()

print(animal.eat())
print(dog.eat())
print(cat.eat())
print(dog.bark())
print(cat.meow())
print(dog2.eat())
print(help(cat))
