from tkinter import *

main_window=Tk()   # careting mai  window


def clicked():
    label=Label(main_window,text='Sorry "H....."')
    label.pack()
label=Label(main_window,text='kamal sanjay',font=('Arial',20),padx=30,pady=50)
label.pack()    # label.pack(side=BOTTOM)----> for text alligns

#craeting text 

user_input=Entry(main_window,width=20,font=('Arial',18))
user_input.pack(pady=10)
# craetimg buttons
button=Button(main_window,text='click',padx=10,pady=5,font=('Arial',14),command=clicked)
button.pack()

main_window.mainloop()