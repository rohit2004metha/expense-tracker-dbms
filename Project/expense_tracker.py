import mysql.connector
import json
from tkinter import PhotoImage 
from tkinter import *
from tkinter import messagebox

# Connect to database

with open('Scripts\\Project\\myconfig.json','r') as c:
    params= json.load(c)['params']

#     mydb = mysql.connector.connect(
#     host=params['host'],
#     user=params['username'],
#     password=params['password'],
#     database= params['database'],
#     port = 3306
# )
mydb = mysql.connector.connect(host=params['host'], user=params['username'], password=params['password'], database=params['database'])

def check_username_exists(db, username):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM USERSINFO WHERE USER_NAME = %s", (username,))
    count = cursor.fetchone()[0]
    return count > 0

def check_passwords_match(password, retype_password):
    return password == retype_password

def clear_variables():
    register_usrname.delete(0, tk.END)
    register_firstname.delete(0, tk.END)
    register_lastname.delete(0, tk.END)
    register_mobile.delete(0, tk.END)
    register_bal.delete(0, tk.END)
    register_pwd.delete(0, tk.END)
    pwd_again.delete(0, tk.END)


import tkinter as tk
import mysql.connector

def registerUser(db):
    reg_cursor = db.cursor()

    # Check if the username is not blank
    usr_name=register_usrname.get() 
    if usr_name.strip() == "":
        # Show an appropriate pop-up message
        messagebox.showerror("Error", "Username cannot be blank")
        return

    fname = register_firstname.get()
    lname= register_lastname.get()
    mob= register_mobile.get().strip()
    dob = '2001-01-01'
    gen = var.get()
    ini_bal = register_bal.get()
    password = register_pwd.get()
    retype_password = pwd_again.get()

    try:
        # Check if the username  or Password is not blank
        usr_name=register_usrname.get() 
        password=register_pwd.get() 
        if (usr_name.strip() == "" and password.strip() == ""):
            # Show an appropriate pop-up message
            messagebox.showerror("Error", "Username or Password cannot be blank")
            return

        # Check if the password and retype password match
        if not check_passwords_match(password, retype_password):
            # Show an appropriate pop-up message
            messagebox.showerror("Error", "Passwords do not match")
            return

        # Insert the user data into the database
        reg_cursor.execute(f"INSERT INTO USERSINFO(USER_NAME, FIRST_NAME, LAST_NAME, MOBILE_NUMBER, DOB, GENDER, INITIAL_BAL, PASSWORDS) VALUES ('\
            {usr_name}', '{fname}', '{lname}', {mob}, '{dob}',{gen}, {ini_bal},'{password}')")

        # Commit the changes
        db.commit()

        # Close the cursor
        reg_cursor.close()

        # Clear the variables
        clear_variables()

        # Show a success message
        messagebox.showinfo("Success", "User registered successfully")

    except Exception as e:
        # Show an error message
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def delete_labels_and_buttons(frame):
  """Deletes all labels and buttons from the given frame."""
  for child in frame.winfo_children():
    if isinstance(child, tk.Label) or isinstance(child, tk.Button) or isinstance(child,tk.Entry) or isinstance(child,tk.Radiobutton)or isinstance(child,tk.StringVar):
      child.destroy()

def create_table(db, user_name,frame):
    """Creates a table in the given frame."""

    # Create a list of headings
    headings = ["Time Stamp", "Description", "Amount"]

     # Create a cursor object
    cursor = db.cursor()

    # Execute a query to get the old expense
    cursor.execute(f"SELECT TIME_STAMP,DESCRIPTION_OF_EXPENSE, AMOUNT FROM EXPENSE_TRACKER where USER_NAME='{user_name}' ORDER BY TIME_STAMP ASC;")

    # Get the old expense from the cursor object
    past_expense = cursor.fetchall()

    # Create a table layout
    # table_frame = tk.Frame(frame)
    # table_frame.pack()

    # Create a label for each heading
    for i, heading in enumerate(headings):
        tk.Label(frame, text=heading).grid(row=0, column=i)

    # Create an entry widget for each data item
    for i, row in enumerate(past_expense):
        for j, column in enumerate(row):
            tk.Label(frame, text=column).grid(row=i + 1, column=j)
    
    try:
        frame.update()
    except:
        pass

def addExpense(db, user_name, description_of_expense, amount):
    """Adds a new expense to the expense tracker."""

    # Create a cursor object
    cursor = db.cursor()

    # Execute an SQL statement to insert the new expense into the database
    cursor.execute(f"INSERT INTO EXPENSE_TRACKER(USER_NAME, DESCRIPTION_OF_EXPENSE, AMOUNT) VALUES('{user_name}', '{description_of_expense}', {amount});")

    # Commit the changes
    db.commit()

    # Close the cursor object
    cursor.close()


def homePage(window,l_frame,r_frame, db, user_name):
    # Create a bottom frame at the bottom of the main window
    bottom_frame = Frame(window, width=1200, height=100, bg="#b1a5cc")
    bottom_frame.place(relx=0.5,rely=0.9,anchor='s')

    def updateBal(db,bottom_frame):
        # Create a cursor object
        cursor = db.cursor()

        # Execute a query to check if the user credentials exist in the database
        cursor.execute(f"SELECT BALANCE FROM ACCOUNT_INFO WHERE USER_NAME = '{user_name}'" )

        # Get the results of the query
        amt = cursor.fetchone()[0]
        cursor.close()
        
        amt_label = Label(bottom_frame, text=f"Remaining Amount: {amt}", font="Arial 20 bold")
        amt_label.pack(padx=10,pady=10)
        
    
    amt = updateBal(db,bottom_frame)
    

    create_table(db, user_name, r_frame)
    
    Label(l_frame, text="Enter Item", bg='#b1a5cc',font=f,background='#b1a5cc',).grid(row=0, column=0, sticky=W, pady=10)

    Label(l_frame, text="Add Amount", bg='#b1a5cc', font=f,background='#b1a5cc',).grid(row=1, column=0, sticky=W, pady=10)

    register_Item = Entry(l_frame, font=f)

    register_Amount = Entry(l_frame, font=f)

    register_btn = Button(l_frame, width=15, text='Add', font=f, relief=SOLID, cursor='hand2', command=
                          lambda: [addExpense(db,user_name,register_Item.get(),register_Amount.get()),create_table(db, user_name, r_frame),updateBal(db,bottom_frame)])

    register_Item.grid(row=0, column=1, pady=10, padx=20) 
    register_Amount.grid(row=1, column=1, pady=10, padx=20)
    register_btn.grid(row=2, column=0, columnspan=2, pady=10)


def login(db,win,left_frame,right_frame,g_frame):
    
    # Check if the username  or Password is not blank
    usr_name=user_name.get() 
    password=pwd_enter.get() 
    if (usr_name.strip() == "" and password.strip() == ""):
        # Show an appropriate pop-up message
        messagebox.showerror("Error", "Username or Password cannot be blank")
        return

    # Create a cursor object
    cursor = db.cursor()

    # Execute a query to check if the user credentials exist in the database
    cursor.execute("SELECT * FROM USERSINFO WHERE USER_NAME = %s AND PASSWORDS = %s", (usr_name, password))

    # Get the results of the query
    results = cursor.fetchone()

    # Close the cursor object
    cursor.close()

    # If the results are not empty, then the user credentials match
    if results is not None:
        # Show a success message
        messagebox.showinfo("Success", "Login successful")

        g_frame.destroy()
        delete_labels_and_buttons(left_frame)
        delete_labels_and_buttons(right_frame)

        # Display home page
        homePage(win,left_frame,right_frame,db,usr_name)

    else:
        # Show an error message
        messagebox.showerror("Error", "Invalid username or password")
    



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
var.set(1)

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
    text="Contact Number",bg='#fff',font=f,foreground='#250073').grid(row=2,column=0,sticky=W,pady=10)

Label(right_frame,
    text="Select Gender",bg='#fff',font=f,foreground='#250073').grid(row=3,column=0,sticky=W,pady=10)

Label(right_frame,
    text="Register Username",bg='#fff',font=f,foreground='#250073').grid(row=4,column=0,sticky=W,pady=10)

Label(right_frame,text="Enter Password",bg='#fff',font=f,foreground='#250073').grid(row=5,column=0,sticky=W,pady=10)

Label(right_frame,text="Re-Enter Password",bg='#fff',font=f,foreground='#250073').grid(row=6,column=0,sticky=W,pady=10)

Label(right_frame,text="Initial Balance",bg='#fff',font=f,foreground='#250073').grid(row=7  ,column=0,sticky=W,pady=10)

gender_frame = LabelFrame(right_frame,bg='#ffffff',bd=2,padx=10,pady=10,foreground='#250073')

register_firstname = Entry(right_frame,font=f,bd=2,foreground='#250073')
register_lastname = Entry(right_frame,font=f,bd=2,foreground='#250073')
register_usrname = Entry(right_frame,font=f,bd=2,foreground='#250073')
register_mobile = Entry(right_frame,font=f,bd=2,foreground='#250073')
male_rb = Radiobutton(gender_frame,text='Male',bg='#ffffff',variable=var,value=1,foreground='#250073',font=('Times',10))
female_rb = Radiobutton(gender_frame,text='Female',bg='#ffffff',variable=var,value=2,foreground='#250073',font=('Times',10))
register_pwd = Entry(right_frame,font=f,bd=2,foreground='#250073',show='*')
pwd_again = Entry(right_frame,font=f,bd=2,foreground='#250073',show='*')
register_bal = Entry(right_frame,font=f,bd=2,foreground='#250073')
register_btn = Button(right_frame,width=15,text='Register',font=f,background='#fff',relief="solid",cursor='hand2',command= lambda: registerUser(mydb),foreground="#250073")

register_firstname.grid(row=0,column=1,pady=10,padx=20)
register_lastname.grid(row=1,column=1,pady=10,padx=20)
register_mobile.grid(row=2,column=1,pady=10,padx=20)
gender_frame.grid(row=3,column=1,pady=10,padx=20)
register_usrname.grid(row=4,column=1,pady=10,padx=20) 
register_pwd.grid(row=5,column=1,pady=10,padx=20)
pwd_again.grid(row=6 ,column=1,pady=10,padx=20)
register_bal.grid(row=7,column=1,pady=10,padx=20)
register_btn.grid(row=8,column=1,pady=10,padx=20)
# right_frame.place(relx=0.75,rely=0.5,anchor="center")
right_frame.place(relx=0.75,y=150,anchor="n")

male_rb.pack(expand=True,side=LEFT)
female_rb.pack(expand=True,side=LEFT)

left_frame = Frame(window,bd=2,bg='#b1a5cc',relief=SOLID,padx=10,pady=10)

Label(left_frame,text="UserName",bg='#b1a5cc',font=f,foreground='#250073').grid(row=0,column=0,sticky=W,pady=10)

Label(left_frame,text="Password",bg='#b1a5cc',font=f,foreground='#250073').grid(row=1,column=0,pady=10)

user_name = Entry(left_frame,font=f,bd=2,foreground='#250073',background='#ddd9de')
pwd_enter = Entry(left_frame,font=f,bd=2,foreground='#250073',background='#ddd9de',show='*')
login_btn = Button(left_frame,width=15,text='Login',font=f,foreground='#250073',relief=SOLID,cursor='hand2',command=lambda: login(mydb,window,left_frame,right_frame,gender_frame),bg='#b1a5cc')

user_name.grid(row=0,column=1,pady=10,padx=20)
pwd_enter.grid(row=1,column=1,pady=10,padx=20)
login_btn.grid(row=2,column=1,pady=10,padx=20)
left_frame.place(relx=0.25,y=150,anchor="n")


# if __name__ == "__main__":

window.mainloop()
