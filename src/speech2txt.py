import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
class VoiceModule:
    def record_text():
        while(1):
            try:
                #use the microphone as a source for input
                with sr.Microphone() as source2:
                    #prepare recognizer to recive input
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    
                    #listens for the user's input
                    audio2=r.listen(source2)
                    
                    #using google to recognize audio
                    MyText=r.recognize_google(audio2)
                    
                    
                    
                    
                    
                    
                    
                    
            except sr.RequestError as e:
                print("Could not request results: {0}".format(e))
            except sr.UnknownValueError as e:
                print(e)
                print("unknown error occurred")
                
                
        return
    def output_text(text):
        f=open("output.txt","a")
        f.write(text)
        f.write("\n")
        f.close()
    
        return
    while(1):
        text=record_text()
        output_text(text)
        print("Wrote text")
def main():
    vm=VoiceModule()
    vm.record_text()
    vm.output_text("hello")
    
    #pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    #app=Controller()
    #app.mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
