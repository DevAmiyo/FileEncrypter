from cryptography.fernet import Fernet
from tkinter import filedialog

keypath = filedialog.askopenfilename(title="Select A Key", filetypes=[("Key File", "*.key")])

with open(keypath, "rb") as secret:
    key = secret.read()

filepath = filedialog.askopenfilename(title="Select A File", filetypes=[("All Files", "*.*")])

with open(filepath, "rb") as file:
    contents = file.read()
decrypted = Fernet(key).decrypt(contents)

with open(filepath, "wb") as file:
    file.write(decrypted)

print("File decrypted!")
