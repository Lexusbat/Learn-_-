from tkinter import *
window = Tk()

window.title("Hello World")
window.geometry("400x300")
label = Label(window, text="LA PROJCT")
label.configurefont=("Garamond", 80, "bold")

label.pack()
window.mainloop()