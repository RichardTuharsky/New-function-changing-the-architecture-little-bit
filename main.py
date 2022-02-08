from cgitb import text
from tkinter import *
import backend
from tkinter.ttk import *


def add_command():
    backend.insert(uzivatel_text.get(), knihy_text.get())
    listb.insert(END, (uzivatel_text.get(), knihy_text.get()))


master = Tk("Kniznica")
master.wm_title("Kniznica")
master.geometry("400x400")


label = Label(master,text ="Dobry den, vytajte v nasej miestnej kniznici.")         
label.pack(pady = 10)

def openNewWindow():

	newWindow = Toplevel(master)
	newWindow.title("Knihy")
	newWindow.geometry("400x400")
	Label(newWindow,text ="Tu mozte najst informacie o knihach",width=20).pack() 
	Button(newWindow,text ="Spusti kniznicu",width=20).pack()
	Button(newWindow,text ="Vyhladaj novu knihu",width=20).pack()
	Button(newWindow,text ="Vymaz knihu",width=20).pack()
	Button(newWindow,text ="Zadaj novu knihu",width=20).pack()
	Button(newWindow,text ="Vrat knihu do kniznice",width=20).pack()	
	
btn = Button(master,text ="Informacie o knihach",command = openNewWindow)  
btn.pack(pady = 18)


def openNewWindow():
    
	newWindow = Toplevel(master)
	newWindow.title("Knihy")
	newWindow.geometry("400x400")
	Label(newWindow,text ="Tu mozte najst informacie o uzivatelovi",width=20).pack()
	Button(newWindow,text ="Vytvor noveho uzivatela",width=20).pack()
	Button(newWindow,text ="Vymaz uzivatela",width=20).pack()
	Button(newWindow,text ="Zoznam uzivatelov",width=20).pack()
	Button(newWindow,text ="Vyhladavanie uzivatela",width=20).pack()
	
btn = Button(master, text ="Informacie o uzivatelovi",command = openNewWindow)           
btn.pack(pady = 18)


mainloop()

window.mainloop()

