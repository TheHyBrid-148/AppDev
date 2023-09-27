# Code 1 - Intro to tkinter and GUI Basics
# Variation 1 - Window creation
import tkinter as tk

root = tk.Tk()
root.title("First Window")

root.mainloop()

# Variation 2 - Adding labels and texts
import tkinter as tk

root = tk.Tk()
root.title("First Window")

label = tk.Label(root, text="Sample Text")
label.pack()

root.mainloop()
--------
# Code 2 - Configurations
# Variation 1 - Basic window and custom background color
import tkinter as tk

window = tk.Tk()
window.title("Sample Window")
window.config(bg="lightblue")

window.mainloop()

# Variation 2 - Window title and size
import tkinter as tk

window = tk.Tk()
window.title("Custom Window Title")
window.geometry("400x300")

root.mainloop()
--------
