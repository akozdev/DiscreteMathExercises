from math import factorial
from errors.non_positive_natural_number import NonPositiveNaturalNumber


def count_comb_without_rep(n, k):
    if n < 1 or k < 1:
        raise NonPositiveNaturalNumber()

    if k > n:
        raise Exception('Błąd! `k` musi być mniejsze lub równe `n`')

    # Według wzoru n! / (k! * (n - k)!)
    comb_count = factorial(n) / (factorial(k) * factorial(n - k))

    return comb_count


def get_comb_without_rep(myset, k):
    n = len(myset)
    if n < 1 or k < 1:
        raise NonPositiveNaturalNumber()

    if k > n:
        raise Exception('Błąd! `k` musi być mniejsze lub równe `n`')

    all_combs = []

    for i in range(0, n):
        for j in range(i, n):
            if i != j:
                all_combs.append([myset[i], myset[j]])

    return all_combs


print(count_comb_without_rep(5, 2))
print(get_comb_without_rep(['a', 'b', 'c', 'd', 'e'], 2))
