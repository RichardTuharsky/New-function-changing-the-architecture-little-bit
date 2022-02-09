from cgitb import text
from tkinter import *
from tkinter import font
import backend
from tkinter.ttk import *


def add_command():
    backend.insert(uzivatel_text.get(), knihy_text.get())
    listb.insert(END, (uzivatel_text.get(), knihy_text.get()))


master = Tk("Kniznica")
master.wm_title("Kniznica")
master.geometry("400x180")


label = Label(master,text ="Dobry den, vytajte v nasej miestnej kniznici.")         
label.pack(pady = 10)

def openNewWindow():

	newWindow = Toplevel(master)
	newWindow.title("Knihy")
	newWindow.geometry("500x400")
	l1 = Label(newWindow, text = "Vymaz knihu")
	l1.grid(row=0, column=3)
	vymaz_knihu = StringVar()
	ent1 = Entry(newWindow, textvariable = vymaz_knihu)
	ent1.grid(row = 0, column = 4)
	vymaz_knihu = StringVar()
	ent1 = Entry(newWindow, textvariable = vymaz_knihu)
	ent1.grid(row = 0, column = 10)
	vymaz_knihu = StringVar()
	ent1 = Entry(newWindow, textvariable = vymaz_knihu)
	ent1.grid(row = 0, column = 15)
	l1 = Label(newWindow, text = "Zadaj novu knihu")
	l1.grid(row=5, column=3)
	zadaj_novu_knihu = StringVar()
	ent1 = Entry(newWindow, textvariable = zadaj_novu_knihu)
	ent1.grid(row = 5, column = 4)
	zadaj_novu_knihu = StringVar()
	ent1 = Entry(newWindow, textvariable = zadaj_novu_knihu)
	ent1.grid(row = 5, column = 10)
	zadaj_novu_knihu = StringVar()
	ent1 = Entry(newWindow, textvariable = zadaj_novu_knihu)
	ent1.grid(row = 5, column = 15)
	l1 = Label(newWindow, text = "Vyhladaj knihu")
	l1.grid(row=10, column=3)
	vyhladaj_knihu = StringVar()
	ent1 = Entry(newWindow, textvariable = vyhladaj_knihu)
	ent1.grid(row = 10, column = 4)
	vyhladaj_knihu = StringVar()
	ent1 = Entry(newWindow, textvariable = vyhladaj_knihu)
	ent1.grid(row = 10, column = 10)
	vyhladaj_knihu = StringVar()
	ent1 = Entry(newWindow, textvariable = vyhladaj_knihu)
	ent1.grid(row = 10, column = 15)
	


btn = Button(master,text ="Informacie o knihach",command = openNewWindow)  
btn.pack(pady = 18)
	


def openNewWindow():
    
	newWindow = Toplevel(master)
	newWindow.title("Uzivatel")
	newWindow.geometry("400x400")
	Label(newWindow,text ="Tu mozte najst informacie o uzivatelovi",width=35).pack()
	Button(newWindow,text ="Vytvor noveho uzivatela",width=21).pack()
	Button(newWindow,text ="Vymaz uzivatela",width=20).pack()
	Button(newWindow,text ="Zoznam uzivatelov",width=20).pack()
	Button(newWindow,text ="Vyhladavanie uzivatela",width=20).pack()
	
btn = Button(master, text ="Informacie o uzivatelovi",command = openNewWindow)           
btn.pack(pady = 18)


mainloop()



	