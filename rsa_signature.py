import numpy as np
import secrets
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# Wczytanie danych z pliku quantized_values.npy
quantized_values = np.load('quantized_values.npy')

# Użycie wartości z pliku jako entropii do seeda generatora losowego
# Przekształcamy dane na ciąg bajtów
seed_data = quantized_values.tobytes()

# Ustawienie seeda dla generatora losowego
secrets_generator = secrets.SystemRandom()
seed = int.from_bytes(seed_data[:16], byteorder='big')  # używamy pierwszych 16 bajtów
secrets_generator.seed(seed)

# Generowanie kluczy RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=secrets_generator
)
public_key = private_key.public_key()

# Zapisanie kluczy do plików
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# Wczytanie wiadomości z pliku tekstowego
with open("message.txt", "rb") as f:
    message = f.read()

# Wyliczenie skrótu wiadomości
digest = hashes.Hash(hashes.SHA3_256())
digest.update(message)
message_hash = digest.finalize()

# Zapisanie skrótu do pliku
with open("message_hash.txt", "wb") as f:
    f.write(message_hash)

# Szyfrowanie skrótu kluczem prywatnym (tworzenie podpisu cyfrowego)
signature = private_key.sign(
    message_hash,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Zapisanie podpisu do pliku
with open("signature.sig", "wb") as f:
    f.write(signature)


# Zapisanie kluczy do plików
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# Wczytanie wiadomości z pliku tekstowego
with open("message.txt", "rb") as f:
    message = f.read()

# Wyliczenie skrótu wiadomości
digest = hashes.Hash(hashes.SHA3_256())
digest.update(message)
message_hash = digest.finalize()

# Zapisanie skrótu do pliku
with open("message_hash.txt", "wb") as f:
    f.write(message_hash)

# Szyfrowanie skrótu kluczem prywatnym (tworzenie podpisu cyfrowego)
signature = private_key.sign(
    message_hash,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Zapisanie podpisu do pliku
with open("signature.sig", "wb") as f:
    f.write(signature)
