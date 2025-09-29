import tkinter as tk

def on_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x150")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14 ))
label.pack(pady=20)
input = tk.Entry(root, width=10)
input.pack(pady=10)
button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

root.mainloop()