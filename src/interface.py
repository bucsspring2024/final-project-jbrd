import PySimpleGUI as sg
from textInput import TextInput 
from engine import searchEngine

sg.theme('DarkGrey5')   # Add a touch of color
# All the stuff inside your window.
layout = [ 
            [sg.Text('Enter Your Search'), sg.InputText()],
            [sg.Button('Search'), sg.Button('Close Window')],
]

# Create the Window
window = sg.Window('Search', layout).Finalize()
#window.Maximize()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Close Window'): # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    string=values[0]
    searchEngine.search(values[0])

window.close()
if values[0]!="":
    window.close()
    

event, values = sg.Window('Choose an option', [[sg.Text('Select one->'), sg.Listbox(['Option a', 'Option b', 'Option c'], size=(20, 3), key='LB')],
    [sg.Button('Ok'), sg.Button('Cancel')]]).read(close=True)

if event == 'Ok':
    sg.popup(f'You chose {values["LB"][0]}')
else:
    sg.popup_cancel('User aborted')