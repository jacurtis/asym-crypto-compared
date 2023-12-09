from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils

# Generate an ECC key pair
private_key = ec.generate_private_key(ec.SECP256R1())  # You can choose different curves like SECP256R1 or SECP384R1

# Serialize the public key to PEM format
public_key = private_key.public_key()
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Message to be signed
message = b"Hello, ECC!"

# Sign the message with the private key
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# Verify the signature using the public key
try:
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    print("Signature is valid.")
except utils.InvalidSignature:
    print("Signature is not valid.")
