import PySimpleGUI as sg

layout = [     [sg.Text("Test")],
               [sg.Button("Exit")],
               [sg.InputText()]]

title = "Matrix calculator"

window = sg.Window(title, layout, margins = (300, 200))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()
