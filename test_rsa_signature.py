import pytest
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes, serialization

@pytest.fixture
def load_keys_and_data():
    # Wczytanie klucza publicznego z pliku
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Wczytanie wiadomości z pliku tekstowego
    with open("message.txt", "rb") as f:
        received_message = f.read()

    # Wczytanie podpisu z pliku
    with open("signature.sig", "rb") as f:
        received_signature = f.read()

    # Wczytanie skrótu wiadomości z pliku
    with open("message_hash.txt", "rb") as f:
        original_message_hash = f.read()

    # Zwrócenie wszystkich załadowanych danych jako krotki
    return public_key, received_message, received_signature, original_message_hash

def verify_signature(message, signature, public_key):
    # Obliczenie skrótu (hash) z otrzymanej wiadomości
    digest = hashes.Hash(hashes.SHA3_256())
    digest.update(message)
    received_message_hash = digest.finalize()

    try:
        # Weryfikacja podpisu za pomocą klucza publicznego i obliczonego skrótu wiadomości
        public_key.verify(
            signature,
            received_message_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Verification failed! {e}")
        return False

def test_valid_signature(load_keys_and_data):
    public_key, received_message, received_signature, original_message_hash = load_keys_and_data
    print("\nTestujemy poprawny przypadek: prawidłowy klucz publiczny, prawidłowa wiadomość.")
    # Sprawdzenie, czy podpis jest prawidłowy przy użyciu prawidłowego klucza publicznego i wiadomości
    if verify_signature(received_message, received_signature, public_key):
        print("Podpis jest prawidłowy.")
    else:
        print("Podpis jest nieprawidłowy.")
    assert verify_signature(received_message, received_signature, public_key) == True

def test_invalid_signature(load_keys_and_data):
    public_key, received_message, received_signature, original_message_hash = load_keys_and_data
    # Generowanie nowej pary kluczy RSA i użycie innego klucza publicznego do weryfikacji
    other_public_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    ).public_key()
    print("\nTestujemy nieprawidłowy przypadek: nieprawidłowy klucz publiczny.")
    # Sprawdzenie, czy podpis jest nieprawidłowy przy użyciu innego klucza publicznego
    if verify_signature(received_message, received_signature, other_public_key):
        print("Podpis jest prawidłowy, ale nie powinien być.")
    else:
        print("Podpis jest nieprawidłowy. Powód: użyto innego klucza publicznego.")
    assert verify_signature(received_message, received_signature, other_public_key) == False

def test_modified_message(load_keys_and_data):
    public_key, received_message, received_signature, original_message_hash = load_keys_and_data
    # Modyfikacja oryginalnej wiadomości
    modified_message = b"To jest inna wiadomosc."
    print("\nTestujemy nieprawidłowy przypadek: zmodyfikowana wiadomość.")
    # Sprawdzenie, czy podpis jest nieprawidłowy przy użyciu zmodyfikowanej wiadomości
    if verify_signature(modified_message, received_signature, public_key):
        print("Podpis jest prawidłowy, ale nie powinien być.")
    else:
        print("Podpis jest nieprawidłowy. Powód: wiadomość została zmodyfikowana.")
    assert verify_signature(modified_message, received_signature, public_key) == False
