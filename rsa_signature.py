from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import numpy as np

# Wczytaj dane z pliku
quantized_values = np.load('quantized_values.npy')

# Generowanie kluczy RSA (pierwsza para)
private_key_1 = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key_1 = private_key_1.public_key()

# Generowanie kluczy RSA (druga para, do testów)
private_key_2 = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key_2 = private_key_2.public_key()

# Wiadomość do podpisania
message = "To jest przykładowa wiadomość do podpisania.".encode('utf-8')

# Wyliczenie skrótu wiadomości
digest = hashes.Hash(hashes.SHA3_256())
digest.update(message)
message_hash = digest.finalize()

# Szyfrowanie skrótu kluczem prywatnym (tworzenie podpisu cyfrowego)
signature = private_key_1.sign(
    message_hash,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Funkcja weryfikująca podpis
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

# Weryfikacja podpisu poprawnym kluczem publicznym
print("Weryfikacja poprawnym kluczem publicznym:")
verify_signature(message, signature, public_key_1)

# Weryfikacja podpisu innym kluczem publicznym
print("\nWeryfikacja innym kluczem publicznym:")
verify_signature(message, signature, public_key_2)

# Weryfikacja podpisu poprawnym kluczem publicznym ale inną wiadomością
print("\nWeryfikacja poprawnym kluczem publicznym, ale inną wiadomością:")
different_message = "To jest inna wiadomość.".encode('utf-8')
verify_signature(different_message, signature, public_key_1)
