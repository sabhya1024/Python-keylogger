import tkinter as tk

def capture_clipboard():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    clipboard_content = root.clipboard_get()
    return clipboard_content
