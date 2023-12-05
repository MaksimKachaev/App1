import PySimpleGUI as Sg
from converters import convert

feet_label = Sg.Text("Enter feet:")
feet_input = Sg.Input(key="feets")

inch_label = Sg.Text("Enter inches")
inch_input = Sg.Input(key="inches")

convert_button = Sg.Button("Convert")
update_output = Sg.Text(key="output")

layout = [[feet_label, feet_input],
          [inch_label, inch_input],
          [convert_button, update_output]]

window = Sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    feet = float(values["feets"])
    inch = float(values["inches"])
    convertor = convert(feet, inch)
    window['output'].update(value=f"{convertor} m", text_color="white")
    if Sg.WIN_CLOSED:
        break
window.close()

