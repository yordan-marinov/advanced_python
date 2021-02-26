class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name: str = name
        self.price: float = price
        self.ingredients: dict = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
        else:
            self.ingredients[ingredient] += quantity

        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return (
                f"Pizza {self.name} already prepared and "
                f"we can't make any changes!"
            )

        if ingredient not in self.ingredients:
            return (
                f"Wrong ingredient selected! "
                f"We do not use {ingredient} in {self.name}!"
            )

        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price * quantity

    def make_order(self):
        self.ordered = True
        return (
            f"You've ordered pizza {self.name} prepared with "
            f"{', '.join(f'{k}: {v}' for k, v in self.ingredients.items())} "
            f"and the price will be {self.price}lv."
        )


margarita = PizzaDelivery("Margarita", 11, {"cheese": 2, "tomatoes": 1})
margarita.add_extra("mozzarella", 1, 0.5)
margarita.add_extra("cheese", 1, 1)
margarita.remove_ingredient("cheese", 1, 1)
print(margarita.remove_ingredient("bacon", 1, 2.5))
print(margarita.remove_ingredient("tomatoes", 2, 0.5))
margarita.remove_ingredient("cheese", 2, 1)
print(margarita.pizza_ordered())
print(margarita.add_extra("cheese", 1, 1))
