import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# Anahtar oluşturma ve saklama
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Anahtarı yükleme
def load_key():
    return open("encryption_key.key", "rb").read()

# Dosya şifreleme
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_name, "wb") as file:
        file.write(encrypted_data)
    
    messagebox.showinfo("Success", f"{file_name} has been encrypted.")

# Dosya şifre çözme
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_name, "wb") as file:
        file.write(decrypted_data)
    
    messagebox.showinfo("Success", f"{file_name} has been decrypted.")

# Dosya seçme
def select_file():
    file_name = filedialog.askopenfilename()
    return file_name

# Şifreleme işlemi
def encrypt():
    file_name = select_file()
    if file_name:
        encrypt_file(file_name)

# Şifre çözme işlemi
def decrypt():
    file_name = select_file()
    if file_name:
        decrypt_file(file_name)

# GUI oluşturma
root = tk.Tk()
root.title("File Encryptor/Decryptor")

frame = tk.Frame(root)
frame.pack(pady=20)

encrypt_button = tk.Button(frame, text="Encrypt File", command=encrypt)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = tk.Button(frame, text="Decrypt File", command=decrypt)
decrypt_button.grid(row=0, column=1, padx=10)

# Anahtar dosyasının var olup olmadığını kontrol et
if not os.path.exists("encryption_key.key"):
    generate_key()

root.mainloop()
