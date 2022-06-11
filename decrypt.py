from cryptography.fernet import Fernet
from tkinter import filedialog

files = filedialog.askopenfilenames(title="Select Files", filetypes=[("All Files", "*.*")])
keypath = filedialog.askopenfilename(title="Select Key", filetypes=[("Key File", "*.key")])

try:
    if files:
        if keypath:
            with open(keypath, "rb") as secret:
                key = secret.read()
            for filepath in files:
                with open(filepath, "rb") as file:
                    contents = file.read()
                decrypted = Fernet(key).decrypt(contents)
                with open(filepath, "wb") as file:
                    file.write(decrypted)
                print("File"+("s" if len(files) > 1 else "")+" decrypted!")
        else:
            print("Error: Decryption key was not provided.")
    else:
        print("Error: No files were selected.")
except Exception:
    print("An error occurred. Please check if the key provided is valid and if the files are encrypted.")