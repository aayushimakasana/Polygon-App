import tkinter as tk
from tkinter import messagebox, simpledialog
import math

def draw_triangle(canvas, angles):
    canvas.delete("all")

    # Ensure angles sum to 180 degrees
    if sum(angles) != 180:
        messagebox.showerror("Error", "The angles do not sum to 180 degrees.")
        return

    # Convert angles to radians
    angles_rad = [math.radians(a) for a in angles]

    # Setup constants
    center_x, center_y = 200, 150
    side_length = 100

    # Calculate the vertices of the triangle
    x0, y0 = center_x, center_y
    x1 = x0 + side_length
    y1 = y0

    angle2 = math.radians(angles[1])
    angle3 = math.radians(angles[2])

    # Calculate x2, y2 using angle2
    x2 = x0 + side_length * math.cos(angle2)
    y2 = y0 - side_length * math.sin(angle2)

    # Calculate x3, y3 using angle3
    x3 = x1 + side_length * math.cos(math.pi - angle3)
    y3 = y1 - side_length * math.sin(math.pi - angle3)

    # Draw the triangle
    canvas.create_line(x0, y0, x1, y1, fill="black")
    canvas.create_line(x1, y1, x2, y2, fill="black")
    canvas.create_line(x2, y2, x0, y0, fill="black")

    # Label the angles
    canvas.create_text(x0, y0, text=f"{angles[0]}°", fill="red", font=("Arial", 12))
    canvas.create_text(x1, y1, text=f"{angles[1]}°", fill="red", font=("Arial", 12))
    canvas.create_text(x2, y2, text=f"{angles[2]}°", fill="red", font=("Arial", 12))


def draw_quadrilateral(canvas, angles):
    canvas.delete("all")

    # Ensure angles sum to 360 degrees
    if sum(angles) != 360:
        messagebox.showerror("Error", "The angles do not sum to 360 degrees.")
        return

    # Convert angles to radians
    angles_rad = [math.radians(a) for a in angles]

    # Setup constants
    center_x, center_y = 200, 150
    side_length = 100

    # Calculate the vertices of the quadrilateral
    coords = [(center_x, center_y)]
    angle_sum = 0

    for angle in angles_rad:
        angle_sum += angle
        x = coords[-1][0] + side_length * math.cos(angle_sum)
        y = coords[-1][1] + side_length * math.sin(angle_sum)
        coords.append((x, y))

    # Draw the quadrilateral
    for i in range(4):
        canvas.create_line(coords[i][0], coords[i][1], coords[(i + 1) % 4][0], coords[(i + 1) % 4][1], fill="black")

    # Label the angles
    for i, (x, y) in enumerate(coords):
        canvas.create_text(x, y, text=f"{angles[i]}°", fill="red", font=("Arial", 12))


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
            draw_triangle(canvas, [angle1, angle2, angle3])
    except ValueError:
        messagebox.showerror("Error", "Please enter valid positive integers for angles.")


def calculate_quadrilateral_angle(canvas, result_label):
    try:
        angle1 = int(simpledialog.askstring("Input", "Enter the first angle:"))
        angle2 = int(simpledialog.askstring("Input", "Enter the second angle:"))
        angle3 = int(simpledialog.askstring("Input", "Enter the third angle:"))

        if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
            raise ValueError

        if angle1 + angle2 + angle3 >= 360:
            messagebox.showerror("Error", "The sum of three angles must be less than 360 degrees.")
        else:
            angle4 = 360 - (angle1 + angle2 + angle3)
            result_label.config(text=f"The fourth angle is {angle4} degrees.")
            draw_quadrilateral(canvas, [angle1, angle2, angle3, angle4])
    except ValueError:
        messagebox.showerror("Error", "Please enter valid positive integers for angles.")


def main_window():
    window = tk.Tk()
    window.title("Polygon Angle Calculator")

    window.configure(bg='lightblue')

    tk.Label(window, text="Polygon Angle Calculator", font=("Arial", 16, "bold"), bg='lightblue').pack(pady=10)

    canvas = tk.Canvas(window, width=400, height=300, bg='white')
    canvas.pack(pady=10)

    result_label = tk.Label(window, text="", font=("Arial", 14), bg='lightblue')
    result_label.pack(pady=10)

    tk.Button(window, text="Triangle", command=lambda: calculate_triangle_angle(canvas, result_label),
              font=("Arial", 12), bg='lightgreen').pack(pady=5)
    tk.Button(window, text="Quadrilateral", command=lambda: calculate_quadrilateral_angle(canvas, result_label),
              font=("Arial", 12),
              bg='lightcoral').pack(pady=5)
    tk.Button(window, text="Exit", command=window.quit, font=("Arial", 12), bg='salmon').pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main_window()