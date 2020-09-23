#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nombre = input('donner un nombre ')
    nombre_entier = float(nombre)
    valeur_absolue = abs(nombre_entier)
    print(valeur_absolue)
    return valeur_absolue


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    Les_noms = 0
    for i in (prefixes):
        print(i + suffixes)

    return [letter + suffixes for letter in prefixes]


def prime_integer_summation() -> int:
    somme = 0
    for i in range(1,100,1):
        if i%2!=0:
            somme += i
        else:
            continue

    return somme


def factorial(number: int) -> int:
    for i in range(number,1, -1):
        factorial = i*(i-1)
    return factorial


def use_continue() -> None:
    for i in range(1,10,1):
        if i == 5:
            continue
        else:
            print(i)




def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
