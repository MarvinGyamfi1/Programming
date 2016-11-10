from tkinter import *
import csv
top = Tk()



def programma():
    reg = Toplevel()
    reg.title("Registreer")


    gebruikersnaam = Label(reg, text="gebruikersnaam:")
    gebruikersnaaminput = Entry(reg, width = 26)
    gebruikersnaam.grid(row=0, column =1)
    gebruikersnaaminput.grid(row=0, column=2, columnspan = 4, pady = 10, padx = 20)

    wachtwoord_1 = Label(reg, text='wachtoord:')
    wachtwoordinput_1 = Entry(reg,show = '*', width = 26)
    wachtwoord_1.grid(row=1, column=1)
    wachtwoordinput_1.grid(row=1, column=2, columnspan = 4, pady = 10, padx = 20)

    wachtwoord_2 = Label(reg, text='herhaal wachtoord:')
    wachtwoordinput_2 = Entry(reg,show = '*', width = 26)
    wachtwoord_2.grid(row=2, column=1)
    wachtwoordinput_2.grid(row=2, column=2, columnspan = 4, pady = 10, padx = 20)


    email = Label(reg, text="email:")
    emailinput = Entry(reg, width = 26)
    email.grid(row=3, column=1)
    emailinput.grid(row=3, column=2, columnspan = 4, pady = 15, padx = 20)

    datumjaar = Label(reg, text="Geboortedatum:")
    datumjaarinput = Spinbox(reg,width = 6, value = (1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016))
    datumjaar.grid(row=4, column=1, pady = 10, padx= 20)
    datumjaarinput.grid(row=4, column=2, sticky=E)

    datummaandinput = Spinbox(reg,width = 10,value = ('Januari','Februari','Maart','April','Mei','Juni','Juli','Augustus','September','Oktober','November','December' ))
    datummaandinput.grid(row=4, column=3)
    datumdaginput = Spinbox(reg,width = 3,value=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32))
    datumdaginput.grid(row=4, column = 4, sticky = W)



    def schrijf():
        wachtwoord_1 = wachtwoordinput_1.get()
        wachtwoord_2 = wachtwoordinput_2.get()
        if wachtwoord_1 != wachtwoord_2:

            wwfout = Label(reg, text = "wachtwoorden ongelijk!")
            wwfout.grid(row = 5, column = 1)

        else:



            gebruikersnaam = gebruikersnaaminput.get()
            print(gebruikersnaam)
            wachtwoord_1 = wachtwoordinput_1.get()
            print (wachtwoord_1)
            email = emailinput.get()
            print (email)
            datumjaar = datumjaarinput.get()
            print (datumjaar)
            datummaand = datummaandinput.get()
            print (datummaand)
            datumdag = datumdaginput.get()
            print (datumdag)
            with open('reg.csv', 'a',newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')

                writer.writerow((gebruikersnaam,wachtwoord_1,email,'{}-{}-{}'.format(datumdag,datummaand,datumjaar)))






    regknop = Button(reg, text='Registreer', command = schrijf, width = 10)
    regknop.grid(column = 3)


    top.mainloop()



programma()

