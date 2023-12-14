import argparse
from Crypto.PublicKey import RSA


def generate_key(key_length=2048, save_keys=False):
    # Generate an RSA key pair
    key = RSA.generate(key_length)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    if save_keys:
        with open("public.pem", "wb") as f:
            f.write(public_key)
        with open("private.pem", "wb") as f:
            f.write(private_key)
    return public_key, private_key


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate RSA keys.')
    parser.add_argument('--key_length', type=int, default=2048, help='The length of the RSA keys to generate.')
    parser.add_argument('--save_keys', type=bool, default=False, help='Whether to save the keys to files.')
    args = parser.parse_args()

    public_key, private_key = generate_key(key_length=args.key_length, save_keys=args.save_keys)
    print("Public key:\n", public_key.decode())
    print("\nPrivate key:\n", private_key.decode())
