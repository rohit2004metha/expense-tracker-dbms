from tkinter import PhotoImage 
from tkinter import *

#Creating a window to show show UI of Desktop app
window = Tk()
window.title('FinTrack')
window.config(bg='#c5bfc7')
window.resizable(False,False)
window.geometry("1200x700+100+50")

# Create a Label Widget to display the text or Image
background_image = PhotoImage(file="Scripts\\Project\\1.png")
label = Label(window,image = background_image)
label.place(relx=0.5,rely=0.5,anchor="center")

f = ('Oxygen 14')
var = StringVar()
var.set('male')

#frame for placing the app name
name_frame = Frame(window,bd=0,bg='#250073',relief=SOLID,padx=2,pady=2 )
app_name_font = ('Oxygen 30 bold')  
app_name = Label(name_frame,text="FinTrack",font=app_name_font ,bg="#fcb603",fg="#250073")
app_name.pack()
name_frame.place(relx=0.5,y=30,anchor="n")

right_frame = Frame(window,bd=2,bg='#ffffff',relief=SOLID,padx=10,pady=10)

Label(right_frame, text="First Name",bg='#fff',font=f,foreground='#250073').grid(row=0,column=0,sticky=W,pady=10)

Label(right_frame,
    text="Last Name",bg='#fff',font=f,foreground='#250073').grid(row=1,column=0,sticky=W,pady=10)

Label(right_frame,
    text="Enter username",bg='#fff',font=f,foreground='#250073').grid(row=2,column=0,sticky=W,pady=10)

Label(right_frame,
    text="Contact Number",bg='#fff',font=f,foreground='#250073').grid(row=3,column=0,sticky=W,pady=10)

Label(right_frame,
    text="Select Gender",bg='#fff',font=f,foreground='#250073').grid(row=4,column=0,sticky=W,pady=10)

Label(right_frame,text="Enter Password",bg='#fff',font=f,foreground='#250073').grid(row=5,column=0,sticky=W,pady=10)

Label(right_frame,text="Re-Enter Password",bg='#fff',font=f,foreground='#250073').grid(row=6,column=0,sticky=W,pady=10)

gender_frame = LabelFrame(right_frame,bg='#ffffff',bd=2,padx=10,pady=10,foreground='#250073')

register_firstname = Entry(right_frame,font=f,bd=2,foreground='#250073')
register_lastname = Entry(right_frame,font=f,bd=2,foreground='#250073')
register_email = Entry(right_frame,font=f,bd=2,foreground='#250073')
register_mobile = Entry(right_frame,font=f,bd=2,foreground='#250073')
male_rb = Radiobutton(gender_frame,text='Male',bg='#ffffff',variable=var,value=1,foreground='#250073',font=('Times',10))
female_rb = Radiobutton(gender_frame,text='Female',bg='#ffffff',variable=var,value=2,foreground='#250073',font=('Times',10))
register_pwd = Entry(right_frame,font=f,bd=2,foreground='#250073',show='*')
pwd_again = Entry(right_frame,font=f,bd=2,foreground='#250073',show='*')
register_btn = Button(right_frame,width=15,text='Register',font=f,background='#fff',relief="solid",cursor='hand2',command=None,foreground="#250073")

register_firstname.grid(row=0,column=1,pady=10,padx=20)
register_lastname.grid(row=1,column=1,pady=10,padx=20)
register_email.grid(row=2,column=1,pady=10,padx=20) 
register_mobile.grid(row=3,column=1,pady=10,padx=20)
gender_frame.grid(row=4,column=1,pady=10,padx=20)
register_pwd.grid(row=5,column=1,pady=10,padx=20)
pwd_again.grid(row=6 ,column=1,pady=10,padx=20)
register_btn.grid(row=7,column=1,pady=10,padx=20)
# right_frame.place(relx=0.75,rely=0.5,anchor="center")
right_frame.place(relx=0.75,y=150,anchor="n")

male_rb.pack(expand=True,side=LEFT)
female_rb.pack(expand=True,side=LEFT)

left_frame = Frame(window,bd=2,bg='#b1a5cc',relief=SOLID,padx=10,pady=10)

Label(left_frame,text="UserName",bg='#b1a5cc',font=f,foreground='#250073').grid(row=0,column=0,sticky=W,pady=10)

Label(left_frame,text="Password",bg='#b1a5cc',font=f,foreground='#250073').grid(row=1,column=0,pady=10)

email_tf = Entry(left_frame,font=f,bd=2,foreground='#250073',background='#ddd9de')
pwd_tf = Entry(left_frame,font=f,bd=2,foreground='#250073',background='#ddd9de',show='*')
login_btn = Button(left_frame,width=15,text='Login',font=f,foreground='#250073',relief=SOLID,cursor='hand2',command=None,bg='#b1a5cc')

email_tf.grid(row=0,column=1,pady=10,padx=20)
pwd_tf.grid(row=1,column=1,pady=10,padx=20)
login_btn.grid(row=2,column=1,pady=10,padx=20)
left_frame.place(relx=0.25,y=150,anchor="n")


if __name__ == "__main__":
    window.mainloop()