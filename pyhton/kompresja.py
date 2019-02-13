#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kompresja.py
#  


def main(args):
    Vk = input("Rozmiar danych skompresowanych: ")
    Vnk = input("Rozmiar danych nieskompresowanych: ")
    
    print("Dane zmniejszyły się o: ", współczynnik1(Vk, Vnk))
    print("Zaoszczędzone miejsce: ") współczynnik2(Vk, Vnk))
     
 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
