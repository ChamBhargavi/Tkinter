import tkinter
from tkinter import *


class Test():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("250x100")
        self.text = StringVar()
        self.text.set("Original Text")
        self.buttonA = Button(self.root, textvariable=self.text)
        self.buttonA.configure(text="test")

        self.buttonB = Button(self.root,
                                text="Click to change text",
                                command=self.changeText
                              )
        self.buttonA.pack(side=LEFT)
        self.buttonB.pack(side=RIGHT)
        self.root.mainloop()

    def changeText(self):
        self.text.set("Updated Text")

app=Test()