import customtkinter as ctk #need this shit dumbass
import random
import string
import tkinter as tk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("nutting-dev pswd gen")
app.geometry("440x309")

instruction_label = ctk.CTkLabel(app, text="create secure pa$$w0rds", font=("Segoe UI", 13, "bold"))
instruction_label.pack(pady=(0, 16))

options_frame = ctk.CTkFrame(app)
options_frame.pack(pady=8, padx=16, fill="x")

length_label = ctk.CTkLabel(options_frame, text="length:", font=("Segoe UI", 12))
length_label.grid(row=0, column=0, sticky="w", padx=(10, 0), pady=(10, 0))
length_slider = ctk.CTkSlider(options_frame, from_=8, to=32, number_of_steps=24, width=180)
length_slider.set(12)
length_slider.grid(row=0, column=1, padx=10, pady=(10, 0))

letters_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)

letters_checkbox = ctk.CTkCheckBox(options_frame, text="Letters", variable=letters_var, font=("Segoe UI", 11))
letters_checkbox.grid(row=1, column=0, sticky="w", padx=(10, 0), pady=(8, 0))
numbers_checkbox = ctk.CTkCheckBox(options_frame, text="Numbers", variable=numbers_var, font=("Segoe UI", 11))
numbers_checkbox.grid(row=1, column=1, sticky="w", padx=(10, 0), pady=(8, 0))
symbols_checkbox = ctk.CTkCheckBox(options_frame, text="Symbols", variable=symbols_var, font=("Segoe UI", 11))
symbols_checkbox.grid(row=1, column=2, sticky="w", padx=(10, 0), pady=(8, 0))

password_entry = ctk.CTkEntry(app, width=260, font=("Consolas", 14))
password_entry.pack(pady=(18, 8))
password_entry.configure(state="readonly")

def gen_pwsd(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if not chars:
        return ''
    return ''.join(random.choice(chars) for _ in range(length))

def on_gen_pswd():
    length = int(length_slider.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    password = gen_pwsd(length, use_letters, use_numbers, use_symbols)
    password_entry.configure(state="normal")
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    password_entry.configure(state="readonly")

def on_cpy_pswd():
    app.clipboard_clear()
    app.clipboard_append(password_entry.get())
    password_entry.configure(placeholder_text="copied")
    app.after(1000, lambda: password_entry.configure(placeholder_text=""))

generate_button = ctk.CTkButton(app, text="gen", command=on_gen_pswd, font=("Segoe UI", 11, "bold"))
generate_button.pack(pady=(4, 6))

copy_button = ctk.CTkButton(app, text="copy", command=on_cpy_pswd, font=("Segoe UI", 11, "bold"))
copy_button.pack(pady=(0, 10))

app.mainloop()
