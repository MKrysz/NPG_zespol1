#include "Matrix.h"

Matrix::Matrix(unsigned int ROW, unsigned int COL, double **values) {
    row = ROW;
    col = COL;
    if(!values){
        value = new double*[row];
        for(int i = 0; i < row; i++){
            value[i] = new double[col];
            for(int j = 0; j < col; j++){
                if(i == j){
                    value[i][j] = 1;
                }
                else{
                    value[i][j] = 0;
                }
            }
        }
    }
    else{
        value = values;
    }
}

void Matrix::print() {
    for(int i = 0; i < row; i++){
        cout<<'\n';
        for(int j = 0; j < col; j++){
            printf("%.2lf\t", value[i][j]);
        }
    }
    cout<<"\n--------------------------------------";
}

Matrix Matrix::operator+(const Matrix &B) {
    Matrix result(row, col);
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            result.value[i][j] = value[i][j] + B.value[i][j];
        }
    }
    return result;
}

Matrix Matrix::operator-(const Matrix &B) {
    Matrix result(row, col);
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            result.value[i][j] = value[i][j] - B.value[i][j];
        }
    }
    return result;
}

Matrix Matrix::operator*(const Matrix &B) {
    Matrix result(row, B.col);
    for(unsigned int i = 0; i < row; i++){
        for(unsigned int j = 0; j < B.col; j++){
            result.value[i][j] = 0;
            for(unsigned int k = 0; k < col; k++){
                result.value[i][j] += value[i][k] *  B.value[k][j];
            }
        }
    }
    return result;
}

Matrix Matrix::operator^(const int pow) {
    Matrix result(row, col);
    Matrix buf(row, col);
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            buf.value[i][j] = value[i][j];
        }
    }
    if(pow == 0){
        return result;
    }
    if(pow > 0){
        for(int i = 0; i < pow; i++){
            result = result * buf;
        }
    }
    return result;
}

void Matrix::rowADD(unsigned int dest, double multiplier, unsigned int from) {
    for(int i = 0; i < col; i++){
        value[dest][i] = value[dest][i] + multiplier*value[from][i];
    }
}

double Matrix::det() {//TODO: make sure you don't divide by zero
    double buffer[row][col];//for storing the values of the matrix
    double buf = 0;//for checking whether the determinant isn't obvious zero
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            buf += value[i][j];
        }
        if(buf == 0){
            return 0;
        }
        buf = 0;
    }//checking whether the entire row isn't filled by zeros
    for(int i = 0; i < col; i++){
        for(int j = 0; j < row; j++){
            buf += value[j][i];
        }
        if(buf == 0){
            return 0;
        }
        buf = 0;
    }//checking whether the entire col isn't filled by zeros
    for(int i = 0; i < row; i++){
        buf += value[i][i];
    }
    if(buf == 0){
        return 0;
    }//checking whether the diagonal isn't filled by zeros
    for(int i = 0; i < row; i++){
        buf += value[i][row-i];
    }
    if(buf == 0){
        return 0;
    }//checking whether the other diagonal isn't filled by zeros
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            buffer[i][j] = value[i][j];
        }
    }//make a copy of values of the matrix
    for(int i = 0; i < col; i++){
        for (int j = 1+i; j < row; j++) {
            if(value[i][i]==0){
                for(int k = i+1; k < row; k++){
                    if(value[k][i]!=0){//TODO:zero-proof determinant function
                        rowChange(i, k);
                    }
                }
            }
            else{
                rowADD(j, -value[j][i]/value[i][i], i);
            }
        }
    }//make the matrix upper triangle matrix
    double result = 1;
    for(int i = 0; i < row; i++){
        result *= value[i][i];
    }//calculate determinant of the matrix
    print();
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            value[i][j] = buffer[i][j];
        }
    }//put values from buffer back into the matrix
    return result;
}

bool Matrix::is_square() {
    return (row==col);
}

void Matrix::rowChange(unsigned int row1, unsigned int row2) {
    double buffer;
    for(int i  = 0; i < col; i++){
        buffer = value[row1][i];
        value[row1][i] = value[row2][i];
        value[row2][i] = buffer;
    }
}
