import pyttsx3
import speech_recognition as sr
import datetime
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    elif hour>=16 and hour<20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am louis , welcome to , Latin , to , Devanagari , Converter.")

def clearAll():
    text1_field.delete(1.0, END)
    text2_field.delete(1.0, END)
    
def convert():
    input_text = text1_field.get("1.0", "end")[:-1]
    output_text = transliterate(input_text, sanscript.ITRANS, sanscript.DEVANAGARI)
    text2_field.insert('end -1 chars', output_text)

    
if __name__ == '__main__':
    wishMe()
    root = Tk()
    root.configure(background = 'light pink')
    root.geometry('600x470')
    root.title('Converter')

headlabel = Label(root, text = 'Welcome!\n Latin to Devanagari Converter.', fg = 'black', bg = 'light blue')
headlabel.grid(row = 0, column = 1)
label1 = Label(root, text = 'Latin Text.', fg = 'black', bg = 'light yellow')
label1.grid(row = 1, column = 0, padx = 10, pady = 10)

label2 = Label(root, text = 'Devanagiri Text.', fg = 'black', bg = 'light yellow')
label2.grid(row = 3, column = 0, padx = 10, pady = 10)

text1_field = Text(root,height = 7, width = 35,font = 'lucida 15')
text1_field.grid(row = 1, column = 1, padx = 10, pady = 10)
text2_field = Text(root,height = 7, width = 35,font = 'lucida 15')
text2_field.grid(row = 3, column = 1, padx = 10, pady = 10)

btn1 = Button(root, text = 'Contert to Devanagiri Text.', bg = 'red', fg = 'yellow', command = convert)
btn1.grid(row = 2, column = 1)

btn2 = Button(root, text = 'Clear.', bg = 'red', fg = 'yellow', command = clearAll)
btn2.grid(row = 4, column = 1)

root.mainloop()
