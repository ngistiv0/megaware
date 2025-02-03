import hashlib
import os
from cryptography.fernet import Fernet
from getpass import getpass

class MegaWare:
    def __init__(self):
        self.key = self.load_key()
        self.cipher_suite = Fernet(self.key)

    def load_key(self):
        """Load or generate a new key"""
        if os.path.exists("secret.key"):
            with open("secret.key", "rb") as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(key)
            return key

    def hash_password(self, password):
        """Hash a password for storing."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        return stored_password == self.hash_password(provided_password)

    def encrypt_data(self, data):
        """Encrypt data"""
        return self.cipher_suite.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        """Decrypt data"""
        return self.cipher_suite.decrypt(encrypted_data).decode()

    def authenticate_user(self):
        """Simulate user authentication"""
        stored_password_hash = self.hash_password("securepassword")
        attempts = 3

        while attempts > 0:
            user_password = getpass("Enter your password: ")
            if self.verify_password(stored_password_hash, user_password):
                print("Authentication successful.")
                return True
            else:
                attempts -= 1
                print(f"Invalid password. {attempts} attempts remaining.")

        print("Authentication failed.")
        return False

    def secure_communication(self):
        """Simulate secure data transmission"""
        if self.authenticate_user():
            message = input("Enter a message to encrypt: ")
            encrypted_message = self.encrypt_data(message)
            print(f"Encrypted message: {encrypted_message}")

            decrypted_message = self.decrypt_data(encrypted_message)
            print(f"Decrypted message: {decrypted_message}")
        else:
            print("Access denied.")

if __name__ == "__main__":
    mw = MegaWare()
    mw.secure_communication()