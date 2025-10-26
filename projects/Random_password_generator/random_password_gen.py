import string
import random
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        alphabets_count = int(alpha_entry.get())
        digits_count = int(digits_entry.get())
        special_count = int(special_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return

    characters_count = alphabets_count + digits_count + special_count

    if characters_count > length:
        messagebox.showerror("Error", "Character counts exceed password length!")
        return

    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list("!@#$%^&()")
    characters = list(string.ascii_letters + string.digits + "!@#$%^&()")

    password = []

    for _ in range(alphabets_count):
        password.append(random.choice(alphabets))
    for _ in range(digits_count):
        password.append(random.choice(digits))
    for _ in range(special_count):
        password.append(random.choice(special_characters))
    if characters_count < length:
        random.shuffle(characters)
        for _ in range(length - characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)
    result_var.set("".join(password))

# Copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("🔒 Random Password Generator")
root.geometry("450x400")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# Center the window on screen
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2 - 200
y = (root.winfo_screenheight() - root.winfo_reqheight()) // 2 - 200
root.geometry(f"+{x}+{y}")

# Title label
title_label = tk.Label(root, text="Random Password Generator", 
                       font=("Helvetica", 18, "bold"), fg="white", bg="#1e1e2e")
title_label.pack(pady=20)

# Frame for inputs
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=10)

label_style = {"font": ("Segoe UI", 11), "fg": "white", "bg": "#1e1e2e"}
entry_style = {"bg": "#2e2e3e", "fg": "white", "insertbackground": "white",
               "font": ("Segoe UI", 10), "relief": "flat", "justify": "center"}

tk.Label(frame, text="Password Length:", **label_style).grid(row=0, column=0, pady=5, sticky="w")
length_entry = tk.Entry(frame, **entry_style)
length_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Alphabets Count:", **label_style).grid(row=1, column=0, pady=5, sticky="w")
alpha_entry = tk.Entry(frame, **entry_style)
alpha_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Digits Count:", **label_style).grid(row=2, column=0, pady=5, sticky="w")
digits_entry = tk.Entry(frame, **entry_style)
digits_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Special Characters Count:", **label_style).grid(row=3, column=0, pady=5, sticky="w")
special_entry = tk.Entry(frame, **entry_style)
special_entry.grid(row=3, column=1, padx=10, pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", font=("Segoe UI", 12, "bold"),
                         bg="#00adb5", fg="white", relief="flat", padx=10, pady=5,
                         activebackground="#00bfc7", activeforeground="white",
                         command=generate_password)
generate_btn.pack(pady=15)

# Result area
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, width=40, font=("Consolas", 12),
                        bg="#2e2e3e", fg="#00ff99", justify="center", relief="flat")
result_entry.pack(pady=5)

# Copy button
copy_btn = tk.Button(root, text="Copy to Clipboard", font=("Segoe UI", 10, "bold"),
                     bg="#393e46", fg="white", relief="flat", padx=10, pady=5,
                     activebackground="#4e545f", activeforeground="white",
                     command=copy_to_clipboard)
copy_btn.pack(pady=10)

# Footer
footer = tk.Label(root, text="Developed by Sanika 💻", fg="#aaaaaa", bg="#1e1e2e", font=("Segoe UI", 9))
footer.pack(side="bottom", pady=10)

root.mainloop()
