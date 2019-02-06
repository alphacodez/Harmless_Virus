import webbrowser
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("Wack", "Neato")
messagebox.showwarning("Bad", "Whoops")
messagebox.showerror("Oopsie", "Something will happen")

i = 0
while i <= 30:
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    i += 1
    print("Congrats, you played yourself")
