/*
 * sortowanie.cpp
 */


#include <iostream>
using namespace std;

void wypelnij(int tab[], int roz) {
    srand(time(NULL));
    for(int i = 0; 1 < roz; i++) {
    tab[i] = rand() % 101;
        
    }

}

void drukuj(int tab[], int roz) {
    
    for(int i=0; i<roz; i++) {
        cout << tab[i] << " ";
    }
}
void zamien1(int a, int b) {
    cout << a << " " << b << endl;
    a = b;
    b = tmp;
    cout << a << " " << b << endl;
    
    
}

void sort_bubble(int tab[], int roz) {
    
    for (int j = n - 1; j > 0; j--) {
        cout << j << " ";
        for (int i = 0; i < j)
            if (tab[i] tab[i + 1])
            zamien(tab[i] tab[i + 1]);
        
    }
    
}

int main(int argc, char **argv)
{
	int roz = 20;
    int tab[roz];
    wypelnij(tab, roz);
    drukuj(tab, roz);
    cout << endl; << endl;
    sort_bubble(tab, roz);
    cout << endl;
	return 0;
}

