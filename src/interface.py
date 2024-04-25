import PySimpleGUI as sg

sg.theme('grey')   # Add a touch of color
# All the stuff inside your window.
layout = [ 
            [sg.Text('Enter Your Search'), sg.InputText()],
            [sg.Button('Search')],
]

# Create the Window
window = sg.Window('Test', layout).Finalize()
#window.Maximize()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Search'): # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
