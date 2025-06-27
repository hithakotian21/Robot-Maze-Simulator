from tkinter import *

root = Tk()
root.title("Robot Simulation")
canvas = Canvas(root, width=400, height=400, bg='White')
canvas.pack()

# Create the rectangle and obstacles
rect = canvas.create_rectangle(10, 30, 30, 10, outline="White", fill='red')
obs1 = canvas.create_rectangle(0, 0, 5, 400, fill='black')
obs2 = canvas.create_rectangle(397, 0, 400, 400, fill='black')
obs3 = canvas.create_rectangle(0, 0, 400, 5, fill='black')
obs4 = canvas.create_rectangle(0, 397, 365, 400, fill='black')
obs5_0 = canvas.create_line(6, 35, 365, 35, fill='black')
obs5_1 = canvas.create_line(40, 65, 397, 65, fill='black')
obs5_2 = canvas.create_line(215, 95, 397, 95, fill='black')
obs5_3 = canvas.create_line(6, 95, 185, 95, fill='black')
obs5_4_1 = canvas.create_line(185, 95, 185, 225, fill='black')
obs5_4_2 = canvas.create_line(215, 95, 215, 225, fill='black')
obs5_5 = canvas.create_line(35, 225, 185, 225, fill='black')
obs5_6 = canvas.create_line(35, 125, 35, 225, fill='black')
obs5_7 = canvas.create_line(35, 125, 155, 125, fill='black')
obs5_8 = canvas.create_line(155, 125, 155, 195, fill='black')
obs5_9 = canvas.create_line(65, 195, 155, 195, fill='black')
obs5_10 = canvas.create_line(245, 125, 245, 225, fill='black')
obs5_11 = canvas.create_line(245, 125, 365, 125, fill='black')
obs5_12 = canvas.create_line(365, 125, 365, 400, fill='black')
obs5_13 = canvas.create_line(245, 225, 335, 225, fill='black')
obs5_14 = canvas.create_line(335, 155, 335, 225, fill='black')
obs5_15 = canvas.create_line(65, 155, 65, 195, fill='black')
obs5_16 = canvas.create_line(275, 155, 335, 155, fill='black')
obs5_17 = canvas.create_line(275, 155, 275, 195, fill='black')
obs6 = canvas.create_rectangle(35, 255, 335, 360, outline='black')
canvas.create_text(185, 307, text="RoboMove", font=("Arial", 14, "bold"), fill="black")
Label(root, text="Exit", bg='White').place(x=370, y=380)
#Label(root, text="RoboMove", bg='White').place(x=100, y=270)

# Define a function to check for collisions
def collides_with_obstacle(item):
    overlaps = canvas.find_overlapping(*canvas.bbox(item))
    for overlap in overlaps:
        if overlap in [obs1, obs2, obs3, obs4, obs5_0, obs5_1, obs5_2, obs5_3, obs5_4_1, obs5_4_2,
                       obs5_5, obs5_6, obs5_7, obs5_8, obs5_9, obs5_10, obs5_11, obs5_12, obs5_13,
                       obs6, obs5_14, obs5_15, obs5_16, obs5_17]:
            return True
    return False

# Define a function to move the rectangle
def move_rect(event):
    key = event.keysym
    x, y = 0, 0
    if key == 'Up':
        y = -10
    elif key == 'Down':
        y = 10
    elif key == 'Left':
        x = -10
    elif key == 'Right':
        x = 10

    canvas.move(rect, x, y)
    if collides_with_obstacle(rect):
        canvas.move(rect, -x, -y)

# Bind the arrow keys
canvas.bind_all('<Key>', move_rect)

# Run the Tkinter app
root.mainloop()
