import tkinter as tk

from frame_view import LoginFrame
from model import Database

root = tk.Tk()
root.geometry("300x200")
root.title("Bank GUI Login Module")
root.configure(bg="#607b8d")
root.resizable(False, False)

database = Database()
box = LoginFrame(root, database)

root.mainloop()
