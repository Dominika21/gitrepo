#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  

def main(args):
    a = int(input("Podaj 1 bok prostokąta: "))
    b = int(input("Podaj 2 bok prostokąta: "))
    znak = input("Podaj znak: ")
    for i in range(a):
        for j in range(b):
            print(znak, end='')
        print()
    
    a = int(input("Podaj 1 bok prostokąta: "))
    b = int(input("Podaj 2 bok prostokąta: "))
    znak = input("Podaj znak: ")
    for i in range(a):
        for j in range(b):
            if j == 0  or j == b - 1:
                print(znak, end='')
            else
                print('',end='')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
