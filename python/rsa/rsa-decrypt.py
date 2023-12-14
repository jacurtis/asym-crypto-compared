import argparse
import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def rsa_decrypt(data, private_key=None):
    """ Encrypt data using RSA. """

    if private_key is None:
        # Load public key from a file
        with open('private.pem', 'r') as f:
            private_key = RSA.import_key(f.read())
        # with open('public.pem', 'r') as f:
        #     private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(binascii.unhexlify(data))
    return plaintext.decode()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decrypt data using RSA.')
    parser.add_argument('ciphertext', type=str, help='The data to decrypt.')
    args = parser.parse_args()

    plaintext = rsa_decrypt(args.ciphertext)
    print(plaintext)
