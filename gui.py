#simple GUI

from tkinter import *

#create the window
matrix = Tk()

#modify the root windotw

matrix.title("Labeler")
matrix.geometry("200x50")

app = Frame(matrix)
app.grid()
button1 = Button(app, text = "This is a button")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "This will show text")

button3 = Button(app)
button3.grid()

button3["text"] = "This will show up as well."

root.mainloop()