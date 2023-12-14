import argparse
import binascii

from Crypto.PublicKey import ECC
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes


def load_key(file_path):
    with open(file_path, 'r') as f:
        key = ECC.import_key(f.read())
    return key


def decrypt_message(ciphertext, nonce, tag, public_key_file='public.pem'):
    public_key = load_key(public_key_file)

    # Generate the shared secret
    shared_secret = 111185609797537691741574424860238785124937811413803063315142078599991847714774 * public_key.pointQ

    # Hash the x-coordinate of the shared secret to get the AES key
    secret_key = SHA256.new(shared_secret.x.to_bytes()).digest()
    cipher_aes = AES.new(secret_key, AES.MODE_EAX, nonce=nonce)
    # data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    data = cipher_aes.decrypt(binascii.unhexlify(ciphertext))

    return data.hex()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decrypt data using ECC.')
    parser.add_argument('data', type=str, default='Hello, ECC!', help='The data to encrypt.')
    # parser.add_argument('--nonce', type=str, help='The data to encrypt.')
    args = parser.parse_args()

    decrypted_msg = decrypt_message(ciphertext=args.data, nonce=b'\x99\xd0;\xed\xa8\xf3\x14\xdc\xbf=\x97\xd3kb\xe5\xac', tag=b'|\x9c\xd6\x0b\x9e\x83\xa9O\xfc\x05t\x7f\x80\xf6O\x06')
    print("Decrypted:", decrypted_msg)
