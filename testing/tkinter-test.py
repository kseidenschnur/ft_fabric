import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
window = tk.Tk()

# Create a label widget
label = tk.Label(window, text="Enter your name:")
label.pack()

# Create an entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button widget
button = tk.Button(window, text="Greet", command=on_button_click)
button.pack()

# Start the main event loop
window.mainloop()
