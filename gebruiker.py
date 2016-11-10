from tkinter import *
from tkinter import ttk


root = Tk()
root.configure()
gebruiker_frame = Frame(root, bg='WHITE')





uitlog_knop = Button(gebruiker_frame, text='Uitloggen',bg='WHITE')
uitlog_knop.pack(anchor=NE)


tree = ttk.Treeview(gebruiker_frame,padding = 10)
tree["columns"]=("one","two","three","four",'five','six')

tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)
tree.column("four", width=100)
tree.column('five', width=100)
tree.column('six', width=100)

tree.heading("one", text="Jaaruitgaven")
tree.heading("two", text="Uitgevers")
tree.heading("three", text="Leeftijd minimaal")
tree.heading("four", text="Genres")
tree.heading('five', text='Rating')
tree.heading('six', text='Lengte')

for x in range (0,51):
    tree.insert("",0,text="Filmnaam: " + str(x) , values=(x*x,'Netflix'))


gebruiker_frame.pack(anchor = CENTER)
tree.pack()
root.mainloop()



