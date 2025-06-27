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

### 2. Run the Program

