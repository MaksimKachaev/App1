import PySimpleGUI as sg

feetInches = [[sg.Text('Enter feet'), sg.InputText()],
              [sg.Text('Enter inches'), sg.Input()],
              [sg.Button("Convert")]]

window = sg.Window("Convertor", feetInches)
window.read()
window.close()



