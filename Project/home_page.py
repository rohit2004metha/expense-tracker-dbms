from tkinter import PhotoImage
from tkinter import *

# Create the main window
window = Tk()
window.title('Expense Tracker')
window.config(bg='#b1a5cc')
window.resizable(False, False)
window.geometry("1200x700+100+50")

# Create a Label Widget to display the text or Image
background_image = PhotoImage(file="Scripts\\Project\\1.png")
label = Label(window, image = background_image)
label.place(relx=0.5,rely=0.5,anchor="center")

f = ('Times', 14)

#frame for placing the app name
name_frame = Frame(window, bd=0, bg='#250073', relief=SOLID, padx=2, pady=2 )
app_name_font = ('Oxygen 30 bold')  
app_name = Label(name_frame, text="FinTrack", font=app_name_font ,bg="#fcb603", fg="#250073")
app_name.pack()
name_frame.place(relx=0.5,y=30,anchor="n")

# Create a bottom frame at the bottom of the main window
bottom_frame = Frame(window, width=1200, height=100, bg="#b1a5cc")
bottom_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=40, sticky='s')

label3 = Label(bottom_frame)
label3.place(x=600, y=50, anchor="center")

amt=FALSE
label4 = Label(label3, text=f"Remaining Amount: {amt}")
register_TotalAmount = Entry(label4,font=f)

label4.grid(row=0, column=0, pady=10, padx=20)


# Create a right frame 
r_frame = Frame(window, width=300, height=600, bg="#b1a5cc")
r_frame.grid(row=0, column=2, padx=10, pady=150, sticky='ne')

Label(r_frame, text="", bg='#b1a5cc',font=f).grid(row=0, column=0, sticky=W, pady=10)

register_blank = Entry(r_frame, font=f)
register_blank.grid(row=0, column=1, pady=10, padx=20)

# Create a left frame 
l_frame = Frame(window, width=300, height=600, bg="#b1a5cc")
l_frame.grid(row=0, column=0, padx=50, pady=150, sticky='nw')

Label(l_frame, text="Enter Item", bg='#b1a5cc',font=f,background='#b1a5cc',).grid(row=0, column=0, sticky=W, pady=10)

Label(l_frame, text="Add Amount", bg='#b1a5cc', font=f,background='#b1a5cc',).grid(row=1, column=0, sticky=W, pady=10)

register_Item = Entry(l_frame, font=f)

register_Amount = Entry(l_frame, font=f)

register_btn = Button(l_frame, width=15, text='Add', font=f, relief=SOLID, cursor='hand2', command=None)

register_Item.grid(row=0, column=1, pady=10, padx=20) 
register_Amount.grid(row=1, column=1, pady=10, padx=20)
register_btn.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
