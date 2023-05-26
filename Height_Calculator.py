from tkinter import *
import decimal


def clear():
    global feet
    global inches
    global centimeters
    global ms
    feet.destroy()
    inches.destroy()
    centimeters.destroy()
    ms.destroy()
    feet = Entry(window)
    feet.place(x=90, y=20)
    feet.config(width=20)
    inches = Entry(window)
    inches.place(x=300, y=20)
    inches.config(width=15)
    centimeters = Entry(window)
    centimeters.place(x=150, y=220)
    message = Entry(window)
    message.place(x=110, y=270)
    message.config(width=35)


def msclear():
    global ms
    ms.destroy()
    ms = Entry(window)
    ms.place(x=110, y=270)
    ms.config(width=35)


def convert():
    global feet
    global inches
    global centimeters
    global ms
    cm = centimeters.get()
    ft = feet.get()
    inch = inches.get()
    if (ft == "" and inch == "" and cm == "") or (ft == "" and cm == "") or (inch == "" and cm == ""):
        msclear()
        ms.insert(0, "Conversion Failed: Not Enough Inputs")

    elif ft == "" and inch == "":
        cm = float(cm)
        total_inch = cm/2.54
        converted_ft = total_inch // 12
        converted_in = decimal.Decimal(total_inch % 12)
        rounded_in = converted_in.quantize(decimal.Decimal("0.001"))
        feet.insert(0, converted_ft)
        inches.insert(0, rounded_in)
        msclear()
        ms.insert(0, "Conversion Completed")
    elif cm == '':
        ft = float(ft)
        inch = float(inch)
        more_inches = ft*12
        total_inches = more_inches + inch
        converted_cm = total_inches*2.54
        centimeters.insert(0, converted_cm)
        msclear()
        ms.insert(0, "Conversion Complete")
    else:
        msclear()
        ms.insert(0, "Conversion Failed: Too Many Inputs")


window = Tk()
window.title("Height Calculator")
window = Canvas(window, width=400, height=300)
window.pack()
feet = Entry(window)
feet.place(x=90, y=20)
feet.config(width=20)
ftlbl = Label(window, text="Feet: ", font=("Ariel", 15))
ftlbl.place(x=30, y=13)
inches = Entry(window)
inches.place(x=300, y=20)
inches.config(width=15)
inlbl = Label(window, text="Inches: ", font=("Ariel", 15))
inlbl.place(x=220, y=13)
centimeters = Entry(window)
centimeters.place(x=150, y=220)
cmlbl = Label(window, text="Centimeters: ", font=("Ariel", 15))
cmlbl.place(x=27, y=213)
convertbttn = Button(window, text="Convert", command=convert, bg="black", fg="White")
convertbttn.place(x=170, y=100)
ms = Entry(window)
ms.place(x=110, y=270)
ms.config(width=35)
clearbttn = Button(window, text="Clear", command=clear, bg="black", fg="#ffffff")
clearbttn.place(x=177, y=140)
window.mainloop()
