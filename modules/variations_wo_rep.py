from math import factorial
from errors.non_positive_natural_number import NonPositiveNaturalNumber


def variations_without_rep(n, k):
    if n < 1 or k < 1:
        raise NonPositiveNaturalNumber()

    if k > n:
        raise Exception('Błąd! `k` musi być mniejsze lub równe `n`')

    # Według wzoru n! / (n - k)!
    variations_count = factorial(n) / factorial(n - k)

    return variations_count
