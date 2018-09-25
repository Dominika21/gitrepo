#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-for.py
  
#jupyter-qtconsole



def main(args):
    start = int(input("Podaj liczbę 1: "))
    stop = int(input("Podaj liczbę 2: "))
    
    while start >= stop:
         print("Za mała druga liczba ")
         stop = int(input("Podaj liczbę 2: "))
             
         
    
    if start >= stop:
        print("Błędne dane!")
        exit(0)
     
    for i in range(start,stop + 1):
        if i % 2 == 0:
            print(i)
        else:
            print("Liczba nieparzysta")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
