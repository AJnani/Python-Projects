import tkinter as tk
from tkinter import messagebox
import os

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        # Initialize tasks
        self.tasks = []
        self.load_tasks()

        # Create UI elements
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Due date entry
        self.due_date_entry = tk.Entry(master, width=25)
        self.due_date_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        self.due_date_label = tk.Label(master, text="Due Date (DD-MM-YYYY):")
        self.due_date_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        # Priority dropdown
        self.priority_var = tk.StringVar(master)
        self.priority_var.set("Priority")
        self.priority_dropdown = tk.OptionMenu(master, self.priority_var, "Low", "Medium", "High")
        self.priority_dropdown.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        
        # Task listbox
        self.task_listbox = tk.Listbox(master, width=50, height=20)
        self.task_listbox.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
        
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=4, column=0, padx=5, pady=5)
        
        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.grid(row=4, column=1, padx=5, pady=5)
        
        # Populate task listbox
        self.update_task_listbox()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            priority = self.priority_var.get()
            due_date = self.due_date_entry.get()
            self.tasks.append({"text": task_text, "completed": False, "priority": priority, "due_date": due_date})
            self.save_tasks()
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Task cannot be empty!")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.save_tasks()
            self.update_task_listbox()
        else:
            messagebox.showerror("Error", "No task selected!")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task["completed"] = True
            self.save_tasks()
            self.update_task_listbox()
        else:
            messagebox.showerror("Error", "No task selected!")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            text = "[✓] " if task["completed"] else "[ ] "
            text += f"{task['text']} - Priority: {task['priority']}, Due Date: {task['due_date']}"
            self.task_listbox.insert(tk.END, text)

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    task_data = line.strip().split("|")
                    self.tasks.append({
                        "text": task_data[0],
                        "completed": bool(task_data[1]),
                        "priority": task_data[2],
                        "due_date": task_data[3]
                    })

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['text']}|{task['completed']}|{task['priority']}|{task['due_date']}\n")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
