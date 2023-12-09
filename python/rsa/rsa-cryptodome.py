from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate an RSA key pair
key = RSA.generate(2048)

# Create an RSA cipher object
cipher = PKCS1_OAEP.new(key)

# Encrypt and decrypt a message
message = b'Hello, RSA!'
encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
