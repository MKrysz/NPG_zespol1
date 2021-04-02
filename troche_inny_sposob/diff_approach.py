import numpy as np
import PySimpleGUI as sg

matrix1 = []
matrix2 = []


def transform():

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
          [sg.Button('Add'), sg.Button('Print')],
          [sg.Button('Clean'), sg.Button('Mem')]]

window = sg.Window('Kalkulator 2x2', layout)

while True: #FIXME: Poszczegolne operacje dozwolone tylko na macierzach odpowiedniego wymiaru
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Mem':
        layout2 = [[sg.Text('Wybierz, do ktorej komorki zapisac wynik')],
                  [sg.Button('1'), sg. Button('2')]]
        window2 = sg.Window('Wybierz komorke pamieci', layout2)

        event2, values2 = window2.read()    #TODO: event2, values2, window2 - do reformatu, żeby nazwy zmiennych bardziej odzwierciedlały czego dotyczą
        if event2 == '1':
            komorka_mem = 1
            if komorka_mem == 1:
                matrix1 = transform()
                window2.close()
        elif event2 == '2':
            komorka_mem = 2
            if komorka_mem == 2:
                matrix2 = transform()
                window2.close()
    elif event == 'Print':
        print(matrix1, '\n', matrix2)
    elif event == 'Add':
        layout3 = [[sg.Text('Wybierz macierz z pamieci')],
                   [sg.Button('1'), sg.Button('2')]]

        window3 = sg.Window('Wybierz pierwsza komorke pamieci', layout3)

        event3, values3 = window3.read()    #TODO: event3, values3, window3 - do reformatu, żeby nazwy zmiennych bardziej odzwierciedlały czego dotyczą

        if event3 == '1':
            add_mem_1 = matrix1
            window3.close()
        elif event3 == '2':
            add_mem_1 = matrix2
            window3.close()

        layout4 = [[sg.Text('Wybierz macierz z pamieci')],
                   [sg.Button('1'), sg.Button('2')]]

        window4 = sg.Window('Wybierz pierwsza komorke pamieci', layout4)

        event4, values4 = window4.read()    #TODO: event4, values4, window4 - do reformatu, żeby nazwy zmiennych bardziej odzwierciedlały czego dotyczą

        if event4 == '1':
            add_mem_2 = matrix1
            window4.close()
        elif event4 == '2':
            add_mem_2 = matrix2
            window4.close()

        print(np.add(add_mem_1, add_mem_2))

    elif event == 'Clean':  #FIXME: Znalezc sposob na zapobiegniecie sytuacji,
                            #   gdzie po wyczyszczeniu komorki pamieci wymiar macierzy spada do 0 - wypelnienie macierzy zerami?
        layout5 = [[sg.Text('Wybierz macierz z pamieci do wyczyszczenia')],
                   [sg.Button('1'), sg.Button('2')]]

        window5 = sg.Window('Wybierz komorke pamieci', layout5)

        event5, values5 = window5.read()    #TODO: event5, values5, window5 - do reformatu, żeby nazwy zmiennych bardziej odzwierciedlały czego dotyczą

        if event5 == '1':
            matrix1 = []
            window5.close()
        elif event5 == '2':
            matrix2 = []
            window5.close()
            #TODO: odejmowanie, mnożenie, dzielenie, potegowanie, pierwiastek tablicowy - opt., wyznacznik macierzy
            #   wiecej komorek pamieci i rozszerzenie funkcji o mozliwosc ich uzywania
            #   mozliwosc zapisywania do pliku - opt.
window.close()
