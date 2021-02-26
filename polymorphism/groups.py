class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + " " + self.surname

    def __add__(self, other):
        name = self.name
        surname = other.surname
        return Person(name, surname)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        res = self.people + other.people
        return Group(self.name, res)

    def __str__(self):
        return f"Group {self.name} with members {', '.join(f'{p.full_name}' for p in self.people)}"

    def __getitem__(self, index: int):
        return f"Person {index}: {self.people[index].full_name}"


p0 = Person("Aliko", "Dangote")
p1 = Person("Bill", "Gates")
p2 = Person("Warren", "Buffet")
p3 = Person("Elon", "Musk")
p4 = p2 + p3

first_group = Group("__VIP__", [p0, p1, p2])
second_group = Group("Special", [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
