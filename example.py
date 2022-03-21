"""Example"""
import tkinter as tk
from tkinter_webcam import webcam

window = tk.Tk()  # Sets up GUI
window.title("Example")  # Titles GUI
window.geometry("1000x1000")  # Sizes GUI

# Uses Box class from webcam to create video window
video = webcam.Box(window, width=450, height=450)
video.show_frames()  # Show the created Box

tk.mainloop()
