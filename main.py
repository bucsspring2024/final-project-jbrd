
from src.interface import Controller
#import your controller

def main():
    
    #Create an instance on your controller object
    #Call your mainloop
    app=Controller()
    app.mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
