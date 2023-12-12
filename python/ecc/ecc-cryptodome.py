from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256


def ecc_encrypt(public_key, data):
    """ Encrypt data using ECC and AES. """
    cipher_aes = None
    ciphertext = None

    # Generate a private key for this encryption
    private_key = ECC.generate(curve='P-256')
    shared_secret = private_key.d * public_key.pointQ

    # Hash the x-coordinate of the shared secret to get the AES key
    secret_key = SHA256.new(shared_secret.x.to_bytes()).digest()
    cipher_aes = AES.new(secret_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    return private_key, ciphertext, cipher_aes.nonce, tag


def ecc_decrypt(private_key, public_key, ciphertext, nonce, tag):
    """ Decrypt data using ECC and AES. """
    # Generate the shared secret
    shared_secret = private_key.d * public_key.pointQ

    # Hash the x-coordinate of the shared secret to get the AES key
    secret_key = SHA256.new(shared_secret.x.to_bytes()).digest()
    cipher_aes = AES.new(secret_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    return data


# Generate ECC keys
private_key = ECC.generate(curve='P-256')
public_key = private_key.public_key()

# Encrypt a message
message = b'Hello, ECC!'
temp_private_key, ciphertext, nonce, tag = ecc_encrypt(public_key, message)

# Decrypt the message
decrypted_message = ecc_decrypt(temp_private_key, public_key, ciphertext, nonce, tag)

print("Original Message:", message)
print("Encrypted Message:", ciphertext)
print("Decrypted Message:", decrypted_message)
