#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py
#  
#liczba = 265, suma = 13
#napisz program, ktory sumuje cyfry podanej liczby minimum dwucyfrowej i wyświetla ich sumę w terminalu.
# np. 8463, suma = 21
def sumaj_cyfry1(liczba):
         
    suma = 0 
        
    while liczba > 0:
        suma = suma + (liczba % 10)
        liczba = int(liczba / 10)
        

def main(args):

    liczba = input("Podaj liczbę minimum dwucyfrową: ")
    liczba = int(liczba)
    while liczba < 10:
        liczba = input("Podaj liczbę minimum dwucyfrową: ")
        liczba = int(liczba)
        
    suma = 0 
        
    while liczba > 0:
        suma = suma + (liczba % 10)
        liczba = int(liczba / 10)
        
    print("Suma:", suma)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
