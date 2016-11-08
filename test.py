from tkinter import *
import csv
top = Tk()



def programma():
    reg = Toplevel()
    reg.title("Registreer")

    gebruikersnaam = Label(top, text="gebruikersnaam:")
    gebruikersnaaminput = Entry(top)
    gebruikersnaam.grid(row=0, column =1)
    gebruikersnaaminput.grid(row=0, column=2)

    wachtwoord = Label(top, text='wachtoord:')
    wachtwoordinput = Entry(top,show = '*')
    wachtwoord.grid(row=1, column=1)
    wachtwoordinput.grid(row=1, column=2)

    wachtwoord = Label(top, text='herhaal wachtoord:')
    wachtwoordinput = Entry(top,show = '*')
    wachtwoord.grid(row=2, column=1)
    wachtwoordinput.grid(row=2, column=2)

    email = Label(top, text="email:")
    emailinput = Entry(top)
    email.grid(row=3, column=1)
    emailinput.grid(row=3, column=2)

    datumjaar = Label(top, text="GeboorteDatum: Jaar|Maand|Dag")
    datumjaarinput = Spinbox(top,width = 5, value = (1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016))
    datumjaar.grid(row=4, column=1)
    datumjaarinput.grid(row=4, column=2)

    datummaandinput = Spinbox(top,width = 10,value = ('Januari','Februari','Maart','April','Mei','Juni','Juli','Augustus','September','Oktober','November','December' ))
    datummaandinput.grid(row=4, column=3)
    datumdaginput = Spinbox(top,width = 3,value=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32))
    datumdaginput.grid(row=4, column = 4)

    with open('test.csv', 'w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow('k')
        csvfile.close()












programma()




top.mainloop()
