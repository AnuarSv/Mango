from tkinter import *
import tkinter as tk
from Conversation import *

def display(response, time=1200):
    display_text_on_screen(response, time)
    save_conversations_to_file('conversation_history.txt')

def display_text_on_screen(text, time=1200):
    text = text[:text.find(".")]
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = screen_width // 4
    window_height = 10
    x_position = (screen_width // 2) - (window_width // 2)
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.wm_attributes('-alpha', .4)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{screen_height - window_height}")
    label = tk.Label(root, text=text, fg='#ffffff', bg='#1c1c1c')
    label.pack(side=tk.LEFT)

    def destroy_root():
        root.destroy()

    root.after(time, destroy_root)
    root.mainloop()

