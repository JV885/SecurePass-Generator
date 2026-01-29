import tkinter as tk
from tkinter import messagebox
import secrets
import string


def generate_string():
    length = length_slider.get()
    pool = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(secrets.choice(pool) for _ in range(length))
    output_label.config(text=result)


def copy_to_clipboard():
    text_to_copy = output_label.cget("text")
    if text_to_copy:
        root.clipboard_clear()
        root.clipboard_append(text_to_copy)
        messagebox.showinfo("Copied", "Password copied to clipboard.")


# --- UI Setup ---
root = tk.Tk()
root.title("SecurePass Generator")
root.geometry("450x300")
root.resizable(False, False)

tk.Label(root, text="Password Length (20-100)",
         font=("Arial", 10, "bold")).pack(pady=10)

length_slider = tk.Scale(root, from_=20, to=100,
                         orient="horizontal", length=300)
length_slider.set(24)
length_slider.pack()

tk.Button(root, text="Generate", command=generate_string,
          bg="#2196F3", fg="white", width=15).pack(pady=15)

result_frame = tk.LabelFrame(root, text="Result", padx=10, pady=10)
result_frame.pack(padx=20, fill="x")

output_label = tk.Label(result_frame, text="Click Generate",
                        font=("Consolas", 10), wraplength=380)
output_label.pack()

tk.Button(root, text="Copy to Clipboard",
          command=copy_to_clipboard).pack(pady=10)

root.mainloop()
