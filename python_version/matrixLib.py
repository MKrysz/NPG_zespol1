import numpy as nmp


def matrixCreate(row, col):


    print("Enter your numbers in a single line, each separated by a spacebar:\n")

    numbers = list(map(int, input().split()))
    matrix = nmp.array(numbers).reshape(row, col)
    return matrix

def main(): #tutaj w mainie tylko demonstracja jak działają funkcje - docelowo działanie będzie raczej w głównym pliku programu, a to będzie załączane jako dodatkowa biblioteka
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))

    matrix1 = matrixCreate(row, col)
    matrix2 = matrixCreate(row, col)

    addedMatrix = nmp.add(matrix1, matrix2)
    print(addedMatrix)
    return 0

main()
