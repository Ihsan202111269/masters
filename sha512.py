from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA512())

message = b"Hello Cryptography"

digest.update(message)

hash_value = digest.finalize()

print("SHA-512:", hash_value.hex())