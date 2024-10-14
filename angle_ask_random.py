## Triangle drawn by one angle measure 

import tkinter as tk
from tkinter import simpledialog
import math


def draw_angle(canvas, origin, length, angle):
    # Draw the horizontal line (0 degrees)
    canvas.create_line(origin[0], origin[1], origin[0] + length, origin[1], fill="blue")

    # Draw the angled line (60 degrees)
    angle_rad = math.radians(angle)  # Convert degrees to radians
    x3 = origin[0] + length * math.cos(angle_rad)
    y3 = origin[1] - length * math.sin(angle_rad)
    canvas.create_line(origin[0], origin[1], x3, y3, fill="blue")
    #triangle complete
    #canvas.create_line(origin[0] + length, origin[1],x3, y3,fill="blue")
    canvas.create_line(x3, y3,origin[0] + length, origin[1], fill="blue")
    # Label the angle
    canvas.create_text(origin[0]+ 15, origin[1] - 10, text=f'{angle}°', fill='black')


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()
angle1=int(simpledialog.askstring("Angle","Angle 1 input"))
angle2=int(simpledialog.askstring("Angle","Angle 2 input"))
if angle1 <= 0 or angle2 <= 0 :
    raise ValueError
elif angle2 + angle1 >= 180 :
    raise  ValueError
else:
    angle3 = 180-(angle1+angle2)
    tk.Label(root, text=f"The third angle is {angle3}degrees", font=("Arial", 16, "bold"), bg='lightblue').pack(pady=10)

origin = (200, 200)
length = 100
draw_angle(canvas, origin, length, angle1)

root.mainloop()

