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
	newWindow.geometry("650x400")
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
	ent1.grid(row = 0, column = 13)
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
	ent1.grid(row = 5, column = 13)
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
	ent1.grid(row = 10, column = 13)
	l1 = Label(newWindow, text = "Zoznam knih")
	l1.grid(row=25, column=3)
	zoznam_uloh = StringVar()
	ent1 = Entry(newWindow, textvariable = zoznam_uloh)
	ent1.grid(row = 25, column = 4)
	sb = Scrollbar(newWindow)
	sb.grid(row=24, column=9, rowspan=6, columnspan=4)
	listb = Listbox(newWindow, height=6, width=35)
	listb.grid(row=23, column=10, rowspan=6, columnspan=2)
	


btn = Button(master,text ="Informacie o knihach",command = openNewWindow)  
btn.pack(pady = 18)
	


def openNewWindow():
    
	newWindow = Toplevel(master)
	newWindow.title("Uzivatel")
	newWindow.geometry("650x400")
	l1 = Label(newWindow, text = "Vymaz uzivatela")
	l1.grid(row=0, column=3)
	vymaz_uzivatela = StringVar()
	ent1 = Entry(newWindow, textvariable = vymaz_uzivatela)
	ent1.grid(row = 0, column = 4)
	vymaz_uzivatela = StringVar()
	ent1 = Entry(newWindow, textvariable = vymaz_uzivatela)
	ent1.grid(row = 0, column = 10)
	l1 = Label(newWindow, text = "Vytvor noveho uzivatela")
	l1.grid(row=5, column=3)
	vytvor_noveho_uzivatela = StringVar()
	ent1 = Entry(newWindow, textvariable = vytvor_noveho_uzivatela)
	ent1.grid(row = 5, column = 4)
	vytvor_noveho_uzivatela = StringVar()
	ent1 = Entry(newWindow, textvariable = vytvor_noveho_uzivatela)
	ent1.grid(row = 5, column = 10)
	l1 = Label(newWindow, text = "Vyhladaj uzivatela")
	l1.grid(row=10, column=3)
	vyhladaj_uzivatela = StringVar()
	ent1 = Entry(newWindow, textvariable = vyhladaj_uzivatela)
	ent1.grid(row = 10, column = 4)
	vyhladaj_uzivatela = StringVar()
	ent1 = Entry(newWindow, textvariable = vyhladaj_uzivatela)
	ent1.grid(row = 10, column = 10)
	l1 = Label(newWindow, text = "Zoznam uzivatelov")
	l1.grid(row=25, column=3)
	sb = Scrollbar(newWindow)
	sb.grid(row=24, column=8, rowspan=6, columnspan=2)
	listb = Listbox(newWindow, height=6, width=35)
	listb.grid(row=23, column=4, rowspan=6, columnspan=2)
	
	
	
btn = Button(master, text ="Informacie o uzivatelovi",command = openNewWindow)           
btn.pack(pady = 18)


mainloop()


	