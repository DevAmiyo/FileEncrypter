from cryptography.fernet import Fernet
from tkinter import Tk
from tkinter import filedialog

root = Tk()
root.withdraw()

root.iconbitmap('assets/file.ico')
files = filedialog.askopenfilenames(title="Select Files to Encrypt", filetypes=[("All Files", "*.*")])
root.iconbitmap('assets/key.ico')
keypath = filedialog.asksaveasfilename(title="Save Key", filetypes=[("Key File", "*.key")])

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