def fibonacci():
    previous_number = 0
    current_number = 0
    while True:
        yield previous_number

        if current_number == 0:
            current_number += 1

        (
            previous_number,
            current_number
        ) = (
            current_number,
            current_number + previous_number
        )


generator = fibonacci()
for i in range(50):
    print(next(generator))
