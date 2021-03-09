class Mother:
    def __init__(self, name):
        self.__name = name

    def _say_hi(self):
        return "Hi from Mother"
    


class Father:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return "Hi from Father"



class Child1(Mother, Father):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hi(self):
        res = super()._say_hi()
        return "Hi from child1 " + res


class Child2(Mother, Father):
    def __init__(self, name, age, mother=None, father=None):
        self.name = name
        self.age = age
        self.mother = mother
        self.father = father
        
    @property
    def full_name(self):
        return self.name + " " + self.father.name

    def say_hi(self):
        res = super()._say_hi()
        return "Hi from child2 " + res

mother = Mother("Samanta")
father = Father("Tommy")

child = Child1("Charley", 12)
child2 = Child2("Sindy", 8, mother=mother, father=father)

# print(child2.say_hi())

# print(child.say_hi())
# print(child.name)


# print(child2.name)
# print(child2.full_name)
# print(child2.father.name)
# print(child2.mother.name)

# print(help(child2))
print(dir(child))
print(130 * "=")
print(dir(child2))