# Juan Valdez
# Pizza Order Application create a visual application for ordering a pizza

#import tkinter
from tkinter import *
 
#click function will act as main
def click():
    print()

    #initialize variables

    toppings = "Cheese"
    enteredSize = "Medium"
    total = 0

    #queries for: to price, pizza size, crust, toppings, and extra cost--------------------------------


    #Text Entry will check what size the pizza ordered will be
    if textEntry.get() == "Small":
        enteredSize = "Small"
        total += 10.99
    if textEntry.get() == "Medium":
        enteredSize = "Medium"
        total += 12.99
    if textEntry.get() == "Large":
        enteredSize = "Large"
        total += 14.99
    #If statements to get style of pizza
    if crust_var.get() == 1: #gets the crust selection from selected 
        pizzaType = "Hand-Tossed"
    elif crust_var.get() == 2:
        pizzaType = "Deep-dish"
    elif crust_var.get() == 3:
        pizzaType = "Thin-crust"

    toppings = []
    toppings.append("Cheese") #default value
    if topping_var.get() == True:
        toppings.append("Pepporoni")
        total += 1.25
    if topping_var2.get() == True:
        toppings.append("Sauasage")
        total += 1.25
    if topping_var3.get() == True:
        toppings.append("Mushrooms")
        total += 1.25
    if topping_var4.get() == True:
        toppings.append("Onions")
        total += 1.25



    #calculate tax and total with formatting
    tax = 8.75 / 100
    totaltax = 0
    totaltax *= tax
    total += totaltax
    #clear text box and print pizza receipt

    output.delete(0.0,END) #clears the window

    output.insert(END,"Your order is: \n" + enteredSize + " pizza\n")
    output.insert(END,"Your pizza is of style: " + pizzaType + "\n")
    output.insert(END,"Your toppings are: ")
    output.insert(END, toppings)
    output.insert(END,"\n")
    output.insert(END,total)


#open window with title,size and background----------------------------------------------------------
window = Tk()
window.title("Juan's Pizzeria")
window.geometry('1050x800')
window.configure(background = 'white')

#options of how to place objects on the window -> .pack() or .grid(row = 0,column = 0,sticky = w) or .place(x=110,y=0)

#create photo object and photo label
photo = PhotoImage(file = "pizzaImage.gif")
image_label = Label(window,image = photo)
image_label.grid(row = 600, column=0,sticky = E+W, padx=5,pady=5)
#image_label.pack()

name_label = Label(window,text="Enter Your Pizza Size:\n Small, Medium, Large", bg = 'white', fg = "black", font = "arial 12 bold")
#name_label.pack()
name_label.grid(row = 800, column=0, sticky=W,padx = 5,pady = 5)

#text label to guide user to enter pizza size

#create text entry for size entry----------------------------------------------------------
textEntry = Entry(window, width=30, bg="white",fg="black")
textEntry.grid(row = 1500, column = 0, sticky = W, padx = 5,pady = 5)
#textEntry.pack()

#create radio buttons to choose crust type----------------------------------------------------------
crust_label = Label(window,text="Crust Type:", bg = 'white', fg = 'black', font = "arial 12 bold")
crust_label.grid(row = 1600,column = 0, sticky = W, padx = 10, pady = 10)
#crust_label.pack()
crust_var = IntVar()
radio1 = Radiobutton(window, text = "Hand-tossed", variable=crust_var,value =1, bg = "white",fg = "black")
radio1.grid(row = 1700, column = 0, sticky = W, padx = 5,pady = 5)

radio2 = Radiobutton(window, text = "Deep-dish", variable=crust_var,value = 2, bg = "white", fg = "black")
radio2.grid(row = 1800, column = 0, sticky = W, padx = 5,pady = 5)

radio3 = Radiobutton(window, text = "Thin-crust", variable=crust_var,value = 3, bg = "white", fg = "black")
radio3.grid(row = 1900, column = 0, sticky = W, padx = 5,pady = 5)

#radio1.pack()
#radio2.pack()
#radio3.pack()


#create check boxes for topp
# crust_label = Label(window,text="Crust Type:", bg = 'white', fg = 'black', font = "arial 12 bold")
topping_var = IntVar()
toppings_label = Label(window,text="Toppings:", bg = 'white', fg = 'black', font = "arial 12 bold")
toppings_label.grid(row = 2000,column = 0, sticky = W, padx = 10, pady = 10)
c = Checkbutton(window, text = "Pepporoni", variable= topping_var,bg = "white", fg = "black")
c.grid(row = 2100, column = 0, sticky = W, padx = 5,pady = 5)
#c.pack(side=LEFT)

topping_var2 = IntVar()
c2 = Checkbutton(window, text = "Sausage", variable = topping_var2,bg = "white", fg = "black")
c2.grid(row = 2200, column = 0, sticky = W, padx = 5,pady = 5)

#c2.pack(side=LEFT)

topping_var3 = IntVar()
c3 = Checkbutton(window, text = "Mushrooms", variable = topping_var3,bg = "white", fg = "black")
c3.grid(row = 2300, column = 0, sticky = W, padx = 5,pady = 5)

#c3.pack(side=LEFT)

topping_var4 = IntVar()
c4 = Checkbutton(window, text = "Onions", variable = topping_var4,bg = "white", fg = "black")
c4.grid(row = 2400, column = 0, sticky = W, padx = 5,pady = 5)

#c4.pack(side=LEFT)



#create button for order submission---------------------------------------------------------------
myButton = Button(window,text = "Click to Submit your order", width = 25,command = click) 
myButton.grid(row = 2500, column = 0, sticky = W, padx = 5,pady = 5)
#myButton.pack()

#create output for text box----------------------------------------------------------------------
output = Text(window,width = 75, height = 6,wrap=WORD,background = "white",foreground="black")
output.grid(row = 2400, column = 100, sticky = E, padx = 5,pady = 5)
#output.pack()

#maintains window
window.mainloop() 