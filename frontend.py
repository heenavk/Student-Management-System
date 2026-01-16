from tkinter import *
from tkinter import ttk
from backend import view_students, add_student, delete_student

root = Tk()
root.title("Student Management System")
root.geometry("500x400")

# Labels
Label(root, text="Roll Number").grid(row=0, column=0, padx=10, pady=5)
Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
Label(root, text="Marks").grid(row=2, column=0, padx=10, pady=5)

# Variables
roll_var = StringVar()
name_var = StringVar()
marks_var = StringVar()

# Entry Fields
Entry(root, textvariable=roll_var).grid(row=0, column=1)
Entry(root, textvariable=name_var).grid(row=1, column=1)
Entry(root, textvariable=marks_var).grid(row=2, column=1)

tree = ttk.Treeview(root, columns=("Roll", "Name", "Marks", "Grade"), show="headings")
tree.heading("Roll", text="Roll No")
tree.heading("Name", text="Name")
tree.heading("Marks", text="Marks")
tree.heading("Grade", text="Grade")

tree.column("Roll", width=80)
tree.column("Name", width=150)
tree.column("Marks", width=80)
tree.column("Grade", width=80)

tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


# Functions
def add():
    add_student(int(roll_var.get()), name_var.get(), int(marks_var.get()))
    view()


def view():
    for row in tree.get_children():
        tree.delete(row)

    for student in view_students():
        tree.insert("", "end", values=student)


def delete():
    delete_student(int(roll_var.get()))
    view()


# Buttons
Button(root, text="Add Student", width=20, command=add).grid(row=3, column=0, pady=5)
Button(root, text="View Students", width=20, command=view).grid(row=3, column=1, pady=5)
Button(root, text="Delete Student", width=20, command=delete).grid(row=4, column=0, pady=5)

root.mainloop()
