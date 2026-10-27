import hashlib

def file_hash(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

hash1 = file_hash("file1.txt")
hash2 = file_hash("file2.txt")

print("File 1:", hash1)
print("File 2:", hash2)

if hash1 == hash2:
    print("Files are identical.")
else:
    print("Files are different.")