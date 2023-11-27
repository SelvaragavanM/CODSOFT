import tkinter as tk
from tkinter import messagebox

tasks = []

def adding_task():
    taskname = entry_task.get()
    if taskname:
        tasks.append(taskname)
        update_listbox_taskbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Field can't be Empty")

def deleting_task():
    clicked_task = listbox_textbox.curselection()
    if clicked_task:
        tasks.pop(clicked_task[0])
        update_listbox_taskbox()
    else:
        messagebox.showinfo("Error", "No Task is Selected")

def clear_the_list():
    tasks.clear()
    update_listbox_taskbox()

def close():
    if messagebox.askokcancel("Exit", "Close the app?"):
        guiWindow.destroy()

def update_listbox_taskbox():
    listbox_textbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        listbox_textbox.insert(tk.END, f"{i}. {task}")

def main():
    global entry_task, listbox_textbox, guiWindow
    guiWindow = tk.Tk()
    guiWindow.title("To-Do-List Application")

    entry_task = tk.Entry(guiWindow, width=60)
    entry_task.pack(pady=15)

    guiWindow.geometry("1000x550+280+280")
    guiWindow.resizable(0, 0)

    listbox_textbox = tk.Listbox(guiWindow, selectmode=tk.SINGLE, width=50, height=15)
    listbox_textbox.pack()

    button_frame = tk.Frame(guiWindow)
    button_frame.pack(pady=15)

    add_button = tk.Button(button_frame, text="Add any task", command=adding_task, bg="#7b68ee")
    add_button.grid(row=0, column=0, padx=5)

    delete_button = tk.Button(button_frame, text="Delete the task", command=deleting_task, bg="#ff1493")
    delete_button.grid(row=0, column=1, padx=5)

    clear_button = tk.Button(button_frame, text="Clear the task", command=clear_the_list, bg="#ffa07a")
    clear_button.grid(row=0, column=2, padx=5)

    exit_button = tk.Button(button_frame, text="Exit from app", command=close, bg="#ffa500")
    exit_button.grid(row=0, column=3, padx=5)

    update_listbox_taskbox()

    guiWindow.mainloop()

if __name__ == "__main__":
    main()


