import tkinter as tk
from tkinter import *
import cv2 
from PIL import Image, ImageTk

class Box:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        
        self.label = Label(self.window, width=self.width, height=self.height)
        self.cap = cv2.VideoCapture(0)
        self.label.pack()

    def show_frames(self): # Define function to show frame

        cv2image= cv2.cvtColor(self.cap.read()[1],cv2.COLOR_BGR2RGB) # Get the latest frame and convert into Image
        img = Image.fromarray(cv2image)
        
        imgtk = ImageTk.PhotoImage(image = img) # Convert image to PhotoImage

        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        
        self.label.after(20, self.show_frames) # Repeat after an interval to capture continiously