import numpy as np
import PySimpleGUI as sg

matrix0 = []
matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []
matrix5 = []
matrix6 = []
matrix7 = []
matrix8 = []
matrix9 = []


def transform():    #Ta funkcja odpowiada za przekształcenie otrzymywanego od GUI słownika na listę, z której tworzona jest macierz, na której operacje wykonuje NumPy
    dictList = list(values.values())

    row1 = []
    row2 = []

    for i in range(0, 2):
        row1.append(dictList[i])
    for j in range(2, 4):
        row2.append(dictList[j])

    arrayList = [row1, row2]

    rt = np.asarray(arrayList, int)

    return rt


sg.theme('Material2')

layout = [[sg.InputText(), sg.InputText()],
          [sg.InputText(), sg.InputText()],
          [sg.Button('Add'), sg.Button('Print'), sg.Button('Multiply')],
          [sg.Button('Clean'), sg.Button('Mem'), sg.Button('Exit')]]

window = sg.Window('Kalkulator 2x2', layout)

while True: #FIXME: Poszczegolne operacje dozwolone tylko na macierzach odpowiedniego wymiaru
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Mem':
        layout_mem = [[sg.Text('Wybierz, do ktorej komorki zapisac wynik')],
                      [sg.Button('0'), sg. Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]
        window_mem = sg.Window('Wybierz komorke pamieci', layout_mem)

        event_mem, values_mem = window_mem.read()
        if event_mem == '0':
            komorka_mem = 0
            if komorka_mem == 0:
                matrix0 = transform()
                window_mem.close()
        elif event_mem == '1':
            komorka_mem = 1
            if komorka_mem == 1:
                matrix1 = transform()
                window_mem.close()
        elif event_mem == '2':
            komorka_mem = 2
            if komorka_mem == 2:
                matrix2 = transform()
                window_mem.close()
        elif event_mem == '3':
            komorka_mem = 3
            if komorka_mem == 3:
                matrix3 = transform()
                window_mem.close()
        elif event_mem == '4':
            komorka_mem = 4
            if komorka_mem == 4:
                matrix4 = transform()
                window_mem.close()
        elif event_mem == '5':
            komorka_mem = 5
            if komorka_mem == 5:
                matrix5 = transform()
                window_mem.close()
        elif event_mem == '6':
            komorka_mem = 6
            if komorka_mem == 6:
                matrix6 = transform()
                window_mem.close()
        elif event_mem == '7':
            komorka_mem = 7
            if komorka_mem == 7:
                matrix7 = transform()
                window_mem.close()
        elif event_mem == '8':
            komorka_mem = 8
            if komorka_mem == 8:
                matrix8 = transform()
                window_mem.close()
        elif event_mem == '9':
            komorka_mem = 9
            if komorka_mem == 9:
                matrix9 = transform()
                window_mem.close()
    elif event == 'Print':
        print(matrix0, '\n', matrix1, '\n', matrix2, '\n', matrix3, '\n', matrix4, '\n', matrix5, '\n', matrix6, '\n', matrix7, '\n', matrix8, '\n', matrix9)
    elif event == 'Add':
        layout_add_mem1 = [[sg.Text('Wybierz macierz z pamieci')],
                           [sg.Button('0'), sg. Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

        window_add_mem1 = sg.Window('Wybierz pierwsza komorke pamieci', layout_add_mem1)

        event_add_mem1, values_add_mem1 = window_add_mem1.read()

        if event_add_mem1 == '0':
            add_mem_1 = matrix0
            window_add_mem1.close()
        elif event_add_mem1 == '1':
            add_mem_1 = matrix1
            window_add_mem1.close()
        elif event_add_mem1 == '2':
            add_mem_1 = matrix2
            window_add_mem1.close()
        elif event_add_mem1 == '3':
            add_mem_1 = matrix3
            window_add_mem1.close()
        elif event_add_mem1 == '4':
            add_mem_1 = matrix4
            window_add_mem1.close()
        elif event_add_mem1 == '5':
            add_mem_1 = matrix5
            window_add_mem1.close()
        elif event_add_mem1 == '6':
            add_mem_1 = matrix6
            window_add_mem1.close()
        elif event_add_mem1 == '7':
            add_mem_1 = matrix7
            window_add_mem1.close()
        elif event_add_mem1 == '8':
            add_mem_1 = matrix8
            window_add_mem1.close()
        elif event_add_mem1 == '9':
            add_mem_1 = matrix9
            window_add_mem1.close()

        layout_add_mem2 = [[sg.Text('Wybierz macierz z pamieci')],
                           [sg.Button('0'), sg. Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

        window_add_mem2 = sg.Window('Wybierz druga komorke pamieci', layout_add_mem2)

        event_add_mem2, values_add_mem2 = window_add_mem2.read()

        if event_add_mem2 == '0':
            add_mem_2 = matrix0
            window_add_mem2.close()
        elif event_add_mem2 == '1':
            add_mem_2 = matrix1
            window_add_mem2.close()
        elif event_add_mem2 == '2':
            add_mem_2 = matrix2
            window_add_mem2.close()
        elif event_add_mem2 == '3':
            add_mem_2 = matrix3
            window_add_mem2.close()
        elif event_add_mem2 == '4':
            add_mem_2 = matrix4
            window_add_mem2.close()
        elif event_add_mem2 == '5':
            add_mem_2 = matrix5
            window_add_mem2.close()
        elif event_add_mem2 == '6':
            add_mem_2 = matrix6
            window_add_mem2.close()
        elif event_add_mem2 == '7':
            add_mem_2 = matrix7
            window_add_mem2.close()
        elif event_add_mem2 == '8':
            add_mem_2 = matrix8
            window_add_mem2.close()
        elif event_add_mem2 == '9':
            add_mem_2 = matrix9
            window_add_mem2.close()

        print(np.add(add_mem_1, add_mem_2)) #   FIXME: "Name 'add_mem_1' / 'add_mem_2' can be undefined" - wynika to z faktu,
                                            #   że jeżeli wybierze się inną opcję, która nie określi definicji w/w zmiennych, to będą niezdefiniowane;
                                            #   chyba nie ma się czym przejmować, bo takiego przypadku nie będzie

    elif event == 'Clean':  #FIXME: Znalezc sposob na zapobiegniecie sytuacji,
                            #   gdzie po wyczyszczeniu komorki pamieci wymiar macierzy spada do 0 - wypelnienie macierzy zerami?
        layout_clean = [[sg.Text('Wybierz macierz z pamieci do wyczyszczenia')],
                        [sg.Button('0'), sg. Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

        window_clean = sg.Window('Wybierz komorke pamieci', layout_clean)

        event_clean, values_clean = window_clean.read()

        if event_clean == '0':
            matrix0 = []
            window_clean.close()
        elif event_clean == '1':
            matrix1 = []
            window_clean.close()
        elif event_clean == '2':
            matrix2 = []
            window_clean.close()
        elif event_clean == '3':
            matrix3 = []
            window_clean.close()
        elif event_clean == '4':
            matrix4 = []
            window_clean.close()
        elif event_clean == '5':
            matrix5 = []
            window_clean.close()
        elif event_clean == '6':
            matrix6 = []
            window_clean.close()
        elif event_clean == '7':
            matrix7 = []
            window_clean.close()
        elif event_clean == '8':
            matrix8 = []
            window_clean.close()
        elif event_clean == '9':
            matrix9 = []
            window_clean.close()

            #TODO: odejmowanie, mnożenie, dzielenie, potegowanie, pierwiastek tablicowy - opt., wyznacznik macierzy
            #   wiecej komorek pamieci i rozszerzenie funkcji o mozliwosc ich uzywania
            #   mozliwosc zapisywania do pliku - opt.
    elif event == 'Multiply':

        layout_mul_mem1 = [[sg.Text('Wybierz macierz z pamieci')],
                           [sg.Button('0'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'),
                            sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

        window_mul_mem1 = sg.Window('Wybierz pierwsza komorke pamieci', layout_mul_mem1)

        event_mul_mem1, values_mul_mem1 = window_mul_mem1.read()

        if event_mul_mem1 == '0':
            mul_mem_1 = matrix0
            window_mul_mem1.close()
        elif event_mul_mem1 == '1':
            mul_mem_1 = matrix1
            window_mul_mem1.close()
        elif event_mul_mem1 == '2':
            mul_mem_1 = matrix2
            window_mul_mem1.close()
        elif event_mul_mem1 == '3':
            mul_mem_1 = matrix3
            window_mul_mem1.close()
        elif event_mul_mem1 == '4':
            mul_mem_1 = matrix4
            window_mul_mem1.close()
        elif event_mul_mem1 == '5':
            mul_mem_1 = matrix5
            window_mul_mem1.close()
        elif event_mul_mem1 == '6':
            mul_mem_1 = matrix6
            window_mul_mem1.close()
        elif event_mul_mem1 == '7':
            mul_mem_1 = matrix7
            window_mul_mem1.close()
        elif event_mul_mem1 == '8':
            mul_mem_1 = matrix8
            window_mul_mem1.close()
        elif event_mul_mem1 == '9':
            mul_mem_1 = matrix9
            window_mul_mem1.close()

        layout_mul_mem2 = [[sg.Text('Wybierz macierz z pamieci')],
                           [sg.Button('0'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'),
                            sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

        window_mul_mem2 = sg.Window('Wybierz pierwsza komorke pamieci', layout_mul_mem2)

        event_mul_mem2, values_mul_mem2 = window_mul_mem2.read()

        if event_mul_mem2 == '0':
            mul_mem_2 = matrix0
            window_mul_mem2.close()
        elif event_mul_mem2 == '1':
            mul_mem_2 = matrix1
            window_mul_mem2.close()
        elif event_mul_mem2 == '2':
            mul_mem_2 = matrix2
            window_mul_mem2.close()
        elif event_mul_mem2 == '3':
            mul_mem_2 = matrix3
            window_mul_mem2.close()
        elif event_mul_mem2 == '4':
            mul_mem_2 = matrix4
            window_mul_mem2.close()
        elif event_mul_mem2 == '5':
            mul_mem_2 = matrix5
            window_mul_mem2.close()
        elif event_mul_mem2 == '6':
            mul_mem_2 = matrix6
            window_mul_mem2.close()
        elif event_mul_mem2 == '7':
            mul_mem_2 = matrix7
            window_mul_mem2.close()
        elif event_mul_mem2 == '8':
            mul_mem_2 = matrix8
            window_mul_mem2.close()
        elif event_mul_mem2 == '9':
            mul_mem_2 = matrix9
            window_mul_mem2.close()

        print(np.multiply(mul_mem_1, mul_mem_2))

window.close()
