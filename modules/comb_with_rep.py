from math import factorial
from errors.non_positive_natural_number import NonPositiveNaturalNumber


def comb_with_rep(n, k):
    if n < 1 or k < 1:
        raise NonPositiveNaturalNumber()

    # Według wzoru (n + k - 1)! / (k! * (n - 1)!)
    comb_count = factorial(n + k - 1) / (factorial(k) * factorial(n - 1))

    return comb_count
