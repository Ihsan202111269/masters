import hashlib

def file_hash(filepath):
    with open(filepath, "rb") as f:
        print("SHA-256 Hash:", hashlib.sha256(f.read()).hexdigest())

file_hash("secret.txt")

from nacl import secret, utils

key = utils.random(secret.SecretBox.KEY_SIZE)

box = secret.SecretBox(key)

message = b"Confidential Data"

encrypted = box.encrypt(message)

print("Encrypted:", encrypted)
print("Decrypted:", box.decrypt(encrypted))

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

msg = b"Integrity Check"

sig = private_key.sign(
    msg,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

public_key.verify(
    sig,
    msg,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Signature verification successful!")


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import os

# Generate a random AES key
aes_key = os.urandom(32)

# Generate RSA private and public keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# Encrypt the AES key using RSA-OAEP
encrypted_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Generate a random IV
iv = os.urandom(16)

# AES-CFB encryption
cipher = Cipher(
    algorithms.AES(aes_key),
    modes.CFB(iv)
)

encryptor = cipher.encryptor()

ciphertext = (
    encryptor.update(b"Hybrid Crypto Example")
    + encryptor.finalize()
)

print("Encrypted AES key:", encrypted_key)
print("IV:", iv)
print("Encrypted data:", ciphertext)