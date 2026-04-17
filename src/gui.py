#GUI

#Imports:
import os
import tkinter as tk
from PIL import Image, ImageTk
from image_loader import get_valid_images
from stats import compute_stats
from storage import save_results

root = tk.Tk()
folder_path = input("Enter the folder path of your images: ")
images = get_valid_images(folder_path)
rated_images = []
current_index = 0
ratings = []

label = tk.Label(root)
label.pack()

def finish():
    stats = compute_stats(ratings)
    label.config(text=f"Finished\nMean: {stats['mean']}")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "results.json")
    save_results(file_path, images, rated_images, stats)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state="disabled")

def show_image():
    global current_index

    if current_index >= len(images):
        finish()
        return

    path = images[current_index]

    with Image.open(path) as img:
        img = img.resize((800, 500), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

    label.config(image=photo)
    label.image = photo


def handle_rating(value):
    global current_index

    print(f"Rating: {value}")
    ratings.append(value)
    rated_images.append(images[current_index])

    current_index += 1
    show_image()


for i in range(11):
    btn = tk.Button(root, text=str(i), command=lambda v=i: handle_rating(v))
    btn.pack(side="left")


show_image()

root.mainloop()
