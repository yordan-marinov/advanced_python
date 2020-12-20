class Trainer:

    def __init__(self, name: str):
        self.name: str = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon.name in [p.name for p in self.pokemon]:
            return f"This pokemon is already caught"

        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemons = [p.name for p in self.pokemon if pokemon_name == p.name]
        if not pokemons:
            return f"Pokemon is not caught"

        self.pokemon.remove(pokemons[0])
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        trainer_data = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n- "
        for p in self.pokemon:
            trainer_data += p.pokemon_details() + "\n"

        return trainer_data
