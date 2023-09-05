import tkinter
from tkinter import *
import time

def _widgets_by_name(parent, name, widgets):
    if not parent.winfo_children():
        if name == parent.winfo_name():
            widgets.append(parent)
    else:
        for child in parent.winfo_children():
            _widgets_by_name(child, name, widgets)


def find_widget_by_name(parent, name):
    ''' ui automation function that can find a widget in an application/hierarchy of widgets by its name '''
    widgets = []
    _widgets_by_name(parent, name, widgets)
    if len(widgets) == 0:
        raise Exception(f'no widget named {name} found')
    elif len(widgets) > 1:
        raise Exception(f'multiple widget named {name} found')
    return (widgets[0])


class Test():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("250x100")
        self.text = StringVar()
        self.text.set("Original Text")
        self.buttonA = Button(self.root, textvariable=self.text, name='button-a')
        self.buttonA.configure(text="test")

        self.buttonB = Button(self.root,
                              text="Click to change text",
                              command=self.changeText,
                              name='button-b'
                              )
        self.buttonA.pack(side=LEFT)
        self.buttonB.pack(side=RIGHT)
        # self.root.mainloop() do not start the main loop for testing purpose
        # can still be started outside of  __init__ for normal operation

    def changeText(self):
        self.text.set("Updated Text")


app = Test()

# test the app step by step
# find one of the buttons and invoke it
find_widget_by_name(app.root, 'button-b').invoke()

app.root.update()  # replace the app mainloop: run the UI refresh once.
time.sleep(10)
assert app.text.get() == "Updated Text"