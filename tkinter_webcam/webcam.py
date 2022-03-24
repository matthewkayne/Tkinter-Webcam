"""Webcam"""
from tkinter import Label
from PIL import Image, ImageTk
import cv2


class Box:
    """Box"""

    def __init__(self, window, width=450, height=450):
        self.window = window
        self.width = width
        self.height = height

        self.label = Label(self.window, width=self.width, height=self.height)
        self.cap = cv2.VideoCapture(0)
        self.label.pack()

    def get_box_info(self):
        """Gets Box Information """
        print(f"Window: {self.window}")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")

    def show_frames(self):  # Define function to show frame
        """Show Frames"""
        # Get the latest frame and convert into Image
        cv2image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)

        imgtk = ImageTk.PhotoImage(image=img)  # Convert image to PhotoImage

        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

        # Repeat after an interval to capture continiously
        self.label.after(20, self.show_frames)
