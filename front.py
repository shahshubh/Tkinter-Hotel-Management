from tkinter import *
import back

def get_selected_row(event):
	global selected_tuple
	index=list1.curselection()[0]
	selected_tuple=list1.get(index)
	entry1.delete(0,END)
	entry1.insert(END,selected_tuple[1])
	entry2.delete(0,END)
	entry2.insert(END,selected_tuple[2])
	entry3.delete(0,END)
	entry3.insert(END,selected_tuple[3])
	entry4.delete(0,END)
	entry4.insert(END,selected_tuple[4])
	entry5.delete(0,END)
	entry5.insert(END,selected_tuple[5])
	entry6.delete(0,END)
	entry6.insert(END,selected_tuple[6])

def view_command():
	list1.delete(0,END)
	for row in back.view():
		list1.insert(END,row)

def search_command():
	list1.delete(0,END)
	for row in back.search(name_text.get(),address_text.get(),phone_number.get(),room_type.get(),stay_duration.get(),amount_text.get()):
		list1.insert(END,row)

def add_command():
	back.insert(name_text.get(),address_text.get(),phone_number.get(),stay_duration.get(),room_type.get(),amount_text.get())
	#list1.delete(0,END)
	#list1.insert(END,(name_text.get(),address_text.get(),phone_number.get(),stay_duration.get(),room_type.get(),amount_text.get()))
	view_command()
	
def delete_command():
	back.delete(selected_tuple[0])
	view_command()

def update_command():
	back.update(selected_tuple[0],name_text.get(),address_text.get(),phone_number.get(),room_type.get(),stay_duration.get(),amount_text.get())
	view_command()

def clear_command():
	entry1.delete(0,END)
	entry2.delete(0,END)
	entry3.delete(0,END)
	entry4.delete(0,END)
	entry5.delete(0,END)
	entry6.delete(0,END)

window=Tk()
window.title("Hotel Management")


label1=Label(window,text="Hotel Highland",font="Times 24 bold",fg="blue")
label1.grid(row=0,column=1)

label2=Label(window,text="Name",font="Times 14")
label2.grid(row=1,column=0)

label3=Label(window,text="Address",font="Times 14")
label3.grid(row=2,column=0)

label4=Label(window,text="Phone Number",font="Times 14")
label4.grid(row=3,column=0)

label5=Label(window,text="Number of days you wanna stay in: ",font="Times 14")
label5.grid(row=4,column=0)

label6=Label(window,text="Room type(normal, king or deluxe)",font="Times 14")
label6.grid(row=5,column=0)

label7=Label(window,text="Total amt: ",font="Times 14")
label7.grid(row=6,column=0)

name_text=StringVar()
entry1=Entry(window,textvariable=name_text,font="Times 14")
entry1.grid(row=1,column=1)

address_text=StringVar()
entry2=Entry(window,textvariable=address_text,font="Times 14")
entry2.grid(row=2,column=1)

phone_number=StringVar()
entry3=Entry(window,textvariable=phone_number,font="Times 14")
entry3.grid(row=3,column=1)

stay_duration=StringVar()
entry4=Entry(window,textvariable=stay_duration,font="Times 14")
entry4.grid(row=4,column=1)

room_type=StringVar()
entry5=Entry(window,textvariable=room_type,font="Times 14")
entry5.grid(row=5,column=1)

amount_text=StringVar()
entry6=Entry(window,textvariable=amount_text,font="Times 14")
entry6.grid(row=6,column=1)


list1=Listbox(window,height=20,width=50,font="Times 14")
list1.grid(row=1,column=4,rowspan=6,columnspan=2)

scrl=Scrollbar(window)
scrl.grid(row=1,column=3,sticky='ns',rowspan=6)

list1.configure(yscrollcommand=scrl.set)
scrl.configure(command=list1.yview, bg="black")

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window,text="view all", width=12, command=view_command,bg="#6610F2",fg="white",font="Times 14 italic")
b1.grid(row=7,column=0,padx=10,pady=10)

b2=Button(window,text="add entry", width=12, command=add_command,bg="#E6C229",fg="black",font="Times 14 italic")
b2.grid(row=8,column=0,padx=10,pady=10)

b3=Button(window,text="delete entry", width=12, command=delete_command, bg="#D11149",fg="white",font="Times 14 italic")
b3.grid(row=9,column=0,padx=10,pady=10)

b4=Button(window,text="search", width=12, command=search_command,bg="#389AD6",fg="white",font="Times 14 italic")
b4.grid(row=7,column=1,padx=10,pady=10)

b5=Button(window,text="update", width=12, command=update_command,bg="#F17105",fg="white",font="Times 14 italic")
b5.grid(row=8,column=1,padx=10,pady=10)

b6=Button(window,text="clear", width=12, command=clear_command,bg="white",fg="black",font="Times 14 italic")
b6.grid(row=9,column=1,padx=10,pady=10)

window.mainloop()