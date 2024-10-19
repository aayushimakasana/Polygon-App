import tkinter as tk
from tkinter import simpledialog, messagebox
import math
import os
import datetime

USER_DATA_FILE = 'user_data.txt'
LOGIN_DATA_FILE = 'login_data.txt'

def draw_triangle(canvas, origin, length, angle1,angle2,angle3):
    # Draw the horizontal line (0 degrees)
    canvas.delete("all")
    canvas.create_line(origin[0], origin[1], origin[0] + length, origin[1], fill="blue")

    # Draw the angled line (60 degrees)
    angle_rad = math.radians(angle1)  # Convert degrees to radians
    x3 = origin[0] + length * math.cos(angle_rad)
    y3 = origin[1] - length * math.sin(angle_rad)
    canvas.create_line(origin[0], origin[1], x3, y3, fill="blue")
    angle_rad1 = math.radians(angle2)
    hypo1 = math.hypot(length,length)
    canvas.create_line(origin[0] + length, origin[1],x3,y3, fill="blue")
    # Label the angle
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        canvas.create_text(origin[0],origin[1], text=f'{angle3}°', fill='black')
    else:
        canvas.create_text(x3,y3, text=f'{angle3}°', fill='black')


def calculate_triangle_angle(canvas, result_label):
    try:
        angle1 = int(simpledialog.askstring("Input", "Enter the first angle:"))
        angle2 = int(simpledialog.askstring("Input", "Enter the second angle:"))

        if angle1 <= 0 or angle2 <= 0:
            raise ValueError

        if angle1 + angle2 >= 180:
            messagebox.showerror("Error", "The sum of two angles must be less than 180 degrees.")
        else:
            angle3 = 180 - (angle1 + angle2)
            result_label.config(text=f"The third angle is {angle3} degrees.")
            #draw_triangle(canvas, [angle1, angle2, angle3])
            if angle1==90 or angle2==90 or angle3 ==90 :
                origin = (150, 150)
                length = 100
                draw_triangle(canvas, origin, length, 90, angle2,90)
            else:
                origin = (150, 150)
                length = 100
                draw_triangle(canvas, origin, length, angle1, angle2,angle3)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid positive integers for angles.")

def draw_quadrilateral(canvas,origin,length,angle1,angle2):
    # Draw the horizontal line (0 degrees)
    canvas.delete("all")
    canvas.create_line(origin[0], origin[1], origin[0] + length, origin[1], fill="blue")

    # Draw the angled line (60 degrees)
    angle_rad = math.radians(angle1)  # Convert degrees to radians
    x3 = origin[0] + length * math.cos(angle_rad)
    y3 = origin[1] - length * math.sin(angle_rad)
    canvas.create_line(origin[0], origin[1], x3, y3, fill="blue")
    angle_rad1 =math.radians(angle2)
    x4 = origin[0] + length + length*math.cos(angle_rad1)
    y4 = origin[1] - length * math.sin(angle_rad1)
    canvas.create_line(origin[0]+length,origin[1],x4,y4,fill="blue")
    canvas.create_line(x3,y3,x4,y4,fill="blue")

    # Label the angle
    canvas.create_text(origin[0] + 15, origin[1] - 10, text=f'{angle1}°', fill='black')

def calculate_quadrilateral_angle(canvas, result_label):
    try:
        angle1 = int(simpledialog.askstring("Input", "Enter the first angle:"))
        angle2 = int(simpledialog.askstring("Input", "Enter the second angle:"))
        angle3 = int(simpledialog.askstring("Input", "Enter the third angle:"))

        if angle1 <= 0 or angle2 <= 0 or angle3 <= 0 or angle1 >= 180 or angle2>=180 or angle3>=180:
            raise ValueError

        if angle1 + angle2 + angle3 >= 360:
            messagebox.showerror("Error", "The sum of three angles must be less than 360 degrees.")
        else:
            angle4 = 360 - (angle1 + angle2 + angle3)
            result_label.config(text=f"The fourth angle is {angle4} degrees.")
            origin = 150,150
            length = 100
            draw_quadrilateral(canvas,origin,length,angle1,angle2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid positive integers for angles.")

def log_login_attempt(username):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGIN_DATA_FILE, 'a') as file:
        file.write(f"{username},{timestamp}\n")

def main_window():
    for widget in root.winfo_children():
        widget.destroy()  # Remove all widgets from the root window

    canvas = tk.Canvas(root, width=400, height=400, bg='white')
    canvas.pack()
    root.title("Polygon Angle Calculator")
    result_label = tk.Label(root, text="", font=("Arial", 14), bg='lightblue')
    result_label.pack(pady=10)
    tk.Label(root, text="Polygon Angle Calculator", font=("Arial", 16, "bold"), bg='lightblue').pack(pady=10)

    tk.Button(root, text="Triangle", command=lambda: calculate_triangle_angle(canvas, result_label),
              font=("Arial", 12), bg='lightgreen').pack(pady=5)
    tk.Button(root, text="Quadrilateral", command=lambda: calculate_quadrilateral_angle(canvas, result_label),
              font=("Arial", 12),
              bg='lightcoral').pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg='salmon').pack(pady=10)


def save_user_data(username, email, password):
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username},{email},{password}\n")


def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    users = {}
    with open(USER_DATA_FILE, 'r') as file:
        for line in file:
            username, email, password = line.strip().split(',')
            users[username] = (email, password)
    return users


def sign_up():
    username = simpledialog.askstring("Sign Up", "Enter username:")
    email = simpledialog.askstring("Sign Up", "Enter email:")
    password = simpledialog.askstring("Sign Up", "Enter password:", show='*')

    if username and email and password:
        save_user_data(username, email, password)
        messagebox.showinfo("Success", "Sign up successful! You can now log in.")
        login_window()
    else:
        messagebox.showerror("Error", "Please fill all fields.")


def login_window():
    username = simpledialog.askstring("Login", "Enter Username or Email:")
    password = simpledialog.askstring("Login", "Enter Password:", show='*')

    users = load_user_data()
    if username in users and users[username][1] == password:
        log_login_attempt(username)
        messagebox.showinfo("Success", "Login successful!")
        main_window()
    else:
        messagebox.showerror("Error", "Invalid username/email or password.")


# Start Screen
root = tk.Tk()
root.configure(bg='lightblue')
root.title("Welcome")

tk.Label(root, text="Polygon Angle Calculator", font=("Arial", 20), bg='lightblue').pack(pady=20)
tk.Button(root, text="Log In", command=login_window, font=("Arial", 12), bg='lightgreen').pack(pady=10)
tk.Button(root, text="Sign Up", command=sign_up, font=("Arial", 12), bg='lightcoral').pack(pady=10)

root.mainloop()