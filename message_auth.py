from nacl import secret, utils

key = utils.random(secret.SecretBox.KEY_SIZE)

box = secret.SecretBox(key)

message = b"Authenticated Message"

encrypted = box.encrypt(message)

print("Encrypted message:", encrypted)

decrypted = box.decrypt(encrypted)

print("Decrypted message:", decrypted)