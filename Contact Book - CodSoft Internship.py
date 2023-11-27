import sqlite3
from tkinter import *
from tkinter import ttk, messagebox,simpledialog 

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.attributes('-fullscreen', True)

        self.create_widgets()

        self.firstname = StringVar()
        self.lastname = StringVar()
        self.mobile = StringVar()
        self.addr = StringVar()
        self.pin = StringVar()

        self.create_contact_details_frame()
        self.create_record_frame()
        self.create_buttons_frame()

        self.fetch_data()

    def create_widgets(self):
        title = Label(self.root, text="Contact Book", font=("Comic Sans MS", 20), bd=8, bg='black', fg='white')
        title.pack(side=TOP, fill=X)

    def create_contact_details_frame(self):
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        detail_frame.place(x=10, y=120, width=350, height=260)

        entries = [
            ("First Name", self.firstname),
            ("Last Name", self.lastname),
            ("Mobile No.", self.mobile),
            ("Address", self.addr),
            ("PinCode", self.pin)
        ]

        for i, (label_text, variable) in enumerate(entries):
            Label(detail_frame, text=label_text, font=("Comic Sans MS", 12)).grid(row=i + 1, column=0, pady=10, padx=20,
                                                                                  sticky="w")
            Entry(detail_frame, font=("Comic Sans MS", 10), bd=3, textvariable=variable).grid(row=i + 1, column=1,
                                                                                                pady=10, sticky="w")

    def create_record_frame(self):
        record_frame = Frame(self.root, bd=5, relief=RIDGE)
        record_frame.place(x=400, y=120, width=500, height=260)

        yscroll = Scrollbar(record_frame, orient=VERTICAL)
        self.contact_table = ttk.Treeview(record_frame, columns=("firstname", "lastname", "mobile", "address", "pin"),
                                          yscrollcommand=yscroll.set)
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.contact_table.yview)

        headings = ["","First Name","Last Name", "Mobile No.", "Address", "PinCode"]
        for i, heading in enumerate(headings):
            col_id = f"#{i}"
            self.contact_table.heading(col_id,text=heading)

            self.contact_table.column(col_id, width=80 if i != len(headings) - 1 else 90)


        self.contact_table['show'] = 'headings'
        self.contact_table.pack(fill=BOTH, expand=1)
        self.contact_table.bind("<ButtonRelease-1>", self.get_cursor)
        

    def create_buttons_frame(self):
        btn_frame = Frame(self.root, bd=5, relief=RIDGE)
        btn_frame.place(x=250, y=400, width=600, height=60)

        buttons = [
            ("Add record", self.add_record),
            ("View", self.view_contacts),
            ("Search", self.search_contact),
            ("Update", self.update_record),
            ("Delete", self.delete_record),
        ]

        for i, (btn_text, command) in enumerate(buttons):
            Button(btn_frame, text=btn_text, font='arial 12 bold', bg='black', fg='white', width=9, command=command).grid(
                row=0, column=i, padx=8, pady=10)

    def add_record(self):
        if any([value.get() == '' for value in (self.firstname, self.lastname, self.mobile, self.addr, self.pin)]):
            messagebox.showerror('Error', 'Please enter all details')
        else:
            if self.check_duplicate():
                messagebox.showerror('Error', 'Duplicates not allowed')
            else:
                self.insert_record()

    def view_contacts(self):
        con = sqlite3.connect('contactbook.db')
        cur = con.cursor()
        cur.execute("SELECT firstname, lastname, mobile, addr, pin FROM contact")
        rows = cur.fetchall()
        con.close()
        self.update_contact_table(rows)

    def search_contact(self):
        name = simpledialog.askstring("Search Contact", "Enter the first name to search:")
        if name:
            con = sqlite3.connect('contactbook.db')
            cur = con.cursor()
            cur.execute("SELECT firstname, lastname, mobile, addr, pin FROM contact WHERE firstname=?", (name,))
            rows = cur.fetchall()
            con.close()
            self.update_contact_table(rows)
        else:
            messagebox.showinfo("Info", "Search canceled. Please enter a first name.")     

    def update_record(self):
        if self.mobile.get() == '':
            messagebox.showerror('Error', 'Mobile number is required to update a record')
        else:
            con = sqlite3.connect('contactbook.db')
            cur = con.cursor()
            cur.execute("UPDATE contact SET firstname=?, lastname=?, mobile=?, addr=?, pin=? WHERE mobile=?", (
                self.firstname.get(),
                self.lastname.get(),
                self.mobile.get(),
                self.addr.get(),
                self.pin.get(),
                self.mobile.get()
            ))
            messagebox.showinfo('Info', f'Record {self.mobile.get()} has been updated successfully')
            con.commit()
            con.close()
            self.fetch_data()
            self.reset_fields()

    def delete_record(self):
        if self.mobile.get() == '':
            messagebox.showerror('Error', 'Enter mobile number to delete the record')
        else:
            con = sqlite3.connect('contactbook.db')
            cur = con.cursor()
            cur.execute("DELETE FROM contact WHERE mobile=?", (self.mobile.get(),))
            con.commit()
            con.close()
            self.fetch_data()
            self.reset_fields()


    def get_cursor(self, ev):
        cursor_row = self.contact_table.focus()
        content = self.contact_table.item(cursor_row)
        row = content['values']
        self.firstname.set(row[0])
        self.lastname.set(row[1])
        self.mobile.set(row[2])
        self.addr.set(row[3])
        self.pin.set(row[4])

    def fetch_data(self):
        con = sqlite3.connect('contactbook.db')
        cur = con.cursor()
        cur.execute("SELECT firstname, lastname, mobile, addr, pin FROM contact")
        rows = cur.fetchall()
        self.update_contact_table(rows)
        con.close()

        updated_rows = [(f"{row[0]} {row[1]}", *row[2:]) for row in rows]

        self.update_contact_table(updated_rows)

    def update_contact_table(self, rows):
        self.contact_table.delete(*self.contact_table.get_children())
        for row in rows:
            self.contact_table.insert('', END, values=row)

    def check_duplicate(self):
        con = sqlite3.connect('contactbook.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM contact WHERE mobile=?", (self.mobile.get(),))
        duplicate = cur.fetchone() is not None
        con.close()
        return duplicate

    def insert_record(self):
        con = sqlite3.connect('contactbook.db')
        cur = con.cursor()

        try:
            cur.execute("INSERT INTO contact VALUES (?, ?, ?, ?, ?)", (
                self.firstname.get(),
                self.lastname.get(),
                self.mobile.get(),
                self.addr.get(),
                self.pin.get(),
            ))
            con.commit()
            messagebox.showinfo('Info', 'Record has been inserted successfully')
            self.reset_fields()
        except sqlite3.IntegrityError:
            messagebox.showerror('Error', 'Duplicate mobile number. Record not inserted.')
        con.close()

if __name__ == "__main__":
    root = Tk()
    obj = ContactManager(root)
    root.mainloop()