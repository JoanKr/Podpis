
# Podpis Cyfrowy z Wykorzystaniem Mapy Chaotycznej i RSA

Ten projekt demonstruje użycie mapy chaotycznej do generowania losowych danych oraz wykorzystanie algorytmu RSA do tworzenia i weryfikacji podpisów cyfrowych.



## Struktura Projektu


- `chaotic_data_generator.py`: Skrypt generujący losowe dane przy użyciu mapy chaotycznej.
- `rsa_signature.py`: Skrypt do generowania kluczy RSA, podpisywania wiadomości i weryfikacji podpisu cyfrowego.
- `test_rsa_signature.py`: Skrypt testowy wykorzystujący `pytest` do weryfikacji podpisu cyfrowego.
- `quantized_values.npy`: Plik generowany przez `chaotic_data_generator.py`, zawierający losowe dane.
- `private_key.pem`: Wygenerowany klucz prywatny RSA.
- `public_key.pem`: Wygenerowany klucz publiczny RSA.
- `message.txt`: Plik tekstowy z wiadomością do podpisania.
- `message_hash.txt`: Skrót wiadomości wygenerowany przy użyciu SHA3-256.
- `signature.sig`: Podpis cyfrowy wiadomości.


## Wymagania
- Python 3
- Biblioteki: `cryptography`, `numpy`, `matplotlib`, `pynput`, `pytest`
## Instalacja
1. **Klonowanie repozytorium:**

    ```bash
    git clone https://github.com/JoanKr/Podpis
    cd Podpis
    ```

2. **Stworzenie wirtualnego środowiska:**

    ```bash
    python3 -m venv myenv
    ```

3. **Aktywacja wirtualnego środowiska:**

    Na macOS/Linux:

    ```bash
    source myenv/bin/activate
    ```

    Na Windows:

    ```bash
    myenv\Scripts\activate
    ```

4. **Instalacja wymaganych bibliotek:**

    ```bash
    pip install cryptography numpy matplotlib pynput pytest
    ```
## Użycie
### 1. Generowanie Losowych Danych

Uruchom skrypt `chaotic_data_generator.py`, aby wygenerować losowe dane:

```bash
python chaotic_data_generator.py
```
Skrypt wygeneruje plik quantized_values.npy, który zawiera losowe dane.

### 2. Podpisywanie i Weryfikacja Wiadomości
Uruchom skrypt rsa_signature.py, aby wygenerować klucze RSA, podpisać wiadomość i zweryfikować podpis:
```bash
python rsa_signature.py
```
### 3. Testowanie Poprawności Podpisu
Uruchom testy automatyczne za pomocą pytest:
```bash
pytest -s test_rsa_signature.py
```

## 4. Wyniki
Skrypt test_rsa_signature.py wykonuje następujące testy:

### 1. Poprawna weryfikacja: 
Sprawdzanie podpisu przy użyciu tej samej pary kluczy, która została użyta do podpisania wiadomości.
### 2. Niepoprawny klucz publiczny: 
Próba weryfikacji podpisu przy użyciu innego klucza publicznego.
### 3. Zmodyfikowana wiadomość: 
Próba weryfikacji podpisu przy użyciu zmodyfikowanej wiadomości.

Każdy test wyświetla odpowiedni komunikat na początku, wyjaśniając, który przypadek jest testowany, oraz szczegółowy powód, dlaczego podpis jest nieprawidłowy, jeśli test nie przejdzie pomyślnie.

### Oczekiwane wyniki:

Pierwsza weryfikacja powinna zakończyć się sukcesem ("Podpis jest prawidłowy.").

Druga i trzecia weryfikacja powinny zakończyć się niepowodzeniem z odpowiednimi komunikatami o błędzie.

## Autor

- [Joanna Krajewska](https://www.github.com/JoanKr)

