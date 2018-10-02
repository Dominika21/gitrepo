#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-cw2.py
#  


def main(args):
    n = int(input("Podaj liczbę n: "))
    while n < 1: 
        print("Błędne dane! ")
        n = int(input("Podaj liczbę n: "))
        
    m = int(input("Podaj liczbę m: "))   
    while m <= n: 
         print("Błędne dane! ")
         m = int(input("Podaj liczbę m: "))   
         
    for liczba in range (n, m +1):
        print(liczba, " ", end="")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
