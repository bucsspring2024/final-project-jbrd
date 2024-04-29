import PySimpleGUI as sg
import speech_recognition as sr
import pyttsx3 

from src.engine import searchEngine
class Controller:

    def __init__(self):

        sg.theme('DarkGrey5')   # Add a touch of color
    # All the stuff inside your window.
        self.layout = [ 
                [sg.Text('Enter Your Search'), sg.InputText()],
                [sg.Button('Search'),sg.Button('Voice Search'), sg.Button('Close Window') ],
        ]
        # Create the Window
        self.window = sg.Window('Search', self.layout).Finalize()
    def mainloop(self):
        r = sr.Recognizer() 

       
   
# Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = self.window.read()
            if event in (None, 'Close Window'): # if user closes window or clicks cancel
                break
            #If they press the search bar this then closes the window and searches
            elif event in('Search'):
                   
                
                string=values[0]
                searchEngine.search(values[0])

                self.window.Hide()
            #If they select the voice search option this allows them to then use their voice to search
            elif event in ('Voice Search'):
                
                self.window.Hide()
                
                try:
         
            # use the microphone as source for input.
                    with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
                        r.adjust_for_ambient_noise(source2, duration=0.2)
                        #Popup window which allows the user to see that the computer is now listening
                        pop=sg.popup("listening")
                         
                        #listens for the user's input 
                        audio2 = r.listen(source2)
             
                        # Using google to recognize audio
                        MyText = r.recognize_google(audio2)
                        MyText = MyText.lower()
                        
                        
       
        
        
        
             
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
         
                except sr.UnknownValueError as e:
                    print(e, "unknown error occurred")
                #A popup to ask the user if the computer heard them correctly
                select=sg.popup_yes_no("Did you say", MyText)
                if select=="Yes":
                         
                    searchEngine.search(str(MyText))
                else:
                    self.window.UnHide()
                    continue
        
        information = open('duckduck_tutorial.csv')
        print(information)
        #for line in information:
            #print(line)
        
            
      
    

        #event, values = sg.Window('Choose an option', [[sg.Text('Select one->'), sg.Listbox(['Option a', 'Option b', 'Option c'], size=(20, 3), key='LB')],
            #[sg.Button('Ok'), sg.Button('Cancel')]]).read(close=True)

        #if event == 'Ok':
            #sg.popup(f'You chose {values["LB"][0]}')
        #else:
            #sg.popup_cancel('User aborted')