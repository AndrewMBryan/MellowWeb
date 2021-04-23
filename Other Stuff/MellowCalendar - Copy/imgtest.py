
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

img = Image.open('../MellowFlowApp/upload.png')
width, height = img.size

canvas = tk.Canvas(window, width = width, height = height)
canvas.pack()

photo = ImageTk.PhotoImage(img)
canvas.create_image(width//2, height//2, image=photo)

window.mainloop()

