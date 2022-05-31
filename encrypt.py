from cryptography.fernet import Fernet
from tkinter import filedialog

filepath = filedialog.askopenfilename(title="Select a File", filetypes=[("All files", "*.*")])

key = Fernet.generate_key()
with open("secret.key", "wb") as secret:
    secret.write(key)

with open(filepath, "rb") as file:
    contents = file.read()
encrypted = Fernet(key).encrypt(contents)

with open(filepath, "wb") as file:
    file.write(encrypted)

print("File encrypted!")
