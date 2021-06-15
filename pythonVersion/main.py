#main
import numpy as np
import PySimpleGUI as sg

matrix0 = np.asarray([[0,0],[0,0]])
matrix1 = np.asarray([[0,0],[0,0]])
matrix2 = np.asarray([[0,0],[0,0]])
matrix3 = np.asarray([[0,0],[0,0]])
matrix4 = np.asarray([[0,0],[0,0]])
matrix5 = np.asarray([[0,0],[0,0]])
matrix6 = np.asarray([[0,0],[0,0]])
matrix7 = np.asarray([[0,0],[0,0]])
matrix8 = np.asarray([[0,0],[0,0]])
matrix9 = np.asarray([[0,0],[0,0]])


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
          [sg.Button('Add'), sg.Button('Print'), sg.Button('Multiply'), sg.Button('Subtract')],
          [sg.Button('Clean'), sg.Button('Mem'), sg.Button('Exit'), sg.Button('scDiv')]]

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
        print(matrix0, '\n', matrix1, '\n', matrix2, '\n', matrix3, '\n', matrix4, '\n', matrix5, '\n', matrix6, '\n', matrix7, '\n', matrix8, '\n', matrix9, '\n\n\n')
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

        print(np.add(add_mem_1, add_mem_2))

    elif event == 'Clean':
        layout_clean = [[sg.Text('Wybierz macierz z pamieci do wyczyszczenia')],
                        [sg.Button('0'), sg. Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

        window_clean = sg.Window('Wybierz komorke pamieci', layout_clean)

        event_clean, values_clean = window_clean.read()

        if event_clean == '0':
            matrix0 = np.asarray([[0,0],[0,0]])
            window_clean.close()
        elif event_clean == '1':
            matrix1 = np.asarray([[0,0],[0,0]])
            window_clean.close()
        elif event_clean == '2':
            matrix2 = np.asarray([[0,0],[0,0]])
            window_clean.close()
        elif event_clean == '3':
            matrix3 = np.asarray([[0,0],[0,0]])
            window_clean.close()
        elif event_clean == '4':
            matrix4 = np.asarray([[0,0],[0,0]])
            window_clean.close()
        elif event_clean == '5':
            matrix5 = np.asarray([[0,0],[0,0]])
            window_clean.close()
        elif event_clean == '6':
            matrix6 = np.asarray([[0,0],[0,0]])
            window_clean.close()
        elif event_clean == '7':
            matrix7 = np.asarray([[0,0],[0,0]])
            window_clean.close()
        elif event_clean == '8':
            matrix8 = np.asarray([[0,0],[0,0]])
            window_clean.close()
        elif event_clean == '9':
            matrix9 = np.asarray([[0,0],[0,0]])
            window_clean.close()

            #TODO: potegowanie, wyznacznik macierzy
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

    elif event == 'Subtract':

        layout_sub_mem1 = [[sg.Text('Wybierz macierz z pamieci')],
                           [sg.Button('0'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'),
                            sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

        window_sub_mem1 = sg.Window('Wybierz pierwsza komorke pamieci', layout_sub_mem1)

        event_scDiv_mem1, values_sub_mem1 = window_sub_mem1.read()

        if event_scDiv_mem1 == '0':
            sub_mem_1 = matrix0
            window_sub_mem1.close()
        elif event_scDiv_mem1 == '1':
            sub_mem_1 = matrix1
            window_sub_mem1.close()
        elif event_scDiv_mem1 == '2':
            sub_mem_1 = matrix2
            window_sub_mem1.close()
        elif event_scDiv_mem1 == '3':
            sub_mem_1 = matrix3
            window_sub_mem1.close()
        elif event_scDiv_mem1 == '4':
            sub_mem_1 = matrix4
            window_sub_mem1.close()
        elif event_scDiv_mem1 == '5':
            sub_mem_1 = matrix5
            window_sub_mem1.close()
        elif event_scDiv_mem1 == '6':
            sub_mem_1 = matrix6
            window_sub_mem1.close()
        elif event_scDiv_mem1 == '7':
            sub_mem_1 = matrix7
            window_sub_mem1.close()
        elif event_scDiv_mem1 == '8':
            sub_mem_1 = matrix8
            window_sub_mem1.close()
        elif event_scDiv_mem1 == '9':
            sub_mem_1 = matrix9
            window_sub_mem1.close()

        layout_sub_mem2 = [[sg.Text('Wybierz macierz z pamieci')],
                           [sg.Button('0'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'),
                            sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

        window_sub_mem2 = sg.Window('Wybierz pierwsza komorke pamieci', layout_sub_mem2)

        event_sub_mem2, values_sub_mem2 = window_sub_mem2.read()

        if event_sub_mem2 == '0':
            sub_mem_2 = matrix0
            window_sub_mem2.close()
        elif event_sub_mem2 == '1':
            sub_mem_2 = matrix1
            window_sub_mem2.close()
        elif event_sub_mem2 == '2':
            sub_mem_2 = matrix2
            window_sub_mem2.close()
        elif event_sub_mem2 == '3':
            sub_mem_2 = matrix3
            window_sub_mem2.close()
        elif event_sub_mem2 == '4':
            sub_mem_2 = matrix4
            window_sub_mem2.close()
        elif event_sub_mem2 == '5':
            sub_mem_2 = matrix5
            window_sub_mem2.close()
        elif event_sub_mem2 == '6':
            sub_mem_2 = matrix6
            window_sub_mem2.close()
        elif event_sub_mem2 == '7':
            sub_mem_2 = matrix7
            window_sub_mem2.close()
        elif event_sub_mem2 == '8':
            sub_mem_2 = matrix8
            window_sub_mem2.close()
        elif event_sub_mem2 == '9':
            sub_mem_2 = matrix9
            window_sub_mem2.close()

        print(np.subtract(sub_mem_1, sub_mem_2))

    elif event == 'scDiv':

        layout_scDiv_mem1 = [[sg.Text('Wybierz macierz z pamieci')],
                             [sg.Button('0'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'),
                              sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

        window_scDiv_mem1 = sg.Window('Wybierz pierwsza komorke pamieci', layout_scDiv_mem1)

        event_scDiv_mem1, values_scDiv_mem1 = window_scDiv_mem1.read()

        if event_scDiv_mem1 == '0':
            scDiv_mem_1 = matrix0
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == '1':
            scDiv_mem_1 = matrix1
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == '2':
            scDiv_mem_1 = matrix2
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == '3':
            scDiv_mem_1 = matrix3
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == '4':
            scDiv_mem_1 = matrix4
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == '5':
            scDiv_mem_1 = matrix5
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == '6':
            scDiv_mem_1 = matrix6
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == '7':
            scDiv_mem_1 = matrix7
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == '8':
            scDiv_mem_1 = matrix8
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == '9':
            scDiv_mem_1 = matrix9
            window_scDiv_mem1.close()
        elif event_scDiv_mem1 == sg.WIN_CLOSED:
            window_scDiv_mem1.close()

        if event_scDiv_mem1 not in (sg.WIN_CLOSED, 'Exit'): #warunek, który powoduje nieotwieranie się okna wyboru,
                                                            #między dzieleniem przez skalar a dzieleniem tablicowym
                                                            #macierzy, gdy nie zostanie wybrana macierz do podzielenia
            layout_scDiv_choice = [[sg.Text('Do you wish to divide by a matrix, or by a scalar?')],
                                   [sg.Button('Matrix')], [sg.Button('Scalar')]]

            window_scDiv_choice = sg.Window('Kalkulator 2x2', layout_scDiv_choice)

            event_scDiv_choice, values_scDiv_choice = window_scDiv_choice.read()

            if event_scDiv_choice == 'Matrix':
                layout_scDiv_mem2 = [[sg.Text('Wybierz macierz z pamieci')],
                                     [sg.Button('0'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'),
                                      sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9')]]

                window_scDiv_mem2 = sg.Window('Wybierz pierwsza komorke pamieci', layout_scDiv_mem2)

                event_scDiv_mem2, values_scDiv_mem2 = window_scDiv_mem2.read()

                if event_scDiv_mem2 == '0':
                    scDiv_mem_2 = matrix0
                    window_scDiv_mem2.close()
                elif event_scDiv_mem2 == '1':
                    scDiv_mem_2 = matrix1
                    window_scDiv_mem2.close()
                elif event_scDiv_mem2 == '2':
                    scDiv_mem_2 = matrix2
                    window_scDiv_mem2.close()
                elif event_scDiv_mem2 == '3':
                    scDiv_mem_2 = matrix3
                    window_scDiv_mem2.close()
                elif event_scDiv_mem2 == '4':
                    scDiv_mem_2 = matrix4
                    window_scDiv_mem2.close()
                elif event_scDiv_mem2 == '5':
                    scDiv_mem_2 = matrix5
                    window_scDiv_mem2.close()
                elif event_scDiv_mem2 == '6':
                    scDiv_mem_2 = matrix6
                    window_scDiv_mem2.close()
                elif event_scDiv_mem2 == '7':
                    scDiv_mem_2 = matrix7
                    window_scDiv_mem2.close()
                elif event_scDiv_mem2 == '8':
                    scDiv_mem_2 = matrix8
                    window_scDiv_mem2.close()
                elif event_scDiv_mem2 == '9':
                    scDiv_mem_2 = matrix9
                    window_scDiv_mem2.close()
                print(np.divide(scDiv_mem_1, scDiv_mem_2))
                window_scDiv_choice.close()
            elif event_scDiv_choice == 'Scalar':

                layout_scDiv_sc = [[sg.Text('Input a scalar')], [sg.InputText()],
                                   [sg.Button('OK')], [sg.Button('Cancel')]]

                window_scDiv_sc = sg.Window('Kalkuator 2x2', layout_scDiv_sc)

                event_scDiv_sc, values_scDiv_sc = window_scDiv_sc.read()

                if event_scDiv_sc == 'OK':
                    scDiv_mem_2 = int(values_scDiv_sc[0])
                    window_scDiv_sc.close()
                    with np.nditer(scDiv_mem_1, op_flags=['readwrite']) as it:  #np.ndinter - funkcja do łatwej iteracji po macierzy jako liście list, flaga 'readwrite' oznacza zamianę elementów macierzy zgodnie z daną instrukcją, zawartą w pętli for
                        for x in it:
                            x[...] = x / scDiv_mem_2
                    print(scDiv_mem_1)
                elif event_scDiv_sc == sg.WINDOW_CLOSED or event_scDiv_sc == 'Cancel':
                    window_scDiv_sc.close()
                window_scDiv_choice.close()

window.close()

#TODO: znaleźć sposób na zapisywanie wyników obliczeń do komórek pamięci - może zapisywanie do pliku?   -   stworzony słownik
#FIXME: poprawić wyświetlane w okienkach tekstowych instrukcje dla użytkownika
