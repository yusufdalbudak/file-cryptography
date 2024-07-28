from cryptography.fernet import Fernet

def load_key():
    return open("encryption_key.key", "rb").read()

# Şifre çözme
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_name, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    decrypt_file("encrypted_files.txt")
