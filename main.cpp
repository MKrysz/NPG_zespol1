#include <iostream>
#include "Matrix.h"
#define SIZE 6

int main() {
    double *x[SIZE];
    double X[SIZE][SIZE] = {{8,2,0,4,5,6},{6,4,2,8,0,7},{9,2,3,1,12,-2},{1,1,1,0,3,8},{1,1,2,3,4,-0.3},{4, 1, -14, -2, 8}};
    for(int i = 0; i<SIZE;i++){
        x[i] = X[i];
    }
    Matrix wynik(SIZE, SIZE, x);
    cout<<"\nWynik:";
    wynik.print();
    printf("\n%lf\n", wynik.det());
    wynik.print();
    return 0;
}