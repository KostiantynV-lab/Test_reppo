from tkinter import *
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
 
header = Label(text="Choose your destiny", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)
 
lang = IntVar()
level = IntVar()
 
python_checkbutton = Radiobutton(text="Python 3", value=1, variable=lang, padx=15, pady=10)
python_checkbutton.grid(row=1, column=0, sticky=W)
 
javascript_checkbutton = Radiobutton(text="JavaScript", value=2, variable=lang, padx=15, pady=10)
javascript_checkbutton.grid(row=2, column=0, sticky=W)

SQL_checkbutton = Radiobutton(text="SQL", value=3, variable=lang, padx=15, pady=10)
SQL_checkbutton.grid(row=3, column=0, sticky=W)
 
selection = Label(textvariable=lang, padx=15, pady=10)
selection.grid(row=4, column=0, sticky=W)
 
junior_checkbutton = Radiobutton(text="Junior", value=1, variable=level, padx=15, pady=10)
junior_checkbutton.grid(row=1, column=1, sticky=W)
 
middle_checkbutton = Radiobutton(text="Middle", value=2, variable=level, padx=15, pady=10)
middle_checkbutton.grid(row=2, column=1, sticky=W)

senior_checkbutton = Radiobutton(text="Senior", value=3, variable=level, padx=15, pady=10)
senior_checkbutton.grid(row=3, column=1, sticky=W)
 
selection = Label(textvariable=level, padx=15, pady=10)
selection.grid(row=4, column=1, sticky=W)
 
root.mainloop()