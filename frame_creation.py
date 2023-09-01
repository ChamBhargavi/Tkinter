import tkinter


window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.Label(frame, text="User Information")
user_info_frame.grid(row=0, column=0)

window.mainloop()