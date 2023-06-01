from tkinter import *
from PIL import Image,ImageTk

def check1():
    if (x.get()):
        print("check")
    else:
        pass

def check2():
    if (y.get()):
        print("check")
    else:
        pass

def check3():
    if (y.get()):
        print("Nowhere in sight!")
    else:
        pass

window = Tk()
window.title("Raze Checkbuttons")
icon = PhotoImage(file="razechar.png")
icon2 = PhotoImage(file="raze.png")
window.iconphoto(True,icon)

logo = ImageTk.PhotoImage(Image.open("raze.png"))
label = Label(window,image=logo)
label.pack(side = LEFT)

x = BooleanVar()
y = BooleanVar()
z = BooleanVar()

checkbutton1 = Checkbutton(window,
                           text = "Paint?",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=check1,
                           font=("Arial",20,"bold"))
checkbutton1.pack()

checkbutton2 = Checkbutton(window,
                           text = "Charges?",
                           variable=y,
                           onvalue=True,
                           offvalue=False,
                           command=check2,
                           font=("Arial",20,"bold"))
checkbutton2.pack()

checkbutton3 = Checkbutton(window,
                           text = "Brakes?",
                           variable=z,
                           onvalue=True,
                           offvalue=False,
                           command=check3,
                           font=("Arial", 20, "bold")
                           )
checkbutton3.pack()


window.mainloop()