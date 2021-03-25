#include <iostream>
#include <string>
#include <fstream>
#include <malloc.h>
using namespace std;


#ifndef MACIERZE_MATRIX_H
#define MACIERZE_MATRIX_H


class Matrix {
private:
    double **value;
    unsigned int row;
    unsigned int col;
    void rowADD(unsigned int dest, double multiplier, unsigned int from);//(dest) = (dest) + (multiplier)*(from)
    void rowChange(unsigned int row1, unsigned int row2);//for changing places of rows
    public:
    Matrix(unsigned int ROW, unsigned int COL, double **values = nullptr);
    Matrix operator+(Matrix const &B);
    Matrix operator-(Matrix const &B);
    Matrix operator*(Matrix const &B);
    Matrix operator^(int pow);
    void print();
    double det();//wyznacznik
    bool capable(Matrix const &B, char function);//'+','-','*','^'//TODO: fuction to make sure an operation is possible
    bool is_square();
    void inverse();
};


#endif //MACIERZE_MATRIX_H
