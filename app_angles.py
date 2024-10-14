import tkinter as tk
from tkinter import messagebox, simpledialog
import math


# Function to calculate the third angle of a triangle
def calculate_triangle_angle():
    try:
        angle1 = int(simpledialog.askstring("Input", "Enter the first angle:"))
        angle2 = int(simpledialog.askstring("Input", "Enter the second angle:"))

        if angle1 <= 0 or angle2 <= 0:
            raise ValueError

        if angle1 + angle2 >= 180:
            messagebox.showerror("Error", "Invalid input! The sum of two angles must be less than 180.")
        else:
            angle3 = 180 - (angle1 + angle2)
            messagebox.showinfo("Result", f"The third angle is {angle3} degrees.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid positive integers for angles.")


# Function to calculate the fourth angle of a quadrilateral
def calculate_quadrilateral_angle():
    try:
        angle1 = int(simpledialog.askstring("Input", "Enter the first angle:"))
        angle2 = int(simpledialog.askstring("Input", "Enter the second angle:"))
        angle3 = int(simpledialog.askstring("Input", "Enter the third angle:"))

        if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
            raise ValueError

        if angle1 + angle2 + angle3 >= 360:
            messagebox.showerror("Error", "Invalid input! The sum of three angles must be less than 360.")
        else:
            angle4 = 360 - (angle1 + angle2 + angle3)
            messagebox.showinfo("Result", f"The fourth angle is {angle4} degrees.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid positive integers for angles.")


# Main window for selecting the polygon
def main_window():
    window = tk.Tk()
    window.title("Polygon Angle Calculator")

    # Use a built-in image or simple background color instead
    window.configure(bg='lightblue')

    tk.Label(window, text="Polygon Angle Calculator", font=("Arial", 16, "bold"), bg='lightblue').pack(pady=10)

    tk.Button(window, text="Triangle", command=open_triangle_window, font=("Arial", 12), bg='lightgreen').pack(pady=5)
    tk.Button(window, text="Quadrilateral", command=open_quadrilateral_window, font=("Arial", 12),
              bg='lightcoral').pack(pady=5)
    tk.Button(window, text="Exit", command=window.quit, font=("Arial", 12), bg='salmon').pack(pady=10)

    window.mainloop()


# Function to open triangle angle input window
def open_triangle_window():
    calculate_triangle_angle()


# Function to open quadrilateral angle input window
def open_quadrilateral_window():
    calculate_quadrilateral_angle()


# Run the application
if __name__ == "__main__":
    main_window()