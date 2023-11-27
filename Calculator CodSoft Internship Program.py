import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title("Calculator")
frame = tk.Frame(master=window, bg="#000000", padx=40)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN,borderwidth=3, width=47)
entry.grid(row=0, column=0, columnspan=8, ipady=5, pady=3)

def myclick(number):
        entry.insert(tk.END, str(number))

def clear_entry():
    current_entry = entry.get()
    if current_entry:
        new_entry = current_entry[:-1]  
        entry.delete(0, tk.END)
        entry.insert(0, new_entry)
   
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=5)
button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=5)
button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=5)
button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=5)
button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=5)
button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=5)
button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=5)
button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=5)
button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=5)
button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=0, pady=5)
button_00 = tk.Button(master=frame, text='00', padx=15, pady=5, width=3, command=lambda: myclick('00'))
button_00.grid(row=4, column=1,pady=5)
button_point = tk.Button(master=frame, text='.', padx=15, pady=5, width=3, command=lambda: myclick('.'),bg='#e0115f')
button_point.grid(row=4,column=2,pady=5)
button_clear_entry = tk.Button(master=frame, text="CE", padx=15, pady=5, width=3, command=clear_entry, bg='#29c5f6')
button_clear_entry.grid(row=1, column=4, pady=5)
button_clear = tk.Button(master=frame, text="clear", padx=15, pady=5, width=3, command=clear,bg='#ff0000')
button_clear.grid(row=1, column=5,columnspan=3,pady=5)
button_multiply = tk.Button(master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'),bg='#ffb81c')
button_multiply.grid(row=2, column=4,pady=5)
button_div = tk.Button(master=frame, text="/", padx=15, pady=5,width=3, command=lambda: myclick('/'),bg='#ffb81c')
button_div.grid(row=2, column=5,columnspan=3,pady=5)
button_add = tk.Button(master=frame, text="+", padx=15, pady=5, height=4, command=lambda: myclick('+'),bg='#ffb81c')
button_add.grid(row=3, column=4, rowspan=5, pady=5)
button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'),bg='#ffb81c')
button_subtract.grid(row=3, column=5,columnspan=3,pady=5)
button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=3, command=equal,bg='#008000')
button_equal.grid(row=4, column=5, rowspan=5,pady=5)

window.mainloop()
