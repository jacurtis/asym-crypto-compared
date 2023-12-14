import argparse
import base64

from Crypto.Util.number import getPrime, getRandomRange
from Crypto.PublicKey import ElGamal


def generate_key(key_length=2048):
    # Generate a 2048-bit prime number
    p = getPrime(key_length)
    # Generate a private key
    x = getRandomRange(1, p - 2)
    # Generate a public key
    g = 2  # we use a fixed generator for simplicity, but a more secure method would use a randomly chosen generator.
    y = pow(g, x, p)
    public_key = (p, g, y)
    public_key = ElGamal.construct((p, g, y))
    private_key = (p, x)
    public_key_string = ",".join([str(x) for x in public_key])
    private_key_string = ",".join([str(x) for x in private_key])

    return public_key_string, private_key_string


# def encrypt(public_key, message):
#     # Encrypt the message
#     p, g, y = public_key.key
#     k = getRandomRange(1, p - 2)
#     c1 = pow(g, k, p)
#     s = pow(y, k, p)
#     c2 = (message * s) % p
#     return c1, c2


def encrypt(public_key, message):
    # Encrypt a message using the public key
    message = bytes(message, 'utf-8')
    plaintext = int.from_bytes(message, 'big')
    # ElGamal
    public_key_decoded = base64.b64decode(public_key)
    print(public_key_decoded)

    # Generate a random number k
    k = getRandomRange(1, p - 2)

    # Compute the ciphertext
    c1 = pow(g, k, p)
    c2 = plaintext * pow(y, k, p) % p
    ciphertext = (c1, c2)
    return ciphertext


def main():
    parser = argparse.ArgumentParser(description='ElGamal encryption.')
    parser.add_argument('operation', type=str, help='Operation to perform: generate_key or encrypt')
    parser.add_argument('message', type=str, nargs='?', default='', help='Message to encrypt')
    parser.add_argument('public_key', type=str, nargs='?', default='', help='Public key for encryption')
    args = parser.parse_args()

    if args.operation == 'generate_key':
        public, private = generate_key()
        print('Public key:', public)
        print('Private key:', private)
    elif args.operation == 'encrypt':
        if args.message == '':
            print('Error: No message provided for encryption')
        else:
            # public_key, _ = generate_key()
            # public_key = ElGamal.construct((public_key)
            print(encrypt(args.public_key, args.message))
    else:
        print('Error: Invalid operation')


if __name__ == "__main__":
    main()