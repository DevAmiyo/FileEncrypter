from cryptography.fernet import Fernet
from tkinter import filedialog

keypath = filedialog.asksaveasfilename(title="Save As", filetypes=[("Key File", "*.key")])
files = filedialog.askopenfilenames(title="Select Files", filetypes=[("All Files", "*.*")])

if keypath:
    if files:
        key = Fernet.generate_key()
        with open(keypath, "wb") as secret:
            secret.write(key)
        for filepath in files:
            with open(filepath, "rb") as file:
                contents = file.read()
            encrypted = Fernet(key).encrypt(contents)
            with open(filepath, "wb") as file:
                file.write(encrypted)
        print("File"+("s" if len(files) > 1 else "")+" encrypted!")
    else:
        print("Error: No files were selected.")
else:
    print("Error: The key was not saved.")