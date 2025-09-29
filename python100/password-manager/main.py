import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)  
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "f"\nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            try:
                with open(r"D:\\pythonlearning\\python100\\password-manager\\data.json", "r") as data_file:  # Fixed with raw string
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(r"D:\\pythonlearning\\python100\\password-manager\\data.json", "w") as data_file:  # Fixed with raw string
                    # Creating new file and adding data
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open(r"D:\\pythonlearning\\python100\\password-manager\\data.json", "w") as data_file:  # Fixed with raw string
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                    # Clearing the fields
                    website_entry.delete(0, tk.END)
                    password_entry.delete(0, tk.END)
#----------------------------Find Password ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(r"D:\\pythonlearning\\python100\\password-manager\\data.json", "r") as data_file:  # Fixed with raw string
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("🔐 MyPass - Password Manager")
window.config(padx=60, pady=40, bg='#2C3E50')  # Dark blue-gray background
window.resizable(False, False)  # Prevent resizing for better layout control

# Define color scheme
COLORS = {
    'bg': '#2C3E50',      # Dark blue-gray
    'primary': '#3498DB',  # Bright blue
    'secondary': '#E74C3C', # Red
    'accent': '#F39C12',   # Orange
    'success': '#27AE60',  # Green
    'text': '#ECF0F1',     # Light gray
    'white': '#FFFFFF',
    'entry_bg': '#34495E', # Darker blue-gray
    'button_bg': '#3498DB' # Blue
}

# Define fonts
FONTS = {
    'title': ('Segoe UI', 16, 'bold'),
    'label': ('Segoe UI', 11, 'normal'),
    'entry': ('Segoe UI', 10, 'normal'),
    'button': ('Segoe UI', 9, 'bold')
}

# Canvas for logo with better styling
canvas = tk.Canvas(height=220, width=220, bg=COLORS['bg'], highlightthickness=0)
try:
    logo_img = tk.PhotoImage(file=r"logo.png")  # Fixed path with raw string
    canvas.create_image(110, 110, image=logo_img)
except tk.TclError:
    # If logo not found, create a simple text logo
    canvas.create_text(110, 110, text="🔐\nMyPass", font=FONTS['title'], 
                      fill=COLORS['primary'], justify=tk.CENTER)
canvas.grid(row=0, column=1, pady=(0, 30))    

# Labels with improved styling
website_label = tk.Label(text="Website:", font=FONTS['label'], 
                        fg=COLORS['text'], bg=COLORS['bg'])
website_label.grid(row=1, column=0, sticky='e', padx=(0, 15), pady=8)

email_label = tk.Label(text="Email/Username:", font=FONTS['label'],
                      fg=COLORS['text'], bg=COLORS['bg'])
email_label.grid(row=2, column=0, sticky='e', padx=(0, 15), pady=8)

password_label = tk.Label(text="Password:", font=FONTS['label'],
                         fg=COLORS['text'], bg=COLORS['bg'])
password_label.grid(row=3, column=0, sticky='e', padx=(0, 15), pady=8)

# Entries with improved styling
website_entry = tk.Entry(width=32, font=FONTS['entry'], bg=COLORS['entry_bg'], 
                        fg=COLORS['white'], insertbackground=COLORS['white'],
                        relief=tk.FLAT, bd=5)
website_entry.grid(row=1, column=1, sticky='ew', pady=8)
website_entry.focus()

email_entry = tk.Entry(width=32, font=FONTS['entry'], bg=COLORS['entry_bg'],
                      fg=COLORS['white'], insertbackground=COLORS['white'],
                      relief=tk.FLAT, bd=5)
email_entry.grid(row=2, column=1, columnspan=2, sticky='ew', pady=8)
email_entry.insert(0, "vtiwari@ishir.com")

password_entry = tk.Entry(width=19, font=FONTS['entry'], bg=COLORS['entry_bg'],
                         fg=COLORS['white'], insertbackground=COLORS['white'],
                         relief=tk.FLAT, bd=5)
password_entry.grid(row=3, column=1, sticky='ew', pady=8, padx=(0, 8)) 

# Buttons with improved styling
search_button = tk.Button(text="🔍 Search", width=16, font=FONTS['button'],
                         bg=COLORS['accent'], fg=COLORS['white'], 
                         relief=tk.FLAT, bd=0, cursor='hand2',
                         activebackground=COLORS['secondary'], command=find_password)
search_button.grid(row=1, column=2, pady=8, padx=(8, 0))

generate_password_button = tk.Button(text="🎲 Generate Password", font=FONTS['button'],
                                   bg=COLORS['primary'], fg=COLORS['white'],
                                   relief=tk.FLAT, bd=0, cursor='hand2',
                                   activebackground=COLORS['secondary'],
                                   command=generate_password)
generate_password_button.grid(row=3, column=2, pady=8, padx=(8, 0))

add_button = tk.Button(text="💾 Add Password", width=35, font=FONTS['button'],
                      bg=COLORS['success'], fg=COLORS['white'],
                      relief=tk.FLAT, bd=0, cursor='hand2',
                      activebackground=COLORS['secondary'],
                      command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=(20, 10))

# Configure grid column weights for responsive design
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

# Add a subtle footer
footer_label = tk.Label(text="Secure • Simple • Reliable", 
                       font=('Segoe UI', 8, 'italic'),
                       fg='#95A5A6', bg=COLORS['bg'])  # Lighter gray for subtle effect
footer_label.grid(row=5, column=0, columnspan=3, pady=(10, 0))


window.mainloop()