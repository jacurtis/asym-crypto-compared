import argparse
import json
import random
from math import pow

a = random.randint(2, 10)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)


# Generating large random numbers
def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)

    return key


# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c


def generate_keys(save_keys=True):
    msg = 'encryption'
    print("Original Message :", msg)

    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)

    key = gen_key(q)  # Private key for receiver
    h = power(g, key, q)
    print("q used : ", q)
    print("g used : ", g)
    print("g^a used : ", h)
    print("key used : ", key)

    data = {
        'q': q,
        'g': g,
        'h': h,
        'key': key
    }

    with open('elgamal_keys.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate ElGamal keys.')
    parser.add_argument('--save_keys', type=bool, default=False, help='Whether to save the keys to files.')
    args = parser.parse_args()

    generate_keys(args.save_keys)