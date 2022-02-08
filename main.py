from cgitb import text
from tkinter import *
import backend

def add_command():
    backend.insert(uzivatel_text.get(), knihy_text.get())
    listb.insert(END, (uzivatel_text.get(), knihy_text.get()))


'''
#uzivatel, knihy
l1 = Label(window, text = "Uzivatel")
l1.grid(row=0, column=0)
l1 = Label(window, text = "Knihy")
l1.grid(row=0, column=2)


#policka pre uyivatela a knihy na pisanie
uzivatel_text = StringVar()
ent1 = Entry(window, textvariable = uzivatel_text)
ent1.grid(row = 0, column = 1)

knihy_text = StringVar()
ent2 = Entry(window, textvariable = knihy_text)
ent2.grid(row = 0, column = 4)

# box pod polickami
listb = Listbox(window, height=6, width=35)
listb.grid(row=2, column=0, rowspan=6, columnspan=2)


listb.configure(yscrollcommand=sb.set)
sb.configure(command=listb.yview)
'''
'''
#tlacitka
b1 = Button(window, text = "Informacie o uzivatelovi", width=40)
b1.grid(row=6, column=10)
b2 = Button(window, text = "Informacie o knihach", width=40)
b2.grid(row=8, column=10)
'''

from tkinter.ttk import *

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

