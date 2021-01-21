def countries_capital_city(separated_by=", ") -> str:
    countries = input().split(separated_by)
    cities = input().split(separated_by)
    return "\n".join(f"{country} -> {city}" for country, city, in zip(countries, cities))


print(countries_capital_city())
