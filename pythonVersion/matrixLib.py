import numpy as nmp
 

def matrixCreate(row, col):

    matrix = []

    print("Enter your numbers in a single line, each separated by a spacebar:\n")

    numbers = list(map(int, input().split()))
    matrix = nmp.array(numbers).reshape(row, col)
    return matrix

def matrixAdd(matrix1, matrix2):
    return nmp.add(matrix1, matrix2)

def matrixSubt(matrix1, matrix2):
    return nmp.subtract(matrix1, matrix2)

def matrixMul(matrix1, matrix2):
    return nmp.multiply(matrix1, matrix2)
 
def matrixDet(matrix1):
    return matrix1[0][0]*matrix1[1][1] - matrix1[0][1]*matrix1[1][0]
