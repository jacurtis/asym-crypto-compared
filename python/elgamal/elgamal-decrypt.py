import argparse
import json


def load_keys(filename='elgamal_keys.json'):
    with open('elgamal_keys.json', 'r') as f:
        data = json.load(f)
    q = data['q']
    g = data['g']
    h = data['h']
    key = data['key']
    return q, g, h, key


def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c


# def encrypt(msg, q, h, g, k):
#     ciphertext = []
#
#     # k = gen_key(q)  # Private key for sender
#     s = power(h, k, q)
#     p = power(g, k, q)
#
#     for i in range(0, len(msg)):
#         en_msg.append(msg[i])
#
#     # print("g^k used : ", p)
#     # print("g^ak used : ", s)
#     for i in range(0, len(ciphertext)):
#         ciphertext[i] = s * ord(ciphertext[i])
#
#     return ciphertext, p


def decrypt(ciphertext, p, key, q):
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(ciphertext)):
        dr_msg.append(chr(int(ciphertext[i] / h)))

    return dr_msg


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decrypt Message with ElGamal')
    parser.add_argument('message', type=str, help='The message to encrypt.')
    parser.add_argument('--load_keys', type=bool, default=True, help='Whether to load the keys from files.')
    parser.add_argument('-q', type=int, default=0, help='The q value to use.')
    parser.add_argument('-p', type=int, default=0, help='The g value to use.')
    parser.add_argument('-key', type=int, default=0, help='The key value to use.')
    args = parser.parse_args()

    q = args.q
    key = args.key
    p = args.p
    if args.load_keys:
        q, _, _, key = load_keys()

    ciphertext_arr = json.loads(args.message)

    # ciphertext, p = encrypt(args.message, q, h, g, k=key)
    # print("Encrypted Message :", ciphertext)
    plaintext = decrypt(ciphertext_arr, p, key, q)
    message = ''.join(plaintext)
    print(message)
    # print("Decrypted Message :", dmsg);