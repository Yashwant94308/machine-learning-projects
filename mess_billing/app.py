from tkinter import *
from tkinter import messagebox
import mysql.connector
from string import ascii_letters, digits
import pandas as pd


class Bill_App:
    def __init__(self, roots):
        self.root = roots
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (self.width, self.height))
        self.root.title("Mess Management app")
        bg_color = "#074463"

        # ======================add/remove student variable====================================================

        self.uni_roll = IntVar()
        self.room_number = StringVar()
        self.name = StringVar()
        self.branch = StringVar()
        self.batch = StringVar()

        # ====================================search bill var================================================
        self.room_no = StringVar()
        self.month_name = StringVar()
        self.last_room_nu = StringVar()

        # =====================================create new table/change room number===========================

        self.rs_per_diet = DoubleVar()
        self.new_room_number = StringVar()

        # =====================================diets detail=================================================
        self.nam = StringVar()
        self.branc = StringVar()
        self.bat = StringVar()
        self.ser = DoubleVar()
        self.diet = IntVar()
        self.extra = DoubleVar()
        self.adjustment = DoubleVar()
        self.amount = DoubleVar()
        self.total = DoubleVar()
        self.to_be_pay = DoubleVar()
        self.receipt_nu = StringVar()

        title = Label(self.root, text="Mess Billing software", bd=12, bg=bg_color, fg="white",
                      relief=GROOVE, font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # =============================ADD OR REMOVE STUDENT============================ #

        f1 = LabelFrame(self.root, text="ADD/REMOVE STUDENTS", bd=7, bg=bg_color, fg="gold",
                        relief=GROOVE, font=("times new roman", 15, "bold"), pady=2)

        f1.place(x=0, y=70, relwidth=1)

        u_r_number = Label(f1, text="Uni-Roll-No.", font=("times new roman", 18, "bold"),
                           bg=bg_color, fg="white").grid(row=0, column=0, padx=20, pady=5)
        u_r_text = Entry(f1, width=10, textvariable=self.uni_roll, font=("arial", 15), bd=7, relief=SUNKEN).grid(
            row=0, column=1)

        r_number = Label(f1, text="Room No.", font=("times new roman", 18, "bold"),
                         bg=bg_color, fg="white").grid(row=0, column=2, padx=20, pady=5)
        r_text = Entry(f1, width=6, textvariable=self.room_number, font=("arial", 15), bd=7, relief=SUNKEN).grid(
            row=0, column=3)

        s_name = Label(f1, text="Name", font=("times new roman", 18, "bold"),
                       bg=bg_color, fg="white").grid(row=0, column=4, padx=20, pady=5)
        s_name_text = Entry(f1, width=15, textvariable=self.name, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=0, column=5)

        s_branch = Label(f1, text="Branch", font=("times new roman", 18, "bold"),
                         bg=bg_color, fg="white").grid(row=0, column=6, padx=20, pady=5)
        s_branch_text = Entry(f1, width=6, textvariable=self.branch, font=("arial", 15), bd=7,
                              relief=SUNKEN).grid(row=0, column=7)

        s_batch = Label(f1, text="Batch", font=("times new roman", 18, "bold"),
                        bg=bg_color, fg="white").grid(row=0, column=8, padx=20, pady=5)
        s_batch_text = Entry(f1, width=6, textvariable=self.batch, font=("arial", 15), bd=9,
                             relief=SUNKEN).grid(row=0, column=10)

        add = Button(f1, command=self.add_students, width=7, bg="lightyellow", text="Add",
                     font=("times new roman", 18, "bold"),
                     bd=7, relief=SUNKEN).grid(row=0, column=11, padx=10)

        remove = Button(f1, command=self.remove_students, width=7, bg="lightyellow", text="Remove",
                        font=("times new roman", 18, "bold"),
                        bd=7, relief=SUNKEN).grid(row=0, column=12, padx=10)

        # ==================================search==========================================================

        f2 = LabelFrame(self.root, text="SEARCH BILL", bd=7, bg=bg_color, fg="gold",
                        relief=GROOVE, font=("times new roman", 15, "bold"), pady=2)

        f2.place(x=0, y=160, relwidth=1)
        r_number = Label(f2, text="Room No.", font=("times new roman", 18, "bold"),
                         bg=bg_color, fg="white").grid(row=0, column=0, padx=20, pady=5)
        r_text = Entry(f2, width=8, textvariable=self.room_no, font=("arial", 15), bd=7, relief=SUNKEN).grid(
            row=0, column=1)

        m_name = Label(f2, text="Month Name", font=("times new roman", 18, "bold"),
                       bg=bg_color, fg="white").grid(row=0, column=2, padx=20, pady=5)
        m_name_text = Entry(f2, width=10, textvariable=self.month_name, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=0, column=3)

        search = Button(f2, command=self.search_bill_sys, width=7, bg="lightyellow", text="Search",
                        font=("times new roman", 18, "bold"),
                        bd=7, relief=SUNKEN).grid(row=0, column=4, padx=10)

        l_room = Button(f2, command=self.find_last_room, width=9, bg="lightyellow", text="Last-room",
                        font=("times new roman", 18, "bold"),
                        bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10)

        l_name = Label(f2, text="Last Room No. Added", font=("times new roman", 18, "bold"),
                       bg=bg_color, fg="white").grid(row=0, column=6, padx=0, pady=5)
        l_name_text = Entry(f2, width=10, textvariable=self.last_room_nu, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=0, column=7)

        # ======================CREATE TABLE/change room ====================================================

        f4 = LabelFrame(self.root, text="CREATE NEW TABLE/CHANGE ROOM NUMBER", bd=7, bg=bg_color, fg="gold",
                        relief=GROOVE, font=("times new roman", 15, "bold"), pady=2)

        f4.place(x=0, y=250, relwidth=1)

        m_name = Label(f4, text="Month Name", font=("times new roman", 18, "bold"),
                       bg=bg_color, fg="white").grid(row=0, column=1, padx=10, pady=5)
        m_name_text = Entry(f4, width=10, textvariable=self.month_name, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=0, column=2)

        creates = Button(f4, command=self.create_month_table, width=8, bg="lightyellow", text="CREATE",
                         font=("times new roman", 18, "bold"),
                         bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10)

        excel = Button(f4, command=self.export_bill, width=8, bg="lightyellow", text="Exel-type",
                       font=("times new roman", 18, "bold"),
                       bd=7, relief=SUNKEN).grid(row=0, column=4, padx=10)
        r_room = Button(f4, command=self.reset_all_room_no, width=13, bg="lightyellow", text="Reset-room-no",
                        font=("times new roman", 18, "bold"),
                        bd=7, relief=SUNKEN).grid(row=0, column=5, padx=10)

        uni_r_number = Label(f4, text="Uni-Roll", font=("times new roman", 18, "bold"),
                             bg=bg_color, fg="white").grid(row=0, column=8, padx=10, pady=5)
        uni_r_text = Entry(f4, width=9, textvariable=self.uni_roll, font=("arial", 15), bd=7, relief=SUNKEN).grid(
            row=0,
            column=9)

        n_r_number = Label(f4, text="New-room", font=("times new roman", 18, "bold"),
                           bg=bg_color, fg="white").grid(row=0, column=10, padx=10, pady=5)
        n_r_text = Entry(f4, width=8, textvariable=self.new_room_number, font=("arial", 15), bd=7, relief=SUNKEN).grid(
            row=0, column=11)

        c_room = Button(f4, command=self.change_room, width=11, bg="lightyellow", text="Change-room",
                        font=("times new roman", 18, "bold"),
                        bd=10, relief=SUNKEN).grid(row=0, column=12, padx=10)

        # ===========================Deit Detail===========================================================

        f3 = LabelFrame(self.root, text="Deit Detail", bd=7, bg=bg_color, fg="gold",
                        relief=GROOVE, font=("times new roman", 15, "bold"), pady=2)

        f3.place(x=0, y=340, relheight=1, relwidth=1)

        m_name = Label(f3, text="Month Name", font=("times new roman", 18, "bold"),
                       bg=bg_color, fg="white").grid(row=0, column=0, padx=10, pady=5)
        m_name_text = Entry(f3, width=10, textvariable=self.month_name, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=0, column=1)

        r_numbers = Label(f3, text="Room No.", font=("times new roman", 15, "bold"),
                          bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=15, pady=20, sticky="w")
        r_texts = Entry(f3, width=10, textvariable=self.room_no, font=("arial", 15), bd=7,
                        relief=SUNKEN).grid(row=1, column=1, padx=30, pady=15)

        ok = Button(f3, command=self.ok_get_detail, width=5, bg="lightyellow", text="Ok",
                    font=("times new roman", 18, "bold"),
                    bd=7, relief=SUNKEN).grid(row=1, column=2, padx=10)

        s_names = Label(f3, text="NAME", font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=20, pady=30, sticky="w")
        s_names_text = Entry(f3, width=13, textvariable=self.nam, font=("arial", 15), bd=7,
                             relief=SUNKEN).grid(row=2, column=1, padx=30, pady=30)

        s_branches = Label(f3, text="BRANCH", font=("times new roman", 15, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=20, pady=30, sticky="w")
        s_branch_texts = Entry(f3, width=13, textvariable=self.branc, font=("arial", 15), bd=7,
                               relief=SUNKEN).grid(row=3, column=1, padx=30, pady=30)

        ss_batch = Label(f3, text="BATCH", font=("times new roman", 15, "bold"),
                         bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=20, pady=20, sticky="w")
        ss_batch_text = Entry(f3, width=13, textvariable=self.bat, font=("arial", 15), bd=7,
                              relief=SUNKEN).grid(row=4, column=1, padx=30, pady=20)

        r_p_d = Label(f3, text="Rs per deit", font=("times new roman", 18, "bold"),
                      bg=bg_color, fg="white").grid(row=0, column=3, padx=10, pady=5)
        r_p_d_text = Entry(f3, width=5, textvariable=self.rs_per_diet, font=("arial", 15), bd=7, relief=SUNKEN).grid(
            row=0, column=4)

        sers = Label(f3, text="SERVICE TAX", font=("times new roman", 15, "bold"),
                     bg=bg_color, fg="lightgreen").grid(row=1, column=3, padx=20, pady=20, sticky="w")
        ser_text = Entry(f3, width=13, textvariable=self.ser, font=("arial", 15), bd=7,
                         relief=SUNKEN).grid(row=1, column=4, padx=30, pady=20)

        deit = Label(f3, text="DEIT", font=("times new roman", 15, "bold"),
                     bg=bg_color, fg="lightgreen").grid(row=2, column=3, padx=20, pady=20, sticky="w")
        deit_text = Entry(f3, width=13, textvariable=self.diet, font=("arial", 15), bd=7,
                          relief=SUNKEN).grid(row=2, column=4, padx=30, pady=20)

        extras = Label(f3, text="EXTRA", font=("times new roman", 15, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=3, column=3, padx=20, pady=20, sticky="w")
        extra_text = Entry(f3, width=13, textvariable=self.extra, font=("arial", 15), bd=7,
                           relief=SUNKEN).grid(row=3, column=4, padx=30, pady=20)

        adjustments = Label(f3, text="ADJUSTMENT", font=("times new roman", 15, "bold"),
                            bg=bg_color, fg="lightgreen").grid(row=4, column=3, padx=20, pady=20, sticky="w")
        adjustments_text = Entry(f3, width=13, textvariable=self.adjustment, font=("arial", 15), bd=7,
                                 relief=SUNKEN).grid(row=4, column=4, padx=30, pady=20)

        totaly = Button(f3, command=self.total_prize, width=10, bg="lightyellow", text="Total",
                        font=("times new roman", 18, "bold"),
                        bd=7, relief=SUNKEN).grid(row=0, column=5, padx=30)

        done = Button(f3, command=self.mess_bill_entry, width=10, bg="lightyellow", text="Done",
                      font=("times new roman", 18, "bold"),
                      bd=7, relief=SUNKEN).grid(row=1, column=5, padx=30)

        clear = Button(f3, command=self.clear_data, width=10, bg="lightyellow", text="Clear/New",
                       font=("times new roman", 18, "bold"),
                       bd=7, relief=SUNKEN).grid(row=2, column=5, padx=30)

        amounts = Label(f3, text="AMOUNT", font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="lightgreen").grid(row=0, column=6, padx=20, pady=20, sticky="w")
        amounts_text = Entry(f3, width=13, textvariable=self.amount, font=("arial", 15), bd=7,
                             relief=SUNKEN).grid(row=0, column=7, padx=30, pady=20)

        totals = Label(f3, text="TOTAL", font=("times new roman", 15, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=1, column=6, padx=20, pady=20, sticky="w")
        totals_text = Entry(f3, width=13, textvariable=self.total, font=("arial", 15), bd=7,
                            relief=SUNKEN).grid(row=1, column=7, padx=30, pady=20)

        t_b_pay = Label(f3, text="TO BE PAY", font=("times new roman", 15, "bold"),
                        bg=bg_color, fg="lightgreen").grid(row=2, column=6, padx=20, pady=20, sticky="w")
        t_b_pay_text = Entry(f3, width=13, textvariable=self.to_be_pay, font=("arial", 15), bd=7,
                             relief=SUNKEN).grid(row=2, column=7, padx=30, pady=20)

        receipts = Label(f3, text="RECEIPT", font=("times new roman", 15, "bold"),
                         bg=bg_color, fg="lightgreen").grid(row=3, column=6, padx=20, pady=20, sticky="w")
        receipts_text = Entry(f3, width=13, textvariable=self.receipt_nu, font=("arial", 15), bd=7,
                              relief=SUNKEN).grid(row=3, column=7, padx=30, pady=20)

        up_date = Button(f3, command=self.updating_bill, width=10, bg="lightyellow", text="UPDATE",
                         font=("times new roman", 18, "bold"),
                         bd=7, relief=SUNKEN).grid(row=4, column=7, padx=30)

    def total_prize(self):
        try:
            self.total_amount = float(self.rs_per_diet.get() * self.diet.get())

            self.total_cost = float(self.total_amount + self.ser.get() + self.extra.get())

            self.to_be_pay_cost = float(self.total_cost - self.adjustment.get())

            self.amount.set(self.total_amount)
            self.total.set(self.total_cost)
            self.to_be_pay.set(self.to_be_pay_cost)

        except:
            messagebox.showerror("Error", "something is wrong, Please check!!!")

    def clear_data(self):
        try:
            op = messagebox.askyesno("Clear/New", "Do you want to Clear/New?")
            if op > 0:
                self.room_no.set("")
                self.nam.set("")
                self.branc.set("")
                self.bat.set("")
                self.ser.set(0)
                self.diet.set(0)
                self.extra.set(0)
                self.adjustment.set(0)
                self.amount.set(0)
                self.total.set(0)
                self.to_be_pay.set(0)
                self.receipt_nu.set("")
        except:
            messagebox.showerror("Error", "something is wrong, Please check!!!")

    def add_students(self):
        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            try:
                # CREATE CURSOR
                cur = conn.cursor()
                uni_roll_number = self.uni_roll.get()
                rooms = self.room_number.get()
                s_names = self.name.get()
                m = str(uni_roll_number)
                if len(m) >= 7:

                    if len(s_names) and len(rooms) > 0:
                        branches = self.branch.get()
                        batches = self.batch.get()
                        insert = """INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s)"""
                        cur.execute(insert, [uni_roll_number, rooms, s_names, branches, batches])
                        conn.commit()

            except:
                messagebox.showerror("Error", "Something wrong, please check UNI ROLL NO. or ROOM NO."
                                              "(It may already added) ")
            else:

                cur.close()
                conn.close()
                if len(m) >= 7:
                    if len(s_names) and len(rooms) > 0:
                        messagebox.showinfo("Added", "Student Added!!")
                        self.uni_roll.set(0)
                        self.name.set('')
                        self.room_number.set('')
                        self.branch.set('')
                        self.batch.set('')

                    else:
                        messagebox.showerror("Error", "Name and Room no. must not empty !!")
                else:
                    messagebox.showerror("Error", "Uni-Roll must be 7 or moe than 7 digits !!")

    def remove_students(self):
        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            try:
                # CREATE CURSOR
                cur = conn.cursor()
                uni_roll_number = self.uni_roll.get()
                check = """select uni_roll from student where uni_roll = %s"""

                cur.execute(check, [uni_roll_number])
                r = cur.fetchone()
                if r is None:
                    messagebox.showerror("Error", "Something wrong, please check UNI. ROLL NO. ")
                else:
                    delete = """delete from student where uni_roll = %s"""
                    cur.execute(delete, [uni_roll_number])
                    conn.commit()
                    messagebox.showinfo("Removed", "Student Removed!!")
                    self.uni_roll.set(0)

            except:
                messagebox.showerror("Error", "Something wrong, please check UNI. ROLL NO. ")
            else:

                cur.close()
                conn.close()

    def change_room(self):

        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            try:
                # CREATE CURSOR
                cur = conn.cursor()
                uni_roll_number = self.uni_roll.get()
                new_room = self.new_room_number.get()
                if set(new_room).difference(ascii_letters + digits) or len(new_room) == 0:
                    messagebox.showerror("Error", "Room number can't be empty ans special character is not allowed !!")
                else:
                    check = """select uni_roll from student where uni_roll = %s"""

                    cur.execute(check, [uni_roll_number])
                    r = cur.fetchone()
                    if r is None:
                        messagebox.showerror("Error", "Something wrong, please check UNI. ROLL NO. ")
                    else:
                        change = """UPDATE STUDENT SET room_no =%s WHERE uni_roll=%s"""
                        cur.execute(change, [new_room, uni_roll_number])
                        conn.commit()
                        messagebox.showinfo("Updated", "Room number Updated!!")
                        self.uni_roll.set(0)
                        self.new_room_number.set('')


            except:
                messagebox.showerror("Error", "Something wrong, please check UNI. ROLL NO. or New room number("
                                              "it may room number is already in data base:)")
            else:

                cur.close()
                conn.close()

    def reset_all_room_no(self):

        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            # CREATE CURSOR
            cur = conn.cursor()
            messagebox.showwarning("Warning", "IT WILL RESET ALL ROOM NUMBERS ?? It must do in starting of the YEAR !")
            op = messagebox.askokcancel("SURE", "Are You Sure For Reset room numbers ??")
            if op:
                messagebox.showinfo("Time-Tkes", "It will Take Some Time !!")
                try:
                    delete = """ALTER TABLE student DROP COLUMN room_no,DROP INDEX room_no"""
                    cur.execute(delete)
                    conn.commit()
                except:
                    messagebox.showerror("Error", "Room number is NOT reset , please try again !!")
                try:

                    reset = """ALTER TABLE student 
                                    ADD COLUMN room_no VARCHAR(7) NULL unique DEFAULT NULL AFTER uni_roll"""
                    cur.execute(reset)
                    conn.commit()

                except:
                    messagebox.showerror("Error", "Room number is NOT reset , please try again !!")
                else:
                    messagebox.showinfo("RESET", "Room number is reset !! NEW ROOM NO.--> Enter one by one ")
                    cur.close()
                    conn.close()
            else:
                cur.close()
                conn.close()
                messagebox.showinfo("Canceled", "Reset canceled")

    def ok_get_detail(self):
        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            try:
                # CREATE CURSOR
                cur = conn.cursor()
                room = self.room_no.get()
                getting = """select name,branch,batch  from student where room_no = %s"""
                cur.execute(getting, [room])
                r = cur.fetchone()
                if r is None:
                    messagebox.showerror("Error", "No data is available !!")
                else:
                    t = 1
                    for i in r:
                        if t == 1:
                            self.nam.set(i)
                            t = t + 1
                        elif t == 2:
                            self.branc.set(i)
                            t = t + 1
                        elif t == 3:
                            self.bat.set(i)
            except:
                messagebox.showerror("Error", "Something wrong, please check ROOM NO. ")
            else:

                cur.close()
                conn.close()

    def create_month_table(self):
        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            try:
                # CREATE CURSOR
                cur = conn.cursor()
                table_nam = self.month_name.get()
                if set(table_nam).difference(ascii_letters + digits) or table_nam == " " or table_nam == "":
                    messagebox.showerror("Error", "Special character is no allowed !!")
                else:
                    op = messagebox.askyesno("Create", "Do you want to Create Table for new mess bill ??")
                    if op:
                        create = """CREATE TABLE {tab}(NAME VARCHAR(25) NOT NULL,ROOM_NO VARCHAR(7)NOT NULL,
                                    BRANCH VARCHAR(10)NULL,BATCH VARCHAR(6)NULL,SER FLOAT NULL,DIET INT NULL,
                                    EXTRA FLOAT NULL,
                                    AMOUNT FLOAT NULL,TOTAL FLOAT NOT NULL,ADJUSTMENT FLOAT NULL,
                                    TO_BE_PAY FLOAT NOT NULL,
                                    RECEIPTS VARCHAR(20)NULL,PRIMARY KEY(ROOM_NO),
                                    UNIQUE INDEX ROOM_NO_UNIQUE(ROOM_NO ASC) VISIBLE)""".format(tab=table_nam)
                        cur.execute(create)
                        conn.commit()
                        messagebox.showinfo("Created", "Yo !! Table is created !! ")
                    else:
                        messagebox.showinfo("Cancel", "Canceled")
            except:
                messagebox.showerror("Error", "Something wrong, Month Name is Already in Data base , Try new !!")
            else:

                cur.close()
                conn.close()

    def mess_bill_entry(self):
        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            try:

                # CREATE CURSOR
                cur = conn.cursor()
                if len(self.room_no.get()) > 0 and len(self.nam.get()) > 0:
                    if self.ser.get() > 0:
                        if self.to_be_pay.get() > 0:
                            insert = """INSERT INTO {tab} (`NAME`, `ROOM_NO`, `BRANCH`, `BATCH`, `SER`, `DIET`, `EXTRA`,
                             `AMOUNT`, `TOTAL`, `ADJUSTMENT`, `TO_BE_PAY`, `RECEIPTS`) VALUES (%s,%s,%s,%s,%s,%s,%s,
                             %s,%s,%s,%s,%s)""".format(tab=self.month_name.get())
                            cur.execute(insert, [self.nam.get(), self.room_no.get(), self.branc.get(),
                                                 self.bat.get(),
                                                 self.ser.get(), self.diet.get(), self.extra.get(),
                                                 self.amount.get(), self.total.get(), self.adjustment.get(),
                                                 self.to_be_pay.get(),
                                                 self.receipt_nu.get()])
                            conn.commit()
                            messagebox.showinfo("Bill Added", "Student's Bill Added !!")
                            updates = """UPDATE last_roll SET room_nu=%s"""
                            cur.execute(updates, [self.room_no.get()])
                            conn.commit()
                        else:
                            messagebox.showerror("Error", "First Click On Total Button !!")
                    else:
                        messagebox.showerror("Error", "Service Tax must not be 0")

                else:
                    messagebox.showerror("Error", "Room no. and Name can't be Empty")

            except:
                messagebox.showerror("Error", "Something wrong, Month Name is not available or Room Number is already"
                                              " added !!")
            else:

                cur.close()
                conn.close()

    def updating_bill(self):
        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            try:
                # CREATE CURSOR
                cur = conn.cursor()
                if len(self.room_no.get()) > 0 and len(self.nam.get()) > 0:
                    if self.ser.get() > 0:
                        updated = """UPDATE {tab} SET NAME = %s,BRANCH = %s,BATCH = %s,
                         SER= %s, DIET= %s, EXTRA= %s,AMOUNT= %s,TOTAL= %s,
                          ADJUSTMENT = %s,TO_BE_PAY = %s,RECEIPTS = %s WHERE (ROOM_NO = %s)
                          """.format(tab=self.month_name.get())
                        cur.execute(updated, [self.nam.get(), self.branc.get(),
                                              self.bat.get(),
                                              self.ser.get(), self.diet.get(), self.extra.get(),
                                              self.amount.get(), self.total.get(), self.adjustment.get(),
                                              self.to_be_pay.get(),
                                              self.receipt_nu.get(), self.room_no.get()])
                        conn.commit()
                        messagebox.showinfo("Updated", "Bill Updated")
                    else:
                        messagebox.showerror("Error", "Service Tax must not be 0")

                else:
                    messagebox.showerror("Error", "Room no. and Name can't be Empty")


            except:
                messagebox.showerror("Error", "Something wrong, Room Number or Month name is not available")

            else:

                cur.close()
                conn.close()

    def find_last_room(self):
        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            try:
                # CREATE CURSOR
                cur = conn.cursor()
                select = """SELECT room_nu from last_roll"""
                cur.execute(select)
                r = cur.fetchone()
                if r is None:
                    messagebox.showerror("Error", "No data is available !!")
                else:
                    for i in r:
                        self.last_room_nu.set(i)
            except:
                messagebox.showerror("Error", "Something wrong, You have not added Yet !!")

            else:

                cur.close()
                conn.close()

    def search_bill_sys(self):
        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "connection failed")
        else:
            # print(conn.get_server_info())
            try:
                # CREATE CURSOR
                cur = conn.cursor()
                if len(self.room_no.get()) > 0 and len(self.month_name.get()):
                    select = """SELECT * from {tab} where room_no = %s""".format(tab=self.month_name.get())
                    cur.execute(select, [self.room_no.get()])
                    r = cur.fetchone()
                    if r is None:
                        messagebox.showerror("Error", "No data is available !!")
                    else:
                        temp = 1
                        for i in r:
                            if temp == 1:
                                self.nam.set(i)
                                temp = temp + 1
                            elif temp == 2:
                                self.room_no.set(i)
                                temp = temp + 1
                            elif temp == 3:
                                self.branc.set(i)
                                temp = temp + 1
                            elif temp == 4:
                                self.bat.set(i)
                                temp = temp + 1
                            elif temp == 5:
                                self.ser.set(i)
                                temp = temp + 1
                            elif temp == 6:
                                self.diet.set(i)
                                temp = temp + 1
                            elif temp == 7:
                                self.extra.set(i)
                                temp = temp + 1
                            elif temp == 8:
                                self.amount.set(i)
                                temp = temp + 1
                            elif temp == 9:
                                self.total.set(i)
                                temp = temp + 1
                            elif temp == 10:
                                self.adjustment.set(i)
                                temp = temp + 1
                            elif temp == 11:
                                self.to_be_pay.set(i)
                                temp = temp + 1
                            elif temp == 12:
                                self.receipt_nu.set(i)
                                temp = temp + 1
                else:
                    messagebox.showerror("Error", "First Fill Room number and Month Name !!")

            except:
                messagebox.showerror("Error", "Something wrong, You have not added Yet !!")

            else:

                cur.close()
                conn.close()

    def export_bill(self):
        try:
            # connection
            conn = mysql.connector.connect(host='localhost',
                                           database='messdb',
                                           user='root',
                                           password='7277439880a')
        except:
            messagebox.showerror("Error", "Connection failed , Try Again !!")
        else:
            # print(conn.get_server_info())
            try:
                # CREATE CURSOR
                cur = conn.cursor()
                selection = """select * from {tab} order by room_no asc""".format(tab=self.month_name.get())
                df = pd.read_sql_query(selection, conn)

                df.to_excel(fr'save_bill/{self.month_name.get()}.xlsx', index=False)
                conn.commit()
                messagebox.showinfo("Excel", f"Bill saved in Save_bill Folder as {self.month_name.get()} !!")

            except:
                messagebox.showerror("Error", "No Data Available or Data is opened in EXCEL please CHECK !!!")
            else:

                cur.close()
                conn.close()


root = Tk()
obj = Bill_App(root)
root.mainloop()
