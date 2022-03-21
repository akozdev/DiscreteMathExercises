from errors.non_positive_natural_number import NonPositiveNaturalNumber


def variations_with_rep(n, k):
    if n < 1 or k < 1:
        raise NonPositiveNaturalNumber()

    # Według wzoru n^k
    variations_count = pow(n, k)

    return variations_count
