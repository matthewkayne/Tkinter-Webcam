import tkinter as tk
from tkinter import *
from tkinter_webcam import webcam

window = tk.Tk() # Sets up GUI
window.title("Example") # Titles GUI
window.geometry("1000x1000") # Sizes GUI

video = webcam.Box(window) # Uses Box class from webcam to create video window
video.show_frames() # Show the created Box

tk.mainloop()