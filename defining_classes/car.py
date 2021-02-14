class Car:
    def __init__(self, name: str, model: str, engine: str):
        self.name = name
        self.model = model
        self.engine = enginec

    def get_info(self):
        return f"This is {self.name} {self.model} " f"with engine {self.engine}"


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())