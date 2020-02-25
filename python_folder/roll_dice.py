'''
Rolling dice with gui interface using tkinter
written by Rhornberger
last updated nov 12 2019
'''
# import library 
from tkinter import *

# create the window size and welcome text
window = Tk()
window.title('Welcome to the D20 roller!')
lbl = Label(window, text = 'Welcome!', font =('arial', 20))
lbl.grid(column = 0, row = 0)
window.geometry('300x200')

# creat a function for the button to do something
def clicked():
    lbl.configure(text = 'Button was clicked!!')
btn = Button(window, text = 'Click to Roll', command = clicked, bg = 'black', fg = 'red')
btn.grid(column = 1, row = 0)

# create check buttons for type of die to use
rad1 = Radiobutton(window, text = 'D20', value = 1)
rad2 = Radiobutton(window, text = 'D12', value = 2)
rad3 = Radiobutton(window, text = 'D10', value = 3)
rad4 = Radiobutton(window, text = 'D8', value = 4)
rad5 = Radiobutton(window, text = 'D6', value = 5)
rad6 = Radiobutton(window, text = 'D4', value = 6)
rad7 = Radiobutton(window, text = 'D%', value = 7)
rad1.grid(column = 0, row = 1)
rad2.grid(column = 1, row = 1)
rad3.grid(column = 2, row = 1)
rad4.grid(column = 3, row = 1)
rad5.grid(column = 4, row = 1)
rad6.grid(column = 5, row = 1)
rad7.grid(column = 6, row = 1)
window.mainloop()