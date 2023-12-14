import argparse

from Crypto.PublicKey import ECC


def generate_ecc_keys(curve_type='P-256', save_keys=False):
    private_key = ECC.generate(curve=curve_type)
    public_key = private_key.public_key()

    if save_keys:
        with open("public.pem", "wb") as f:
            f.write(public_key.export_key(format='PEM').encode())
        with open("private.pem", "wb") as f:
            f.write(private_key.export_key(format='PEM').encode())

    return private_key, public_key


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate ECC keys.')
    parser.add_argument('--curve_type', type=str, default='P-256', help='The length of the ECC keys to generate.')
    parser.add_argument('--save_keys', type=bool, default=False, help='Whether to save the keys to files.')
    args = parser.parse_args()

    private_key, public_key = generate_ecc_keys(args.curve_type, args.save_keys)
    print("Private Key:\n", private_key.export_key(format='PEM'))
    print("\nPublic Key:\n", public_key.export_key(format='PEM'))
