/*
 * fibonacci.cpp
 */


#include <iostream>
using namespace std;

long int fibonacci_it(int n) {
    long int wynik = 0;
    long int a = 0;   
    long int b = 1;
    
    if(n == 0) return a;
    if(n == 1) return b;
    for (int i = 2; i <= n; i++) {
        wynik = a + b;
        a = b;
        b = wynik;
        
    }
    return wynik;
}

long int fibonacci_re(int n) {
 
    if (n == 0);
    if (n == 1);

    return fibonacci_re(n - 1) + fibonacci_re(n - 2);

}
    
int main(int argc, char **argv)
{
	int n;
    cout << "Podaj numer wyrazu ciągu: ";
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu " << n << ":" << endl;
    // dopisac kod wyswitlajacy wszystkie wyrzay ciagu az do wyraz<u n podanego przez urzutkownika
    cout << fibonacci_it(n);
	return 0;
}

