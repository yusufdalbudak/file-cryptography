from cryptography.fernet import Fernet

#Creating Key and saving

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
            key_file.write (key)
            
            
            
#upload to key
def load_key():
    return open("encryption_key.key", "rb").read()

#Encryption file
def encrypt(file_name):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_name, "rb") as file:
        file_data = file.read()
        
    encrypted_data = fernet.encrypt(file_data)
    
    with open(file_name, "wb") as file:
        file.write(encrypted_data)
        

if __name__=="__main__":
    generate_key()
    encrypt("encrypted_files.txt")
    