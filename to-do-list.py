import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.resizable(False, False)

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        if not task.startswith("✔ "):
            tasks[index] = "✔ " + task
            listbox.delete(index)
            listbox.insert(index, tasks[index])
        else:
            messagebox.showinfo("Info", "Task already marked as done.")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

def edit_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        current_task = tasks[index]
        new_task = simpledialog.askstring("Edit Task", "Update your task:", initialvalue=current_task)
        if new_task:
            tasks[index] = new_task
            listbox.delete(index)
            listbox.insert(index, new_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=20, fill='x')

add_button = tk.Button(root, text="Add Task", command=add_task, width=15)
add_button.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12), height=15, selectbackground="skyblue")
listbox.pack(pady=10, padx=20, fill='both', expand=True)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

edit_button = tk.Button(button_frame, text="Edit Task", command=edit_task, width=12)
edit_button.grid(row=0, column=0, padx=5)

done_button = tk.Button(button_frame, text="Mark as Done", command=mark_done, width=12)
done_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=12)
delete_button.grid(row=0, column=2, padx=5)

root.mainloop()
