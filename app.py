import tkinter as tk
import time

def animate_text(label, text):
    for i in range(len(text)+1):
        label.config(text=text[:i])
        label.update()
        time.sleep(0.1)

root = tk.Tk()
root.title("Message Display, Hola Amigo")
root.geometry("400x200")

label = tk.Label(root, text="", font=("Helvetica", 20, "bold"))
label.pack(expand=True)

animate_text(label, "Hello, CI/CD World!")

root.mainloop()

