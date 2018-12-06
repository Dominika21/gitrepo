/*
 * potega.cpp
 */


#include <iostream>

int potega_it(int a, int n) {
    int wynik = 1;
    for(int i = 0; i < n  ; i++) {
        wynik  *= a;
    
    }
    return wynik;
}

int potega_re(int a, int n) {
    if (n == 1)  return 1;
    return potega_re(a, n-1) * a;
   
    
    
    
}
    

int main(int argc, char **argv)
{
	int a, n;
    cout << "Podaj podstawę i wykładnik: ";
    cin >> a >> n;
    cout << "Potęga: " << potęga_it(a, n) << endl;
	return 0;
}

