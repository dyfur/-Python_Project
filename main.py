import tkinter as tk
from screens import build_ui

def main():
    root = tk.Tk()
    root.title("Electronics with Spark")
    root.geometry("600x750")

    build_ui(root)

    root.mainloop()

if __name__ == "__main__":
    main()
