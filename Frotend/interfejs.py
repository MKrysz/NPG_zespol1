import PySimpleGUI as sg

#stuff inside the window
sg.theme('LightGrey1')

layout = [ [sg.Text('Enter 3x3 matrix')],
           [sg.Input(size=(4, 1), key=(1, 1), do_not_clear=False), sg.Input(size=(4, 10), key=(1, 2)), sg.Input(size=(4,10), key=(1, 3))], #macierz wejściowa
           [sg.Input(size=(4, 10), key=(2, 1)), sg.Input(size=(4, 10), key=(2, 2)), sg.Input(size=(4,10), key=(2, 3))],
           [sg.Input(size=(4, 10), key=(3, 1)), sg.Input(size=(4, 10), key=(3, 2)), sg.Input(size=(4,10), key=(3, 3))],
           [sg.Button('='), sg.Button('Submit'), sg.Button('Exit')], #przyciski, usunąć 'Submit'1   2
           [sg.Text(key='-OUTPUT11-', size=(2, 1)), sg.Text(key='-OUTPUT12-', size=(2, 1)), sg.Text(key='-OUTPUT13-', size=(2, 1))], #wynik ale ograniczony do 1 cyfry
           [sg.Text(key='-OUTPUT21-', size=(2, 1)), sg.Text(key='-OUTPUT22-', size=(2, 1)), sg.Text(key='-OUTPUT23-', size=(2, 1))],
           [sg.Text(key='-OUTPUT31-', size=(2, 1)), sg.Text(key='-OUTPUT32-', size=(2, 1)), sg.Text(key='-OUTPUT33-', size=(2, 1))],
           [sg.Button('<'), sg.Button('>')]
           ]

#creating a window
window = sg.Window('Matrix calculator', layout, margins = (100, 100))

while True:
    #odczytanie wartości z komórek
    event, values = window.read()

    #wyjścia
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    #ułomne drukowanie na konsoli po naciśnięciu 'Submit', nie wiem jak zrobić w jednym rzędzie, do usunięcia
    if event == 'Submit':
        for i in range(1, 4):
                print(values[i, 1], values[i, 2], values[i, 3])

    #Jeszcze bardziej ułomne wypisywanie macierzy po naciśnięciu '='. Jak zapisać to bardziej zwięźle?
    if event == '=':
        window['-OUTPUT11-'].update(values[1, 1]), window['-OUTPUT12-'].update(values[1, 2]), window['-OUTPUT13-'].update(values[1, 3])
        window['-OUTPUT21-'].update(values[2, 1]), window['-OUTPUT22-'].update(values[2, 2]), window['-OUTPUT23-'].update(values[2, 3])
        window['-OUTPUT31-'].update(values[3, 1]), window['-OUTPUT32-'].update(values[3, 2]), window['-OUTPUT33-'].update(values[3, 3])

        #czyszczenie komórek w pętli dopiero po wciśnięciu '=', ustawić podczas tworzenia elementów do_not_clear=False
        for i in range(1, 4):
            for j in range(1, 4):
                window[(i, j)].update('')


window.close()
