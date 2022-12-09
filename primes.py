"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number must be positive")
    else:
        list = []
        current_number = 2

        while len(list) < number_of_primes:
            if is_prime(current_number):
                list.append(current_number)
                current_number += 1

        return list
