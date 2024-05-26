from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import numpy as np

# Wczytaj dane z pliku
quantized_values = np.load('quantized_values.npy')

# Generowanie kluczy RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Wiadomość do podpisania
message = "To jest przykładowa wiadomość do podpisania.".encode('ascii')

# Wyliczenie skrótu wiadomości
digest = hashes.Hash(hashes.SHA3_256())
digest.update(message)
message_hash = digest.finalize()

# Szyfrowanie skrótu kluczem prywatnym (tworzenie podpisu cyfrowego)
signature = private_key.sign(
    message_hash,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Weryfikacja podpisu kluczem publicznym
def verify_signature(message, signature, public_key):
    # Wyliczenie skrótu wiadomości
    digest = hashes.Hash(hashes.SHA3_256())
    digest.update(message)
    message_hash = digest.finalize()

    try:
        public_key.verify(
            signature,
            message_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Podpis jest prawidłowy.")
    except:
        print("Podpis jest nieprawidłowy.")

# Weryfikacja podpisu
verify_signature(message, signature, public_key)
