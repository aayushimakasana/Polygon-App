import tkinter as tk
from tkinter import simpledialog,messagebox
import math


def draw_triangle(canvas, origin, length, angle1,angle2):
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
    canvas.create_text(origin[0]+ 15, origin[1] - 10, text=f'{angle1}°', fill='black')

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
                draw_triangle(canvas, origin, length, 90, angle2)
            else:
                origin = (150, 150)
                length = 100
                draw_triangle(canvas, origin, length, angle1, angle2)
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

def main_window():
    window = tk.Tk()
    canvas = tk.Canvas(window, width=400, height=400, bg='white')
    canvas.pack()
    window.title("Polygon Angle Calculator")
    window.configure(bg='lightblue')
    result_label = tk.Label(window, text="", font=("Arial", 14), bg='lightblue')
    result_label.pack(pady=10)
    tk.Label(window, text="Polygon Angle Calculator", font=("Arial", 16, "bold"), bg='lightblue').pack(pady=10)

    tk.Button(window, text="Triangle", command=lambda: calculate_triangle_angle(canvas, result_label),
              font=("Arial", 12), bg='lightgreen').pack(pady=5)
    tk.Button(window, text="Quadrilateral", command=lambda: calculate_quadrilateral_angle(canvas, result_label),
              font=("Arial", 12),
              bg='lightcoral').pack(pady=5)
    tk.Button(window, text="Exit", command=window.quit, font=("Arial", 12), bg='salmon').pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main_window()