import PySimpleGUI as sg

# Add some color
# to the window
sg.theme('SandyBeach')

# Very basic window.
# Return values using
# automatic-numbered keys

col_buttons_layout = [
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('+'), sg.Button('.-')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*'), sg.Button('/')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('.*'), sg.Button('./')],
    [sg.Button(','), sg.Button('0'), sg.Button('-'), sg.Button('^-1'), sg.Button('det')],
    [sg.Button('='), sg.Button('^x')]

]

col_text_layout = [
    [sg.Multiline()],
    [sg.Output()]
]


layout = [
    [sg.SaveAs(), sg.FileBrowse()],
    [sg.Column(col_text_layout), sg.Column(col_buttons_layout)]
]

window = sg.Window('Kalkulator macierzowy',layout)

while True:
    event, values = window.read()

    # The input data looks like a simple list
    # when automatic numbered
    print(values)
    if event == '=' or event == "":
        sg.Submit()
        print(values)
    if event == sg.WIN_CLOSED:
        break