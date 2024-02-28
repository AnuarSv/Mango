import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
window = tk.Tk()
window.geometry('200x200')
window.title('Images')

# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# window_width = screen_width // 4
# window_height = 10
# x_position = (screen_width // 2) - (window_width // 2)
window.overrideredirect(True)
window.attributes('-topmost', True)
window.wm_attributes('-alpha', 1)
#window.geometry(f"{window_width}x{window_height}+{x_position}+{screen_height - window_height}")
image_original = Image.open('loading.gif').resize((200,200))
for i in range(0, image_original.n_frames):
    image_original.seek(i)

print(image_original.n_frames)
image_resize = image_original.resize((200,200))
image_tk = ImageTk.PhotoImage(image_original)
label = ttk.Label(window, image = image_tk, background='#1c1c1c')
label.pack()
window.mainloop()
