from tkinter import *
import time
def click(event):
    global scvalue
    #event.widget gives the button that is clicked and cget gives the text in the button
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            #eval calculates a string e.g "2+3" = 5
            value = eval(screen.get())
        scvalue.set(value)

        screen.update()        
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text) 
        screen.update()       
root =Tk()
root.title("Calculator by gouransh")
root.geometry("500x600")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 20 bold")
screen.pack(fill = X,ipadx=8,pady=10,padx=10)
root.wm_iconbitmap("E:/games photos/bird.png")

f1 =Frame(root,bg ="cyan")
b1 = Button(f1,text="9",padx = 28,pady=7,font="Arial 15 bold",bg="green",fg="orange")
b1.pack(side=LEFT,padx=18,pady=12)
b1.bind("<Button-1>",click)

b2 = Button(f1,text="8",padx = 28,pady=7,font="Arial 15 bold",bg="green",fg="orange")
b2.pack(side=LEFT,padx=18,pady=12)
b2.bind("<Button-1>",click)

b3 = Button(f1,text="7",padx = 28,pady=7,font="Arial 15 bold",bg="green",fg="orange")
b3.pack(side=LEFT,padx=18,pady=12)
b3.bind("<Button-1>",click)
f1.pack()

#jo padding button banate sme hoti he vo padding button ke andar text se button ki boun dary tak hoti hai
#jo padding button packing ke andar hoti he vo button ke bhar ki padding hoti hai e.g.pady
f1 =Frame(root,bg ="cyan")
b1 = Button(f1,text="6",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b1.pack(side=LEFT,padx=18,pady=20)
b1.bind("<Button-1>",click)
b2 = Button(f1,text="5",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b2.pack(side=LEFT,padx=18,pady=12)
b2.bind("<Button-1>",click)
b3 = Button(f1,text="4",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b3.pack(side=LEFT,padx=18,pady=12)
b3.bind("<Button-1>",click)
f1.pack()

f1 =Frame(root,bg ="cyan")
b1 = Button(f1,text="3",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b1.pack(side=LEFT,padx=18,pady=12)
b1.bind("<Button-1>",click)
b2 = Button(f1,text="2",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b2.pack(side=LEFT,padx=18,pady=12)
b2.bind("<Button-1>",click)
b3 = Button(f1,text="1",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b3.pack(side=LEFT,padx=18,pady=12)
b3.bind("<Button-1>",click)
f1.pack()

f1 =Frame(root,bg ="cyan")
b1 = Button(f1,text="0",padx = 29,pady=7,font="Arial 15 bold",bg="green",fg="orange")
b1.pack(side=LEFT,padx=18,pady=12)
b1.bind("<Button-1>",click)
b2 = Button(f1,text="+",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b2.pack(side=LEFT,padx=18,pady=12)
b2.bind("<Button-1>",click)
b3 = Button(f1,text="-",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b3.pack(side=LEFT,padx=18,pady=12)
b3.bind("<Button-1>",click)
f1.pack()

f1 =Frame(root,bg ="cyan")
b1 = Button(f1,text="*",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b1.pack(side=LEFT,padx=18,pady=12)
b1.bind("<Button-1>",click)
b2 = Button(f1,text="/",padx = 30,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b2.pack(side=LEFT,padx=20,pady=12)
b2.bind("<Button-1>",click)
b3 = Button(f1,text="%",padx = 25,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b3.pack(side=LEFT,padx=18,pady=12)
b3.bind("<Button-1>",click)
f1.pack()

f1 =Frame(root,bg ="cyan")
b1 = Button(f1,text="=",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b1.pack(side=LEFT,padx=18,pady=12)
b1.bind("<Button-1>",click)
b2 = Button(f1,text="C",padx = 28,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b2.pack(side=LEFT,padx=18,pady=20)
b2.bind("<Button-1>",click)
b3 = Button(f1,text=".",padx = 29,pady=5,font="Arial 15 bold",bg="green",fg="orange")
b3.pack(side=LEFT,padx=18,pady=1)
b3.bind("<Button-1>",click)
f1.pack()

timeframe = Frame(root,bg="grey")
Label(timeframe,text=time.ctime(),padx=3,bg="orange",font="lucida 20 italic").pack()
timeframe.pack(side=BOTTOM,fill=X)
root.mainloop()