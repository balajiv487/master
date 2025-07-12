# Imports
import hashlib
from base64 import b64encode, b64decode
import os
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import platform


if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

def encrypt(plain_text,password):
    if not password:
        raise ValueError("Password cannot be empty.")
    s=get_random_bytes(AES.block_size)
    private_key=hashlib.scrypt(password.encode(),s=s,n=2**14,p=1,dk_len=32)


