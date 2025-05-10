import tkinter as tk
from tkinter import messagebox


from users_3 import User
from projects import Projects


root = tk.Tk()
root.title("TOGETHER Crowdfunding App")
root.geometry("400x300")


def register():
    try:
        User.Registration()
        messagebox.showinfo("Success", "Registration completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def login():
    try:
        User.login()
        messagebox.showinfo("Success", "Login successful!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_project():
    try:
        Projects.create()
        messagebox.showinfo("Success", "Project created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def donate():
    try:
        Projects.donate()
        messagebox.showinfo("Success", "Donation successful!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def logout():
    try:
        User.logout()
        messagebox.showinfo("Goodbye", "Logged out successfully!")
        root.quit()
    except Exception as e:
        messagebox.showerror("Error", str(e))


tk.Label(root, text="Welcome to TOGETHER Crowdfunding App :)", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Register", command=register, width=20, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Login", command=login, width=20, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Create New Project", command=create_project, width=20, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Donate", command=donate, width=20, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Logout", command=logout, width=20, bg="red", fg="white").pack(pady=20)


root.mainloop()