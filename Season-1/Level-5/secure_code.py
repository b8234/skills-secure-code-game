# secure_code.py

import os
import bcrypt
import secrets

class RandomGenerator:
    def generate_token(self, length=32):
        """
        Secure random token generation using secrets.token_urlsafe
        """
        return secrets.token_urlsafe(length)

    def generate_salt(self):
        """
        bcrypt handles salt generation internally; no need for manual salt generation.
        This method is retained for interface compatibility but is not used.
        """
        return bcrypt.gensalt()

class PasswordHasher:
    def __init__(self, algorithm='bcrypt'):
        if algorithm != 'bcrypt':
            raise ValueError("Only bcrypt is supported for secure password hashing.")
        self.algorithm = algorithm

    def password_hash(self, password: str) -> str:
        """
        Securely hash the password using bcrypt.
        """
        if not isinstance(password, str):
            raise TypeError("Password must be a string.")
        password_bytes = password.encode('utf-8')
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed.decode('utf-8')

    def password_verification(self, password: str, hashed_password: str) -> bool:
        """
        Verify the password against the hashed password.
        """
        if not isinstance(password, str) or not isinstance(hashed_password, str):
            return False
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        except ValueError:
            return False

# Environment-based secrets (do not hardcode!)
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')  # Avoid hardcoding; load from secure vault or env

# Always use the secure hasher
PASSWORD_HASHER = 'PasswordHasher'
