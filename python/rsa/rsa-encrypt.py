import argparse

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def rsa_encrypt(data, public_key=None):
    """ Encrypt data using RSA. """

    if public_key is None:
        # Load public key from a file
        with open('public.pem', 'r') as f:
            public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(bytes(data, 'utf-8'))
    return ciphertext


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt data using RSA.')
    parser.add_argument('data', type=str, default='Hello, RSA!', help='The data to encrypt.')
    args = parser.parse_args()

    ciphertext = rsa_encrypt(args.data)
    print(ciphertext.hex())
