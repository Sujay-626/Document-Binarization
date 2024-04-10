import tkinter as tk
from tkinter import filedialog
import subprocess
import tkinter.messagebox as messagebox

def run_binarize():
    img_path = img_entry.get()
    model_path = model_entry.get()
    cmd = f"python binarize.py -imgpath {img_path} -modelpath {model_path} -w 256 -s 96 -f 64 -k 5 -stride 2 -th 0.5 --demo"
    try:
        subprocess.run(cmd, shell=True, check=True)
        # Display output image
        output_img = "output_img.png"  # Assuming this is the name of the output image
        output_label.config(text=output_img)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error occurred: {e}")


def browse_img():
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    img_entry.delete(0, tk.END)
    img_entry.insert(0, img_path)

def browse_model():
    model_path = filedialog.askopenfilename(filetypes=[("Model files", "*.h5")])
    model_entry.delete(0, tk.END)
    model_entry.insert(0, model_path)

root = tk.Tk()
root.title("Image Binarization")

# Image selection
img_label = tk.Label(root, text="Select Image:")
img_label.grid(row=0, column=0, padx=10, pady=5)
img_entry = tk.Entry(root, width=50)
img_entry.grid(row=0, column=1, padx=10, pady=5)
browse_img_button = tk.Button(root, text="Browse", command=browse_img)
browse_img_button.grid(row=0, column=2, padx=10, pady=5)

# Model selection
model_label = tk.Label(root, text="Select Model:")
model_label.grid(row=1, column=0, padx=10, pady=5)
model_entry = tk.Entry(root, width=50)
model_entry.grid(row=1, column=1, padx=10, pady=5)
browse_model_button = tk.Button(root, text="Browse", command=browse_model)
browse_model_button.grid(row=1, column=2, padx=10, pady=5)

# Run button
run_button = tk.Button(root, text="Run Binarization", command=run_binarize)
run_button.grid(row=2, column=1, padx=10, pady=10)

# Output label
output_label = tk.Label(root, text="")
output_label.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
