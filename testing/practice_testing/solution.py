class Person:
    def __init__(self, name, last_name, age, gender, town):
        self.__name = name
        self.__last_name = last_name
        self.age = age
        self.gender = gender
        self.town = town

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def full_name(self):
        return f"{self.__name} {self.__last_name}"
    
    def get_info(self):
        return f"Hi I am {self.gender} from {self.town} on {self.age} and my name is {self.full_name}!"
    
    def __repr__(self):
        return f"{self.__dict__}"
