from cryptography.fernet import Fernet
from tkinter import filedialog

keypath = filedialog.asksaveasfilename(title="Save Key As", filetypes=[("Key File", "*.key")])
key = Fernet.generate_key()
with open(keypath, "wb") as secret:
    secret.write(key)

filepath = filedialog.askopenfilename(title="Select A File", filetypes=[("All Files", "*.*")])
with open(filepath, "rb") as file:
    contents = file.read()
encrypted = Fernet(key).encrypt(contents)

with open(filepath, "wb") as file:
    file.write(encrypted)

print("File encrypted!")
