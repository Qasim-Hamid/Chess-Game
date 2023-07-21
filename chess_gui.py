from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Chess")

mainframe = ttk.Frame(root, padding = "20 20 20 20")
mainframe.grid(column = 0, row = 0)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 3)


img = PhotoImage(file = "Blank Pawn.png")
style = ttk.Style()
style.theme_use('alt')

style.configure("B.TButton", background="#6b8737", width=10)
style.map('B.TButton', background=[('active', '#6b8737')])

style.configure("W.TButton", background="#ebe2d3", width=10)
style.map('W.TButton', background=[('active', '#ebe2d3')])

for row_index in range(8):
    for clmn_index in range (8):
        if ((row_index % 2 == 0) & (clmn_index % 2 == 0)) or ((row_index % 2 == 1) & (clmn_index % 2 == 1)):
            B_Botton = ttk.Button(mainframe, style='W.TButton')
            B_Botton.grid(column = clmn_index, row = row_index)


for row_index in range(8):
    for clmn_index in range(8):
        if ((row_index % 2 == 0) & (clmn_index % 2 == 1)) or ((row_index % 2 == 1) & (clmn_index % 2 == 0)):
            W_Button = ttk.Button(mainframe, style='B.TButton')
            W_Button.grid(column = clmn_index, row = row_index)


root.mainloop()