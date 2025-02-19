import os
import csv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import imageio

# File paths
GIF_FOLDER = "/home/jecroisp/Thesis/processed_data/TestingData/downLoadedGifs"  # Folder containing GIFs
OUTPUT_CSV = "manual_labels.csv"

# Emotion labels
LABELS = ["Anger", "Disgust", "Fear", "Happiness", "Neutral", "Sadness"]

# Load GIFs
gif_files = [f for f in os.listdir(GIF_FOLDER) if f.endswith(".gif")]
current_index = 0  # Track current GIF index

# Load existing labels to avoid duplicates
labeled_files = set()
if os.path.exists(OUTPUT_CSV):
    with open(OUTPUT_CSV, "r") as file:
        reader = csv.reader(file)
        labeled_files = {row[0] for row in reader}

# Skip already labeled GIFs
gif_files = [f for f in gif_files if f not in labeled_files]

# Create the GUI window
root = tk.Tk()
root.title("GIF Labeling App")
root.geometry("600x600")

# Load and display GIF
def load_gif():
    """Displays the current GIF."""
    global gif_label, current_index
    if current_index < len(gif_files):
        gif_path = os.path.join(GIF_FOLDER, gif_files[current_index])
        gif = imageio.mimread(gif_path)  # Read all frames
        middle_frame = gif[len(gif) // 2]  # Extract middle frame
        img = Image.fromarray(middle_frame).convert("RGB")
        img = img.resize((300, 300))  # Resize for better display
        img_tk = ImageTk.PhotoImage(img)

        gif_label.config(image=img_tk)
        gif_label.image = img_tk  # Keep reference
        filename_label.config(text=f"Labeling: {gif_files[current_index]}")

# Save the labeled GIF to CSV
def save_label(label):
    """Saves the selected label to the CSV file and moves to the next GIF."""
    global current_index
    if current_index < len(gif_files):
        with open(OUTPUT_CSV, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([gif_files[current_index], label])

        current_index += 1
        if current_index < len(gif_files):
            load_gif()
        else:
            filename_label.config(text="🎉 All GIFs Labeled! 🎉")
            gif_label.config(image="")

# Create UI elements
filename_label = tk.Label(root, text="Loading...", font=("Arial", 14))
filename_label.pack(pady=10)

gif_label = tk.Label(root)
gif_label.pack()

# Create labeling buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

for lbl in LABELS:
    btn = ttk.Button(button_frame, text=lbl, command=lambda l=lbl: save_label(l))
    btn.pack(side=tk.LEFT, padx=5)

# Load first GIF
load_gif()

# Run the app
root.mainloop()
