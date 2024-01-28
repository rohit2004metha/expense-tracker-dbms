import tkinter as tk
from tkinter import PhotoImage

class GenderFrame(tk.LabelFrame):
    def __init__(self, master, bg='#ffffff', bd=2, padx=10, pady=10, foreground='#250073'):
        super().__init__(master, bg=bg, bd=bd, padx=padx, pady=pady, foreground=foreground, width=20)
        self.var = tk.StringVar()
        self.var.set('male')

        self.male_rb = tk.Radiobutton(self, text='Male', bg='#ffffff', variable=self.var, value='male', foreground='#250073', font=('Times', 10))
        self.male_rb.grid(row=0,column=0,pady=2,padx=10)

        self.female_rb = tk.Radiobutton(self, text='Female', bg='#ffffff', variable=self.var, value='female', foreground='#250073', font=('Times', 10))
        self.female_rb.grid(row=0,column=1,pady=2,padx=10)


class RegisterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bd=2, relief="solid", bg='#ffffff')
        self.f = ("Oxygen 14")

        self.gender_frame = GenderFrame(self)
        self.register_firstname = tk.Entry(self, font=self.f,foreground='#250073')
        self.register_lastname = tk.Entry(self, font=self.f,foreground='#250073')
        self.register_email = tk.Entry(self, font=self.f,foreground='#250073')
        self.register_mobile = tk.Entry(self, font=self.f,foreground='#250073')
        self.register_pwd = tk.Entry(self, font=self.f,foreground='#250073', show="*")
        self.pwd_again = tk.Entry(self, font=self.f,foreground='#250073', show="*")
        self.register_btn = tk.Button(self, text="Register", font=self.f, width=15, command=None,background='#fff',relief="solid",cursor='hand2')

        self.register_firstname.grid(row=0, column=1, pady=10, padx=20)
        self.register_lastname.grid(row=1, column=1, pady=10, padx=20)
        self.register_email.grid(row=2, column=1, pady=10, padx=20)
        self.register_mobile.grid(row=3, column=1, pady=10, padx=20)
        self.gender_frame.grid(row=4, column=1, pady=10, padx=20)
        self.register_pwd.grid(row=5, column=1, pady=10, padx=20)
        self.pwd_again.grid(row=6, column=1, pady=10, padx=20)
        self.register_btn.grid(row=7, column=1, pady=10, padx=20)

        tk.Label(self, text="First Name", bg='#fff', font=self.f, foreground='#250073').grid(row=0, column=0, pady=10,sticky='w')
        tk.Label(self, text="Last Name", bg='#fff', font=self.f, foreground='#250073').grid(row=1, column=0, sticky='w',pady=10)
        tk.Label(self, text="Enter username", bg='#fff', font=self.f, foreground='#250073').grid(row=2, column=0, sticky='w', pady=10)
        tk.Label(self, text="Contact Number", bg='#fff', font=self.f, foreground='#250073').grid(row=3, column=0, sticky='w', pady=10)
        tk.Label(self, text="Select Gender", bg='#fff', font=self.f, foreground='#250073').grid(row=4, column=0, sticky='w', pady=10)
        tk.Label(self, text="Enter Password", bg='#fff', font=self.f, foreground='#250073').grid(row=5, column=0, sticky='w', pady=10)
        tk.Label(self, text="Re-Enter Password", bg='#fff', font=self.f, foreground='#250073').grid(row=6, column=0, sticky='w', pady=10)


class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bd=2, relief="solid", bg='#b1a5cc')
        self.f = ("Oxygen 14")

        self.email_tf = tk.Entry(self, font=self.f, bg='#ddd9de',bd=2,foreground='#250073')
        self.pwd_tf = tk.Entry(self, font=self.f, show="*", bg='#ddd9de',bd=2,foreground='#250073')
        self.login_btn = tk.Button(self, text="Login", font=self.f, width=15, command=None,bg='#b1a5cc', relief="solid" ,cursor='hand2')

        self.email_tf.grid(row=0, column=1, pady=10, padx=20)
        self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        self.login_btn.grid(row=2, column=1, pady=10, padx=20)

        tk.Label(self, text="UserName", bg='#b1a5cc', font=self.f, foreground='#250073').grid(row=0, column=0, pady=10)
        tk.Label(self, text="Password", bg='#b1a5cc', font=self.f, foreground='#250073').grid(row=1, column=0, pady=10)

class FinTrack(tk.Tk):
    def __init__(self):
        super().__init__()
        self.f = ("Oxygen 14")

        self.title("FinTrack")
        self.config(bg="#c5bfc7")
        self.resizable(False, False)
        self.geometry("1200x700+100+50")

        self.background_image = PhotoImage(file="Scripts\\Project\\1.png")
        self.label = tk.Label(self, image=self.background_image)
        self.label.place(relx=0.5, rely=0.5, anchor="center")

        self.app_name_font = ('Oxygen 30 bold')
        self.app_name = tk.Label(self, text="FinTrack", font=self.app_name_font, bg="#fcb603", fg="#250073")

        self.name_frame = tk.Frame(self, bd=1, bg='#250073',relief='solid', padx=2, pady=2 )
        self.app_name.place(relx=0.5 ,y=40, anchor='n')

        self.register_frame = RegisterFrame(self)
        self.login_frame = LoginFrame(self)

        self.name_frame.place(relx=0.5,y=30,anchor="n")
        self.register_frame.place(x=700,y=150,anchor="nw")
        self.login_frame.place(x=100,y=150,anchor="nw")

if __name__ == "__main__":
    app = FinTrack()
    app.mainloop()
