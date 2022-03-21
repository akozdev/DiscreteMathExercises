import sys
from errors.non_positive_natural_number import NonPositiveNaturalNumber

from modules.comb_wo_rep import count_comb_without_rep
from modules.comb_wo_rep import get_comb_without_rep
from modules.comb_with_rep import comb_with_rep
from modules.variations_wo_rep import variations_without_rep
from modules.variations_with_rep import variations_with_rep

print('\nDostępne programy:')
print('1) Kombinacje bez powtórzeń')
print('2) Kombinacje z powtórzeniami')
print('3) Wariacje bez powtórzeń')
print('4) Wariacje z powtórzeniami')
print('5) Permutacje z powtórzeniami')
print('6) Podziały zbioru na niepuste zbiory rozłączne')
print('7) Stirlinga...')

while True:
    user_input = input('\nWybierz program (lub wpisz "exit" w celu wyjścia): ')
    print("")

    try:
        match user_input:
            # Kombinacje bez powtórzeń
            case '1':
                print('Wybrano kombinacje bez powtórzeń\n')
                n = int(input('Wprowadź liczbę wszystkich elementów w zbiorze (n): '))
                k = int(input('Wprowadź liczbę elementów w podzbiorze (k): '))

                comb_count = count_comb_without_rep(n, k)
                all_combinations = get_comb_without_rep({"a", "b", "c", "d", "e"}, 2)

                print(all_combinations)

                print(
                    f"Istnieje {int(comb_count)} {k}-elementowych kombinacji bez powtórzeń zbioru {n}-elementowego")
            case '2':
                print('Wybrano kombinacje z powtórzeniami\n')
                n = int(input('Wprowadź liczbę wszystkich elementów w zbiorze (n): '))
                k = int(input('Wprowadź liczbę elementów w podzbiorze (k): '))

                comb_count = comb_with_rep(n, k)
                print(
                    f"Istnieje {int(comb_count)} {k}-elementowych kombinacji z powtórzeniami zbioru {n}-elementowego")
            case '3':
                print('Wybrano wariacje bez powtórzeń\n')
                n = int(input('Wprowadź liczbę wszystkich elementów w zbiorze (n): '))
                k = int(input('Wprowadź liczbę elementów w ciągu (k): '))

                variations_count = variations_without_rep(n, k)
                print(
                    f"Istnieje {int(variations_count)} {k}-elementowych wariacji bez powtórzeń zbioru {n}-elementowego")
            case '4':
                print('Wybrano wariacje z powtórzeniami\n')
                n = int(input('Wprowadź liczbę wszystkich elementów w zbiorze (n): '))
                k = int(input('Wprowadź liczbę elementów w ciągu (k): '))

                variations_count = variations_with_rep(n, k)
                print(
                    f"Istnieje {int(variations_count)} {k}-elementowych wariacji z powtórzeniami zbioru {n}-elementowego")
            case '5':
                print('Wybrano 5')
            case '6':
                print('Wybrano 6')
            case '7':
                print('Wybrano 7 (Stirlinga)')
            case 'exit':
                sys.exit('Program zakończył działanie')
            case _:
                print('Nie dokonano poprawnego wyboru (wpisz numer)')
    except ValueError:
        print('Błąd! Wprowadzone dane muszą być liczbami całkowitymi')
        continue
    except NonPositiveNaturalNumber:
        print('Błąd! Wprowadzone liczby muszą być naturalne i dodatnie')
