import argparse

from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes


def load_key(file_path):
    with open(file_path, 'r') as f:
        key = ECC.import_key(f.read())
    return key


def encrypt_message(message, public_key_file='public.pem'):
    public_key = load_key(public_key_file)

    # Generate a private key for this encryption
    temp_private_key = ECC.generate(curve='P-256')
    shared_secret = temp_private_key.d * public_key.pointQ

    # Hash the x-coordinate of the shared secret to get the AES key
    secret_key = SHA256.new(shared_secret.x.to_bytes()).digest()
    cipher_aes = AES.new(secret_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode())

    return temp_private_key, ciphertext.hex(), cipher_aes.nonce, tag


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt data using ECC.')
    parser.add_argument('data', type=str, default='Hello, ECC!', help='The data to encrypt.')
    args = parser.parse_args()

    encrypted_msg = encrypt_message(args.data)
    print("Encrypted:", encrypted_msg)
