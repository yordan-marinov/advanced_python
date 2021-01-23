def split_data(data):
    def quantity_quality_values_in_tuple() -> (int, int):
        return tuple(int(value.split(":")[1]) for value in quantity_quality.split(";"))

    categories, names, quantity_quality = data.split(" - ")
    quantity_quality_value = quantity_quality_values_in_tuple()

    return categories, names, quantity_quality_value


def average_quality(quality_total, categories_count) -> str:
    return f"{quality_total / categories_count:.2f}"


def print_result(final_dict, t_quantity, t_quality):
    print(f"Count of items: {t_quantity}")
    print(f"Average quality: {average_quality(t_quality, len(final_dict))}")

    for category, values in final_dict.items():
        print(f"{category} -> {', '.join(e for e in values.keys())}")


dict_of_item_categories = {
    item_category: {}
    for item_category in input().split(", ")
}

total_quantity = 0
total_quality = 0

for _ in range(int(input())):
    input_data = input()
    category, name, quantity_quality_values = split_data(input_data)
    dict_of_item_categories[category][name] = quantity_quality_values
    total_quantity += quantity_quality_values[0]
    total_quality += quantity_quality_values[1]

print_result(dict_of_item_categories, total_quantity, total_quality)
