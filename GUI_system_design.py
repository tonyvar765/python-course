from tkinter import *

window = Tk()
window.title("My Tkinter Window")
window.geometry("500x500")

def sugano():
    print("poda myre")

def vere():
    print('poda poori mone')

button1 = Button(window, text="sugano", width=15, height=2, fg="red", command=sugano)
button2 = Button(window, text='vere nthoke', width=15, height=2, command=vere)
label = Label(window, text="Welcome")

  # Using pack for the label
button1.grid(row=1,column=2)
button2.grid(row=2,column=1)

window.mainloop()
