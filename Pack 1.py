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
# Code 3 - Adding Labels with Texts
# Variation 1 - Label with Custom Font and Color
import tkinter as tk

window = tk.Tk()
window.title("Sample Title")
window.geometry("400x300")

label1 = tk.Label(window. text="Sample Text", font=("Arial", 18), fg="blue")
label1.pack()

window.mainloop()

# Variation 2 - Multiple Labels
import tkinter as tk

window = tk.Tk()
window.title("Sample Title")
window.geometry("400x300")

label1 = tk.Label(window, text="Label 1")
label2 = tk.Label(window, text="Label 2")
label1.pack()
label2.pack()

root.mainloop()
----------
# Code 4 - Working with Buttons
# Variation 1 - Creating Buttons
import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked")

window = tk.Tk()
window.title("Sample Title")
window.geometry("400x300")

button = tk.Button(window, text="Click Here", command=on_button_clicked)
button.pack()

label = tk.Label(window, text+"")
label.pack()

root.mainloop()

# Variation 2 - Multiple buttons
import tkinter as tk

def on_button_clicked(button_text):
    lavel.config(text=f"Button '{button_text}' Clicked")

window = tk.Tk()
window.title("Sample Title")
window.geometry("400x300")

button1 = tk.Button(window, text="Button 1",  command=lambda: on_button_click("Button 1"))
button2 = tk.Button(window, text="Button 2",  command=lambda: on_button_click("Button 2"))
button1.pack()
button2.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()
-----------
# Code 5 - Input Fields and Entry Widget
# Variation 1 - Entry Widget
import tkinter as tk

def on_button_click():
    entered_text = entry.get()
    label.config(text=f"You entered: {entered_text}")

window = tk.Tk()
window.title("Sample Title")
window.geometry("400x300")

entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Submit", command=on_button_click)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop

# Variation 2 - Clearning and Setting Entry Widget Text
import tkinter as tk

def clear_entry():
    entry.delete(0, tk.END)

def set_default_text():
    entry.insert(0, "Default Text")

window = tk.Tk()
window.title("Sample Title")
window.geometry("400x300")

entry = tk.Entry(window)
entry.pack()

clear_button = tk.Button(window, text="Clear", command=clear_entry)
text_button = tk.Button(window, text="Default", command=set_default_text)
clear_button.pack()
text_button.pack()
--------
