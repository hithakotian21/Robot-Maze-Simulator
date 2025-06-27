# 🤖 Robo-Maze Simulator

A simple robot maze simulation built using **Python Tkinter**, designed to visualize robot navigation within a predefined maze. The robot (represented by a red rectangle) can be manually controlled using the **arrow keys**, and automatically detects collisions with walls or obstacles.

---

## 🧠 Introduction

This project simulates a robot navigating a maze using a graphical user interface. It's ideal for demonstrating basic robot motion, obstacle detection, and collision handling. The simulation is interactive and can be extended with AI, pathfinding algorithms, or sensor simulations.

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** (Python's standard GUI library)

---

## 🎮 Features

- Arrow key-based manual robot control  
- Obstacle-aware movement with collision detection  
- Maze created using lines and rectangles  
- Robot bounces back on hitting obstacles  
- Visually interactive and beginner-friendly interface  

---

## 🧱 Maze Structure

- The robot is represented as a red rectangle.
- Borders and walls are created using `Canvas.create_rectangle()` and `Canvas.create_line()`.
- The robot moves within the maze in steps of 10 pixels.
- An "Exit" zone is marked using a black-bordered box.
- The title **"RoboMove"** appears centered in the Exit zone.

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/hithakotian21/robo-maze-simulator.git
cd robo-maze-simulator

2. Run the Program
Make sure you have Python 3 installed.

bash
Copy
Edit
python robomaze.py
🎯 Controls
Control the robot using your keyboard:

Key	Action
↑ Up Arrow	Move Up
↓ Down Arrow	Move Down
← Left Arrow	Move Left
→ Right Arrow	Move Right

🧪 How It Works
The robot (red rectangle) is drawn using Tkinter’s Canvas.create_rectangle().

When a key is pressed, the robot moves in that direction.

Each move is validated using canvas.find_overlapping() to check for collision.

If a collision with an obstacle is detected, the robot is automatically moved back to the previous position.

The goal is to reach the "Exit" zone without touching walls or getting stuck.

📸 Screenshots
(You can add screenshots of your GUI here once the project is pushed to GitHub)
For example:
![Maze Screenshot](screenshots/maze.png)

📚 Future Improvements
Add automatic robot pathfinding using algorithms like A*, BFS, or DFS

Integrate simulated sensors (IR, LIDAR)

Add scoring, levels, or a timer

Implement GUI buttons: Reset, Start, or Theme Toggle

Export robot path or performance data






