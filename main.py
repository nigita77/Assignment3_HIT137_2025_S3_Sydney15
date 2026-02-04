import tkinter as tk
from core.controller import Controller
from core.gui import AppGUI

def main():
    root = tk.Tk()

    #initial window size
    root.geometry("700x500") 

    controller = Controller()
    AppGUI(root, controller)

    root.mainloop()

if __name__ == "__main__":
    main()
