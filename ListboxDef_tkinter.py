from tools import *
from tkinter import *
frm =form("600x600")

label(frm,"hello").pack(pady=7)
button(frm,"ok").pack(pady=7)
textbox(frm).pack(pady=5)
checkbox(frm).pack(pady=5)
combobox(frm,["ahmed","amr"],True).pack()
radio(frm).pack(pady=5)

Label(frm,text="name").pack()
Entry(frm).pack()
Button(frm,text="text").pack()
lbx=listbox(frm,("ahmed","amr","adel"))
lbx.pack(pady=5)
bgall(frm,"lightblue")
fontall(frm,"None 20")
fgall(frm,"navy")
frm.mainloop()
