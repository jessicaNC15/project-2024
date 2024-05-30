from tkinter import *
import tkinter.font
 
root = Tk()
root.title("Converter")
root.geometry("400x400")
 
thefont = tkinter.font.Font(size=15)
 
newframe = LabelFrame(root,text="Converter Temperature",padx=10,pady=10)
newframe.place(x =15 , y = 10 )
 
judul = Label(newframe,text="Temperatur").grid(row = 0, columnspan=3)
samde = Label(newframe, text="=").grid(row = 1,column=1)
 
e1 = Entry(newframe,width=15)
e2 = Entry(newframe,width=15)
e1["font"] = thefont
e2["font"] = thefont
e2.insert(0, "0")
e1.grid(row=1,column=0)
e2.grid(row=1, column=2)
 
rmslbl = Label(newframe,text="Formula")
rmslbl.place(x = 1, y =90)
 
rmsnya = Label(newframe,text="(...°C x 9/5) + 32 = ... °F")
rmsnya.place(x = 50 , y = 90)
 
chek = {"rumus","yes"}
 
def rumus(rm):
    e2.delete(0,END)
    
    suhuawal = cliked.get()
    suhuakhir = cliked2.get()
    nomer1 = int(e1.get())
 
    global rmsnya
    if "rumus" in chek:
        rmsnya.place_forget()
    else:
        pass
    if suhuawal == "celcius" and suhuakhir == "fahrentheit":
        rmsnya = Label(newframe,text="("+e1.get()+"°C × 9/5) + 32 = ... °F")
        cara = (nomer1 * 9/5) + 32
    elif suhuawal == "celcius" and suhuakhir == "kelvin":
        rmsnya = Label(newframe,text=e1.get()+"°C + 273.15 = ... K")
        cara = (nomer1 + 273.15)
    elif suhuawal == "celcius" and suhuakhir == "reamur":
        rmsnya = Label(newframe,text="(4/5 × "+e1.get()+"°C) = ... R")
        cara = (4/5 * nomer1)
    elif suhuawal == "fahrentheit" and suhuakhir == "celcius":
        rmsnya = Label(newframe,text="("+e1.get()+"°F - 32) × 5/9 = ... °C")
        cara = (nomer1 - 32) * 5/9
    elif suhuawal == "fahrentheit" and suhuakhir == "kelvin":
        rmsnya = Label(newframe,text="("+e1.get()+"°F - 32) × 5/9 + 273.15 = ... K")
        cara = (nomer1 - 32) * 5/9 + 273.15
    elif suhuawal == "fahrentheit" and suhuakhir == "reamur":
        rmsnya = Label(newframe,text="("+e1.get()+"F - 32) × 4/9 = ... R")
        cara = (nomer1 - 32) * 4/9
    elif suhuawal == "reamur" and suhuakhir == "celcius":
        rmsnya = Label(newframe,text="5/4 × "+e1.get()+"R) = ... °C")
        cara = (5/4 * nomer1)
    elif suhuawal == "reamur" and suhuakhir == "fahrentheit":
        rmsnya = Label(newframe,text="(9/4 × "+e1.get()+"R) + 32 = ... F")
        cara = (9/4 * nomer1) + 32
    elif suhuawal == "reamur" and suhuakhir == "kelvin":
        rmsnya = Label(newframe,text="(5/4 ×"+e1.get()+"R) + 273 = ... K")
        cara = (5/4 * nomer1) + 273
    elif suhuawal == "kelvin" and suhuakhir == "celcius":
        rmsnya = Label(newframe,text=e1.get()+"K - 273.15 = ... °C")
        cara = (nomer1 - 273.15)
    elif suhuawal == "kelvin" and suhuakhir == "fahrentheit":
        rmsnya = Label(newframe,text="("+e1.get()+"K - 273.15) × 9/5 + 32 = ... °F ")
        cara = (nomer1 - 273.15) * 9/5 + 32 
    elif suhuawal == "kelvin" and suhuakhir == "reamur":
        rmsnya = Label(newframe,text="("+e1.get()+"k - 273) × 4/5 = ... R")
        cara = (nomer1 - 273) * 4/5
    elif suhuawal == "celcius" and suhuakhir == "celcius" or suhuawal == "fahrentheit" and suhuakhir == "fahrentheit" or  suhuawal == "reamur" and suhuakhir == "reamur" or suhuawal == "kelvin" and suhuakhir == "kelvin" :
        rmsnya = Label(newframe,text="tidak ada rumus")
        cara = nomer1
    hasil = cara
    e2.insert(0,hasil)
    rmsnya.place(x = 50 , y = 90)
    
option = ["celcius","fahrentheit","kelvin","reamur"]
cliked = StringVar()
cliked.set(option[0])
drop = OptionMenu(newframe,cliked,*option,command=rumus)
drop.config(width=20)
drop.grid(row = 2,column=0)
 
cliked2 = StringVar()
cliked2.set(option[1])
drop2 = OptionMenu(newframe,cliked2,*option,command=rumus)
drop2.config(width=20)
drop2.grid(row = 2,column=2)
 
btn = Button(newframe,text="count",command=lambda:rumus("hitung"))
btn.grid(row = 3,column=2)
 
root.mainloop()