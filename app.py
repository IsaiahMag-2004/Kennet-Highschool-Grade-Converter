import PySimpleGUI as sg
from main import grade_converter

layout = [
    [sg.Text("Score: "), sg.Input(key="-INPUT-")],
    [sg.Button("Convert", key="-BUTTON-")],
    [sg.Text("Grade: "), sg.Text(" ", key="-GRADE-")]
]

sg.theme('reddit')
window = sg.Window("Grade Converter", layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "-BUTTON-":
        score = float(values["-INPUT-"])
        window["-GRADE-"].update(grade_converter(score))

window.close()



