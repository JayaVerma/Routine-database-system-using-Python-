from tkinter import *
import backend1

def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

def delete_command():
    backend1.delete(selected_row[0])

def view_command():
    list.delete(0,END)
    for row in backend1.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in backend1.search(date_text.get(), gaming_text.get(), exercise_text.get(), study_text.get(), yoga_text.get(), coding_text.get()):
        list.insert(END,row)

def add_command():
    backend1.insert(date_text.get(), gaming_text.get(), exercise_text.get(), study_text.get(), yoga_text.get(), coding_text.get())

    list.delete(0,END)
    list.insert(END,(date_text.get(),gaming_text.get(),exercise_text.get(),study_text.get(),yoga_text.get(),coding_text.get()))

win = Tk()

win.wm_title('MY ROUTINE DATABASE')
font_format=("Helvetica",10,"bold italic")

mainlabel = Label(win, text="MY Routine DATABASE", font=("Helvetica",15,"bold"))
mainlabel.grid(row=0,column=1,columnspan=2)

l1 = Label(win, text='Date',font=font_format)
l1.grid(row=1,column=0)
l2 = Label(win, text='Gaming',font=font_format)
l2.grid(row=1,column=2)
l3 = Label(win, text='Exercise',font=font_format)
l3.grid(row=2,column=0)
l4 = Label(win, text='Study',font=font_format)
l4.grid(row=2,column=2)
l5 = Label(win, text='Yoga',font=font_format)
l5.grid(row=3,column=0)
l6 = Label(win, text='Coding',font=font_format)
l6.grid(row=3,column=2)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=1,column=1,ipadx=20,ipady=3)

gaming_text = StringVar()
e2 = Entry(win, textvariable=gaming_text)
e2.grid(row=1,column=3,ipadx=20,ipady=3)

exercise_text = StringVar()
e3 = Entry(win, textvariable=exercise_text)
e3.grid(row=2,column=1,ipadx=20,ipady=3)

study_text = StringVar()
e4 = Entry(win, textvariable=study_text)
e4.grid(row=2,column=3,ipadx=20,ipady=3)

yoga_text = StringVar()
e5 = Entry(win, textvariable=yoga_text)
e5.grid(row=3,column=1,ipadx=20,ipady=3)

coding_text = StringVar()
e6 = Entry(win, textvariable=coding_text)
e6.grid(row=3,column=3,ipadx=20,ipady=3)

list = Listbox(win,height=15,width=60)
list.grid(row=4,column=0,rowspan=9,columnspan=2)
list.DataFrame()

sb = Scrollbar(win)
sb.grid(row=4,column=2,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(win,text='ADD',width=12,pady=5,command=add_command ,font=font_format)
b1.grid(row=4,column=3)

b2 = Button(win,text='Search',width=12,pady=5,command=search_command ,font=font_format)
b2.grid(row=5,column=3)

b3 = Button(win,text='Delete date',width=12,pady=5,command=delete_command ,font=font_format)
b3.grid(row=6,column=3)

b4 = Button(win,text='View all',width=12,pady=5,command=view_command ,font=font_format)
b4.grid(row=7,column=3)

b5 = Button(win,text='Close',width=12,pady=5,command = win.destroy ,font=font_format)
b5.grid(row=8,column=3)

win.mainloop()
