#GUI = Graphical User Interface
#Libraries
##############
#1.Tkinter
#2.PyQT
#3.Turtle

import tkinter as ttk
app = ttk.Tk()
app.title('my app')
app.geometry('600x400')

ttk.Label(app, text = 'A simple Text Label').place(x=50,y=50)
ttk.Label(app, text = 'Anushka Goyal').place(x=60,y=60)


app.mainloop()
