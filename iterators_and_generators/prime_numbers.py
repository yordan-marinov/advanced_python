def get_primes(lst_numbers: list):
    for number in lst_numbers:
        if number > 1:
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
