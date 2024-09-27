from tkinter import*
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import tkinter as tk
import mysql.connector

class login:
    def __init__ (self,top):
        self.top=top
        self.top.title("LOGIN PAGE")
        self.top.geometry("1560x670+0+0")
#login poage image
        frame1 = Frame(top, width=1560, height=670)
        frame1.place(x=0, y=0)

        
        image_path = "C:/Users/Software_PC/Downloads/desktop-wallpaper-backgrounds-for-login-page-login-page.jpg"
        image0 = Image.open(image_path)
        resized_image = image0.resize((1500, 665))  # Resize the image to fit the frame
        photo = ImageTk.PhotoImage(resized_image)
        label = Label(frame1, image=photo,bg='black', bd=3, relief='solid')
        label.photo = photo  # Keep a reference to the image to prevent garbage collection
        label.place(x=0, y=0)
        #text=Label(top,text="HAVE A PLEASURE WORK",fg="black",font=("display",25,"bold")).place(x=480,y=100)
        frame = Frame(top, bg="lightgrey", width=550, height=300)
        frame.place(x=400, y=190)
        user = Label(frame, text="LOGIN ID",font=("display",15,"bold"))
        user.place(x=250, y=40)
        username = Label(frame, text="USERNAME:",font=("display",13,"bold"))
        username.place(x=100, y=120)
        self.e=Entry(frame,width='50')
        self.e.place(x=230, y=120)
        password = Label(frame, text="PASSWORD:",font=("display",13,"bold"))
        password.place(x=100, y=160)
        self.e1=Entry(frame,width='50',show="*")
        self.e1.place(x=230, y=160)
        b1=Button(frame,text="SIGNIN",background="skyblue",command=self.loginpage)
        b1.place(x=250,y=230)



#login entry
    def loginpage(self):
        user_name=self.e.get()
        pass_word=self.e1.get()
        if  (user_name=="A" and  pass_word=="23"):
            messagebox.showinfo("login, successfully completed")  
            self.top.destroy()
            top=Tk()
            menu(top)
            top.mainloop()

        else:
            messagebox.showinfo("kindly enter the password correct")
                
         

class menu:
    def __init__(self,top):
        self.top=top
        self.top.title("BANK MANAGEMENT")
        self.top.geometry("1560x670+0+0")
     ##---------------------------- logo-----------------------------------##
        image = Image.open("C://Users//Software_PC//Downloads//CANBK.NS.png")
        image_resized = image.resize((150, 95))
        image_1 = ImageTk.PhotoImage(image_resized)
        label = Label(top, image=image_1,bg='black', bd=3, relief='solid')
        label.image_1 = image_1
        label.place(x=0, y=0)
        title=Label(self.top,text="BANKING MANAGEMENT",fg='black',bg='white',font=('times new roman',30,'bold'),border='10',relief='ridge').place(x=161,y=0,width='1195',height='100')
##for menu bar button
        main_frame=Frame(self.top,width='150',height='200')
        main_frame.pack()
        main_frame.pack(anchor='nw', padx=0, pady=101)
        button1=Button(self.top,text="WELCOME ! FEED YOUR INFORMATION............",bg="#B1F9A4",fg="black",activebackground="#00b2ca",font=("serif",14,"bold"),width="115",height='1').place(x=0,y=105)
        button3=Button(self.top,text="MENU",bg="#B1F9A4",activebackground="#00b2ca",fg="black",font=("serif",11,"bold"),width="20",height='1').place(x=0,y=170)
        button4=Button(self.top,text="ACCOUNT DETAILS",bg="#B1F9A4",activebackground="#00b2ca",fg="black",font=("serif",11,"bold"),width="20",height='1',command=self.account_page).place(x=0,y=210)
        button5=Button(self.top,text="ATM DETAILS",bg="#B1F9A4",activebackground="#00b2ca",fg="black",font=("serif",12,"bold"),width="18",height='1',command=self. atm_page).place(x=1,y=250)
#side images
        image2 = Image.open("C:/Users/Software_PC/Downloads/download.jfif")
        image_resized_1= image2.resize((185, 180))
        image_3 = ImageTk.PhotoImage(image_resized_1)
        label = Label(top, image=image_3, bd=3, relief='solid')
        label.image_3 = image_3
        label.place(x=0, y=295)
        image4 = Image.open("C:/Users/Software_PC/Downloads/images (2).jfif")
        image_resized_2= image4.resize((185, 175))
        image_5 = ImageTk.PhotoImage(image_resized_2)
        label = Label(top, image=image_5,bg='black', bd=3, relief='solid')
        label.image_5 = image_5
        label.place(x=0, y=485)

        #background image
       
        background = Image.open("C:/Users/Software_PC/Downloads/pexels-movievolkov-15086546.jpg")
        bg_resized_2 = background.resize((1075, 520))  # Ensure the size matches the frame
        background_image_1 = ImageTk.PhotoImage(bg_resized_2)

    
        label = Label(top, image=background_image_1)
        label.image = background_image_1
        label.place(x=195, y=145)
    def account_page(self):
        self.top.destroy()
        top=Tk()
        bank_details(top)
        top.mainloop()
    def atm_page(self):
        self.top.destroy()
        top=Tk()
        ATMdetails(top)
        top.mainloop()
class bank_details:
    def __init__(self,top):
        self.top=top
        self.top.geometry("1560x670+0+0")
        self.top.title("ACCOUNT DETAILS")
        image = Image.open("C://Users//Software_PC//Downloads//CANBK.NS.png")
        image_resized = image.resize((150, 95))
        image_1 = ImageTk.PhotoImage(image_resized)
        label = Label(top, image=image_1,bg='black', bd=3, relief='solid')
        label.image_1 = image_1
        label.place(x=0, y=0)
        title=Label(self.top,text="ACCOUNT DETAILS",fg='black',bg='white',font=('times new roman',30,'bold'),border='10',relief='ridge').place(x=161,y=0,width='1195',height='100')
        background = Image.open("C://Users//Software_PC//Downloads//CANBK.NS_BIG.png")
        bg_resized_2 = background.resize((800, 300))
        background_image_1 = ImageTk.PhotoImage(bg_resized_2)
        label = Label(top, image=background_image_1)
        label.background_image_1 = background_image_1  # Prevent garbage collection
        label.place(x=450, y=290)
##for menu bar button

      
#label AND PLACE for ATM
        n2=tk.Label(top,text="USER NAME:",fg="black",font=("display",12,"bold")).place(x=0,y=150)
        n3=tk.Label(top,text="DATE OF BIRTH:",fg="black",font=("display",12,"bold")).place(x=0,y=180)
        n4=tk.Label(top,text="AGE:",fg="black",font=("display",12,"bold")).place(x=0,y=210)
        n5=tk.Label(top,text="ACCOUNT NO:",fg="black",font=("display",12,"bold")).place(x=0,y=240)
        n6=tk.Label(top,text="EMAIL ID:",fg="black",font=("display",12,"bold")).place(x=0,y=270)
        n7=tk.Label(top,text="ID DOCUMENT ",fg="black",font=("display",12,"bold")).place(x=0,y=300)
        n8=tk.Label(top,text="ADDRESS :",fg="black",font=("display",12,"bold")).place(x=0,y=330)
        n9=tk.Label(top,text="ACCOUNT TYPE I:",fg="black",font=("display",12,"bold")).place(x=0,y=380)
        n10=tk.Label(top,text="ACCOUNT TYPE II:",fg="black",font=("display",12,"bold")).place(x=0,y=500)
        n11=tk.Label(top,text="BRANCH",fg="black",font=("display",12,"bold")).place(x=0,y=530)
        n12=tk.Label(top,text="IFSC CODE",fg="black",font=("display",12,"bold")).place(x=0,y=560)
        n13=tk.Label(top,text="PHONE NO:",fg="black",font=("display",12,"bold")).place(x=0,y=590)
#ENTRY FOR ATM
       
        self.e1 = tk.Entry(top, width=35)
        self.e1.place(x=150, y=150)

        self.e2 = tk.Entry(top, width=35)
        self.e2.place(x=150, y=180)

        self.e3 = tk.Entry(top, width=35)
        self.e3.place(x=150, y=210)

        self.e4 = tk.Entry(top, width=35)
        self.e4.place(x=150, y=240)

        self.e5 = tk.Entry(top, width=35)
        self.e5.place(x=150, y=270)

        self.c1 = ttk.Combobox(top, values=["AADHAR", "DRIVING LISENCE", "PAN NUMBER", "OTHER"], width=32)
        self.c1.place(x=150, y=300)

        self.e7 = tk.Entry(top, width=35)
        self.e7.place(x=150, y=330)

        
        self.e8 = ttk.Combobox(top,values=["DOMESTIC","INTERNATIONAL"],width=32)
        self.e8.place(x=150, y=380)

       

        self.e10 = ttk.Combobox(top, values=["saving", "Current"], width=32)
        self.e10.place(x=150, y=500)

        self.e11 = tk.Entry(top, width=35)
        self.e11.place(x=150, y=530)

        self.e12 = tk.Entry(top, width=35)
        self.e12.place(x=150, y=560)

        self.e13 = tk.Entry(top, width=35)
        self.e13.place(x=150, y=590)
        
        #BUTTON FOR SAVE, EXIT,CANCEL,UPDATE



        self.frame1 = Frame(self.top, width=930, height=300, bd=4, relief='ridge')
        self.frame1.place(x=400, y=150, width=910, height=500)
        
        scroll_x = ttk.Scrollbar(self.frame1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame1, orient=VERTICAL)
        
        self.bank_table = ttk.Treeview(self.frame1, columns=("USERNAME", "DATEOFBIRTH", "AGE", "ACCOUNTNO", "EMAIL", "IDDOCUMENT", "ADDRESS", "ACCOUNTTYPE1", "ACCOUNTTYPE2", "BRANCH", "IFSCCODE", "PHONENO"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.bank_table.xview)
        scroll_y.config(command=self.bank_table.yview)
       
        self.bank_table.heading("USERNAME", text="USERNAME")
        self.bank_table.heading("DATEOFBIRTH", text="DATEOFBIRTH")
        self.bank_table.heading("AGE", text="AGE")
        self.bank_table.heading("ACCOUNTNO", text="ACCOUNTNO")
        self.bank_table.heading("EMAIL", text="EMAIL")
        self.bank_table.heading("IDDOCUMENT", text="IDDOCUMENT")
        self.bank_table.heading("ADDRESS", text="ADDRESS")
        self.bank_table.heading("ACCOUNTTYPE1", text="ACCOUNTTYPE1")
        self.bank_table.heading("ACCOUNTTYPE2", text="ACC0UNTTYPE2")
        self.bank_table.heading("BRANCH", text="BRANCH")
        self.bank_table.heading("IFSCCODE", text="IFSCCODE")
        self.bank_table.heading("PHONENO", text="PHONENO")
        
        self.bank_table['show'] = 'headings'
      
        self.bank_table.column("USERNAME", width=100)
        self.bank_table.column("DATEOFBIRTH", width=100)
        self.bank_table.column("AGE", width=100)
        self.bank_table.column("ACCOUNTNO", width=100)
        self.bank_table.column("EMAIL", width=100)
        self.bank_table.column("IDDOCUMENT", width=100)
        self.bank_table.column("ADDRESS", width=100)
        self.bank_table.column("ACCOUNTTYPE1", width=100)
        self.bank_table.column("ACCOUNTTYPE2", width=100)
        self.bank_table.column("BRANCH", width=100)
        self.bank_table.column("IFSCCODE", width=100)
        self.bank_table.column("PHONENO", width=100)
        
        self.bank_table.pack(fill=BOTH, expand=1)
        self.fetch_data1()
        
   
        #BUTTON FOR SAVE, EXIT,CANCEL,UPDATE
        self.b1 = tk.Button(top, text="SAVE", width=10, activebackground="dark blue", background="#0DAD8D", font=("times new roman", 10, "bold"), command=self.save2)
        self.b1.place(x=3, y=640)

        self.b2 = tk.Button(top, text="DELETE", width=10, background="#0DAD8D", activebackground="dark blue", font=("times new roman", 10, "bold"), command=self.delete_data1)
        self.b2.place(x=75, y=640)

        self.b3 = tk.Button(top, text="UPDATE", width=10, background="#0DAD8D", activebackground="dark blue", font=("times new roman", 10, "bold"), command=self.update1)
        self.b3.place(x=150, y=640)

        self.b4 = tk.Button(top, text="EXIT", width=10, background="#0DAD8D", activebackground="dark blue", font=("times new roman", 10, "bold"), command=self.back1)
        self.b4.place(x=230, y=640)

        self.b5 = tk.Button(top, text="VIEW", width=10, background="#0DAD8D", activebackground="dark blue", font=("times new roman", 10, "bold"), command=self.view_button1)
        self.b5.place(x=310, y=640)
    def save2(self):
        try:
            db = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='banking'
            )
            cursor = db.cursor()
            sql = """INSERT INTO account 
                     (USERNAME, `DATEOFBIRTH`, AGE, ACCOUNTNO, EMAIL, IDDOCUMENT, ADDRESS, ACCOUNTTYPE1, ACCOUNTTYPE2, BRANCH, IFSCCODE, PHONENO) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            val = (
                self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), 
                self.c1.get(), self.e7.get(), self.e8.get(), self.e10.get(), self.e11.get(), 
                self.e12.get(), self.e13.get()
            )
            cursor.execute(sql, val)
            db.commit()
            print(cursor.rowcount, "record inserted.")
            messagebox.showinfo("Success", "Record inserted successfully")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            messagebox.showerror("Error", "Failed to insert record")
        finally:
            if db.is_connected():
                cursor.close()
                db.close()

    
    
    def delete_data1(self):
        selected_item = self.e4.get()
        if selected_item:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="", database="banking")
                cursor = con.cursor()
                
                # Debugging: Print the selected item to ensure it is correct
                print(f"Selected ACCOUNTNO: '{selected_item}'")
                
                cursor.execute("DELETE FROM account WHERE ACCOUNTNO=%s;", (selected_item,))
                con.commit()
                
                if cursor.rowcount > 0:
                    print(cursor.rowcount, "record deleted.")
                    messagebox.showinfo("Success", "Record has been deleted")
                else:
                    print("No record found with the given ACCOUNTNO.")
                    messagebox.showwarning("Warning", "No record found with the given ACCOUNTNO.")
            except mysql.connector.Error as err:
                print("Error: ", err)
                messagebox.showerror("Error", f"An error occurred: {err}")
            finally:
                con.close()
        else:
            print("No item selected.")
            messagebox.showwarning("Warning", "No item selected.")


           
    def back1(self):
        self.top.destroy()
        top = Tk()
        menu(top)
        top.mainloop()
   

    def update1(self):
        try:
            m1 = self.e1.get()
            m2 = self.e2.get()
            m3 = self.e3.get()
            m4 = self.e4.get()
            m5 = self.e5.get()
            m6 = self.c1.get()
            m7 = self.e7.get()
            m8 = self.e8.get()
            m10 = self.e10.get()
            m11 = self.e11.get()
            m12 = self.e12.get()
            m13 = self.e13.get()
            print(m4)

            con = mysql.connector.connect(host="localhost", user="root", password="", database="banking")
            cursor = con.cursor()

            sql_query = """UPDATE `account` 
                           SET `USERNAME`=%s, `DATEOFBIRTH`=%s, `AGE`=%s, `EMAIL`=%s, `IDDOCUMENT`=%s, 
                               `ADDRESS`=%s, `ACCOUNTTYPE1`=%s, `ACCOUNTTYPE2`=%s, `BRANCH`=%s, 
                               `IFSCCODE`=%s, `PHONENO`=%s 
                           WHERE `ACCOUNTNO`=%s"""

            values = (m1, m2, m3, m5, m6, m7, m8, m10, m11, m12, m13, m4)

            cursor.execute(sql_query, values)
            con.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Record has been updated")
            else:
                print("No record found with the given ACCOUNTNO.")
                messagebox.showwarning("Warning", "No record found with the given ACCOUNTNO.")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            if con.is_connected():
                con.close()


    def fetch_data1(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="banking")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM account")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.bank_table.delete(*self.bank_table.get_children())
            for row in rows:
                self.bank_table.insert('', END, values=row)
            con.commit()
        con.close()

    def view_button1(self):
        view_button_calling = self.bank_table.focus()
        values =self.bank_table.item(view_button_calling , 'values')

  
        if values:
            self.e1.delete(0, tk.END)
            self.e2.delete(0, tk.END)
            self.e3.delete(0, tk.END)
            self.e4.delete(0, tk.END)
            self.e5.delete(0, tk.END)
            self.c1.delete(0, tk.END)
            self.e7.delete(0, tk.END)
            self.e8.delete(0, tk.END)
            self.e10.delete(0, tk.END)
            self.e11.delete(0,tk.END)
            self.e12.delete(0,tk.END)
            self.e13.delete(0,tk.END)
            
            self.e1.insert(0, values[0])
            self.e2.insert(0, values[1])
            self.e3.insert(0, values[2])
            self.e4.insert(0, values[3])
            self.e5.insert(0, values[4])
            self.c1.insert(0, values[5])
            self.e7.insert(0, values[6])
            self.e8.insert(0, values[7])
            self.e10.insert(0, values[8])
            self.e11.insert(0, values[9])
            self.e12.insert(0, values[10])
            self.e13.insert(0, values[11])
            # Create buttons and place the
 
class ATMdetails():
    def __init__(self,top):
        self.top=top
        self.top.geometry("1560x670+0+0")
        self.top.title("ATM DETAILS")
       
        image = Image.open("C://Users//Software_PC//Downloads//CANBK.NS.png")
        image_resized = image.resize((150, 95))
        image_1 = ImageTk.PhotoImage(image_resized)
        label = Label(top, image=image_1,bg='black', bd=3, relief='solid')
        label.image_1 = image_1
        label.place(x=0, y=0)
        title=Label(self.top,text="ATM USER DETAILS............",fg='black',bg='white',font=('times new roman',30,'bold'),border='10',relief='ridge').place(x=161,y=0,width='1195',height='100')
        background = Image.open("C://Users//Software_PC//Downloads//CANBK.NS_BIG.png")
        bg_resized_2 = background.resize((800, 300))
        background_image_1 = ImageTk.PhotoImage(bg_resized_2)
        label = Label(top, image=background_image_1)
        label.background_image_1 = background_image_1  # Prevent garbage collection
        label.place(x=450, y=290)
##for 

#label AND PLACE for ATM
       
        n2=tk.Label(top,text="USER NAME:",fg="black",font=("times new roman",12,"bold")).place(x=5,y=200)
        n3=tk.Label(top,text="ACCOUNT NO:",fg="black",font=("times new roman",12,"bold")).place(x=5,y=230)                                                                               
        n4=tk.Label(top,text="EMAIL ID:",fg="black",font=("times new roman",12,"bold")).place(x=5,y=260)
        n5=tk.Label(top,text="CARD NO:",fg="black",font=("times new roman",12,"bold")).place(x=5,y=290)
        n6=tk.Label(top,text="CARD TYPE I :",fg="black",font=("times new roman",12,"bold")).place(x=5,y=320)
        n7=tk.Label(top,text="CARD TYPE II :",fg="black",font=("times new roman",12,"bold")).place(x=5,y=350)
        n8=tk.Label(top,text="CARD STATUS:",fg="black",font=("times new roman",12,"bold")).place(x=5,y=380)
        n9=tk.Label(top,text="CARD ISSUER:",fg="black",font=("times new roman",12,"bold")).place(x=5,y=410)
        n10=tk.Label(top,text="C.EXPIRE DATE",fg="black",font=("times new roman",12,"bold")).place(x=5,y=440)
        n11=tk.Label(top,text="PHONE NO:",fg="black",font=("times new roman",12,"bold")).place(x=5,y=470)
#ENTRY FOR ATM
       
        self.e1 = tk.Entry(top, width=40)
        self.e1.place(x=155, y=200)

        self.e2 = tk.Entry(top, width=40)
        self.e2.place(x=155, y=230)

        self.e3 = tk.Entry(top, width=40)
        self.e3.place(x=155, y=260)

        self.e4 = tk.Entry(top, width=40)
        self.e4.place(x=155, y=290)

        self.c1 = ttk.Combobox(top, values=["platinum", "gold", "silver"], width=37)
        self.c1.place(x=155, y=320)

        self.c2 = ttk.Combobox(top, values=["Rupay", "Visa", "Master card"], width=37)
        self.c2.place(x=155, y=350)

        self.c3 = ttk.Combobox(top, values=["Active", "Expired", "Blocked"], width=37)
        self.c3.place(x=155, y=380)

        self.e8 = tk.Entry(top, width=40)
        self.e8.place(x=155, y=410)

        self.e9 = tk.Entry(top, width=40)
        self.e9.place(x=155, y=440)

        self.e10 = tk.Entry(top, width=40)
        self.e10.place(x=155, y=470)
        self.frame = Frame(self.top, bd=4, relief='ridge')
        self.frame.place(x=400, y=150, width=900, height=500)

        scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame, orient=VERTICAL)
        self.atm_table = ttk.Treeview(self.frame, columns=("username", "AccountNo", "emailno", "cardno", "cardtype1", "cardtype2", "cardstatus", "cardissuer", "cardexpiredate","phoneno"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.atm_table.xview)
        scroll_y.config(command=self.atm_table.yview)

       
        self.atm_table.heading("username", text="USER NAME")
        self.atm_table.heading("AccountNo", text="ACCOUNT NO")
        self.atm_table.heading("emailno", text="EMAIL ID")
        self.atm_table.heading("cardno", text="CARD NO   ")
        self.atm_table.heading("cardtype1", text="CARD TYPE1")
        self.atm_table.heading("cardtype2", text="CARD TYPE2")
        self.atm_table.heading("cardstatus", text="CARD STATUS")
        self.atm_table.heading("cardissuer",text="CARD ISSURE")

        self.atm_table.heading("cardexpiredate", text="C.EXPIRE DATE")
        self.atm_table.heading("phoneno", text="PHONE NO")

        self.atm_table['show'] = 'headings'

        
        self.atm_table.column("username", width=100)
        self.atm_table.column("AccountNo", width=100)
        self.atm_table.column("emailno", width=100)
        self.atm_table.column("cardno", width=100)
        self.atm_table.column("cardtype1", width=100)
        self.atm_table.column("cardtype2", width=100)
        self.atm_table.column("cardstatus", width=100)
        self.atm_table.column("cardissuer", width=100)
        self.atm_table.column("cardexpiredate", width=100)
        self.atm_table.column("phoneno", width=100)

        self.atm_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.view_button()
        

#BUTTON FOR SAVE, EXIT,CANCEL,UPDATE
        self.b1=tk.Button(top,text="SAVE",width='10',activebackground="dark blue",background="#0DAD8D",font=("times new roman",10,"bold"),command=self.add_atm).place(x=00,y=600)
        self.b2=tk.Button(top,text="DELETE",width='10',background="#0DAD8D",activebackground="dark blue",font=("times new roman",10,"bold"),command=self.delete_data).place(x=75,y=600)
        self.b3=tk.Button(top,text="UPDATE",width='10',background="#0DAD8D",activebackground="dark blue",font=("times new roman",10,"bold"),command=self.update_data).place(x=150,y=600)
        self.b4=tk.Button(top,text="EXIT",width='10',background="#0DAD8D",activebackground="dark blue",font=("times new roman",10,"bold"),command=self.back2).place(x=230,y=600)
        self.b5=tk.Button(top,text="VIEW",width='10',background="#0DAD8D",activebackground="dark blue",font=("times new roman",10,"bold"),command=self.view_button).place(x=310,y=600)
    def add_atm(self):
        try:
            db = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='banking'
            )
            cursor = db.cursor()
            sql = """INSERT INTO atm 
                     (USERNAME, ACCOUNTNO, EMAILID, CARDNO, CARDTYPE1, CARDTYPE2, CARDSTATUS, CARDISSUER, CARDEXPIREDATE, `PHONENO`) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            val = (
                self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), 
                self.c1.get(), self.c2.get(), self.c3.get(), self.e8.get(), 
                self.e9.get(), self.e10.get()
            )
            print(val)
            cursor.execute(sql, val)
            db.commit()
            print(cursor.rowcount, "record inserted.")
            messagebox.showinfo("Success", "Record inserted successfully")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            messagebox.showerror("Error", "Failed to insert record")
        finally:
            if db.is_connected():
                cursor.close()
                db.close()

    def view_button(self):
        view_button_calling = self.atm_table.focus()
        values =self.atm_table.item(view_button_calling , 'values')

  
        if values:
            self.e1.delete(0, tk.END)
            self.e2.delete(0, tk.END)
            self.e3.delete(0, tk.END)
            self.e4.delete(0, tk.END)
            self.c1.delete(0, tk.END)
            self.c2.delete(0, tk.END)
            self.c3.delete(0, tk.END)
            self.e8.delete(0, tk.END)
            self.e9.delete(0, tk.END)
            self.e10.delete(0,tk.END)

            
            self.e1.insert(0, values[0])
            self.e2.insert(0, values[1])
            self.e3.insert(0, values[2])
            self.e4.insert(0, values[3])
            self.c1.insert(0, values[4])
            self.c2.insert(0, values[5])
            self.c3.insert(0, values[6])
            self.e8.insert(0, values[7])
            self.e9.insert(0, values[8])
            self.e10.insert(0, values[9])
            # Create buttons and place the

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="banking")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM atm")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.atm_table.delete(*self.atm_table.get_children())
            for row in rows:
                self.atm_table.insert('', END, values=row)
            con.commit()
        con.close()

  
    def delete_data(self):
        selected_item = self.e2.get()
        if selected_item:
    
            con = mysql.connector.connect(host="localhost", user="root", password="", database="banking")
            cursor = con.cursor()
            cursor.execute("DELETE FROM atm WHERE `ACCOUNTNO`=%s",(selected_item,))
            con.commit()
            con.close()
            print(cursor.rowcount, "record deleted.")
            messagebox.showinfo("Success", "Record has been deleted")

    def back2(self):
        self.top.destroy()
        top = Tk()
        menu(top)
        top.mainloop()
    def update_data(self):
        m1 = self.e1.get()
        m2 = self.e2.get()
        m3 = self.e3.get()
        m4 = self.e4.get()
        m5 = self.c1.get()
        m6 = self.c2.get()
        m7 = self.c3.get()
        m8 = self.e8.get()
        m9 = self.e9.get()
        m10 = self.e10.get()

        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="banking")
            cursor = con.cursor()

            sql_query = """UPDATE atm SET
                           USERNAME=%s, ACCOUNTNO=%s, EMAILID=%s, CARDNO=%s, CARDTYPE1=%s, 
                           CARDTYPE2=%s, CARDSTATUS=%s, CARDISSUER=%s, CARDEXPIREDATE=%s, 
                           PHONENO=%s WHERE ACCOUNTNO=%s"""
                
            # Ensure ACCOUNTNO is passed twice, once for update and once for WHERE clause
            values = (m1, m2, m4, m5, m6, m7, m8, m9, m10, m3, m2)
            cursor.execute(sql_query, values)
            con.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Record has been updated")
            else:
                messagebox.showwarning("Warning", "No record found with the given ACCOUNTNO.")
        
        except mysql.connector.Error as err:
            print("Error: ", err)
            messagebox.showerror("Error", f"An error occurred: {err}")
        
        finally:
            con.close()

if __name__ == "__main__":
    top = Tk()
    app = login(top)
    top.mainloop()

