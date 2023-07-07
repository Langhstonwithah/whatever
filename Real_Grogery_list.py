from tkinter import *
import tkinter as tk

root = Tk()

# make a class/oblect
class Doodad:
    def __init__(self, name, quan, price):
        self.name = name
        self.quan = quan
        self.price = price



#create listbox aspect right here
my_listbox = Listbox(root)

#listbox.grid(options)
my_listbox.grid(row=4, column=0)

#Textbox and text label
mytextbox = tk.Text(root,
                    height=1,
                    width = 20)
mytextlabel = tk.Label(root, text = "Item")
mytextlabel.grid(row=0, column=0)
mytextbox.grid(row=1, column=0)

#Function for adding stuff
def mylist(): 
    inp = mytextbox.get(1.0,"end-1c")
    name = inp[0:inp.index(",")]
    inp = inp[inp.index(",")+1:]
    quan = inp[0:inp.index(",")]
    price = inp[inp.index(",")+1:]
    cole = True
    for i in range(len(mylist1)):
        if mylist1[i].name == name:
            cole = False
            mylist1[i].quan = int(mylist1[i].quan) + int(quan)
                
    if cole:        
        mylist1.append(Doodad(name, quan, price))
    my_listbox.delete(0,END)
    for i in range(len(mylist1)):
        #add chicken to listbox using listbox.insert function
        my_listbox.insert(END, str(mylist1[i].name) + " , " + str(mylist1[i].quan) + " , " + str(mylist1[i].price) + "\n")
        
        
    tprice = 0
    for i in range(len(mylist1)):
        tprice = tprice + float(mylist1[i].price) * float(mylist1[i].quan)
    mytextlabel.configure(text="Your Total Price Is: " + str(tprice))
        #guilist.insert(END, chicken)

    
#Function for removing things
def removeMyList():
    inp = mytextbox.get(1.0,"end-1c")
    name = inp[0:inp.index(",")]
    inp = inp[inp.index(",")+1:]
    quan = inp[0:inp.index(",")]
    price = inp[inp.index(",")+1:]
    for i in range(len(mylist1)):
        if mylist1[i].name == name:
            if int(mylist1[i].quan) > int(quan):
                mylist1[i].quan = int(mylist1[i].quan) - int(quan)
            else:
                mylist1.remove(mylist1[i])
    my_listbox.delete(0,END)
    for i in range(len(mylist1)):
        my_listbox.insert(END, str(mylist1[i].name) + " , " + str(mylist1[i].quan) + " , " + str(mylist1[i].price) + "\n")
        
#Total price
    tprice = 0
    for i in range(len(mylist1)):
        tprice = tprice + float(mylist1[i].price) * float(mylist1[i].quan)
    mytextlabel.configure(text="Your Total Price Is: " + str(tprice))
        #guilist.insert(END, chicken)
        #guilist.insert(END, chicken)
    
#making a button, and adding text to that button
my_button= Button(root, text = "Add Something", command= mylist)
#putting the button on the screen
my_button.grid(row=2, column=0)

#making a button, and adding text to that button
my_button2= Button(root, text = "Remove Something", command= removeMyList)
#putting the button on the screen
my_button2.grid(row=3, column=0)

mylist1 = []
mylist1.append(Doodad("Juice", 2, 3.50))
mylist1.append(Doodad("lca", 2, 4.99))
for i in range(len(mylist1)):
    #add chicken to listbox using listbox.insert function
    my_listbox.insert(END, str(mylist1[i].name) + " , " + str(mylist1[i].quan) + " , " + str(mylist1[i].price) + "\n")
    #guilist.insert(END, chicken)
    
    
    
root.mainloop()

