from abc import ABC, abstractclassmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractclassmethod
    def make_sound(self):
        pass
    
    @abstractclassmethod
    def __repr__(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"

        
        
class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"

class Kitten(Cat):
    def __init__(self, name, age, gender="Female"):
        Cat.__init__(self, name, age, gender)

    def make_sound(self):
        return "Meow"    
        
        
class Tomcat(Cat):
    def __init__(self, name, age, gender="Male"):
        Cat.__init__(self, name, age, gender)

    def make_sound(self):
        return "Hiss"    
                
        
        
dog = Dog("Sharo", 5, "male")
dog2 = Dog("Simba", 5, "female")
print(dog2.make_sound())
print(dog2)
cat = Cat("Pisi", 2, "female")
print(cat.make_sound())
print(cat)
kitty = Kitten("Kity", 8)
print(kitty.make_sound())
print(kitty)
tom = Tomcat("Tom", 4)
print(tom.make_sound())
print(tom)