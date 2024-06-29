from language_selection.language_selection import language
import pyttsx3 as pt

class main:
    def __init__(self):
        self.engine = pt.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('rate', 160)
        self.engine.setProperty('voice', self.voices[1].id) 
        return self.mainFunc()
        
    def mainFunc(self):
        self.condition = True
        self.engine.say("Please Choose Your Language")
        self.engine.runAndWait()
        choices = language().language_choices()
        for i in range(len(choices)):
            self.engine.say(f"{i+1} for {choices[i]}")
            self.engine.runAndWait()
        choice = input("Select Your language: ")
            
        
            

main()

