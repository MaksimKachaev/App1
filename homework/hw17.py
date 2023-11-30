import PySimpleGUI as sg

sg.theme("DarkAmber")

feet_label = sg.Text()
feet_input = sg.Input(key="feet")
inch_label = sg.Text()
inch_input = sg.Input(key="inch")
convert_button = sg.Button("Convert")


layout = [[feet_label, feet_input],
          [inch_label, inch_input],
          [convert_button]]

window = sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    feets = values["feet"]
    inches = values["inch"]
    match event:
        case "Convert":
            convert_to_meters = float(feets) * 0.3048 + float(inches) * 0.0254
            #+ float(inches) * 0,245
            print(convert_to_meters, 'm')
            window['']
            # feet_to_inches = feet_input * 0,3048 layout.i #+ #layout.inch * 0,0254
            # print(feet_to_inches)
        case sg.WIN_CLOSED:
            break

window.close()

#Inches = Feet * 12
#d(m) = d(ft) × 0,3048 + d(in) × 0,0254