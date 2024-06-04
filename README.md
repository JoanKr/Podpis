# Podpis Cyfrowy z Wykorzystaniem Mapy Chaotycznej i RSA

Ten projekt demonstruje użycie mapy chaotycznej do generowania losowych danych oraz wykorzystanie algorytmu RSA do tworzenia i weryfikacji podpisów cyfrowych.

## Struktura Projektu

- `chaotic_data_generator.py`: Skrypt generujący losowe dane przy użyciu mapy chaotycznej.
- `rsa_signature.py`: Skrypt do generowania kluczy RSA, podpisywania wiadomości i weryfikacji podpisu cyfrowego.
- `quantized_values.npy`: Plik generowany przez `chaotic_data_generator.py`, zawierający losowe dane.

## Wymagania

- Python 3
- Biblioteki: `cryptography`, `numpy`, `matplotlib`, `pynput`

## Instalacja

1. **Klonuj repozytorium:**

    ```bash
    git clone https://github.com/JoanKr/Podpis
    cd Podpis
    ```

2. **Stwórz wirtualne środowisko:**

    ```bash
    python3 -m venv myenv
    ```

3. **Aktywuj wirtualne środowisko:**

    Na macOS/Linux:

    ```bash
    source myenv/bin/activate
    ```

    Na Windows:

    ```bash
    myenv\Scripts\activate
    ```

4. **Zainstaluj wymagane biblioteki:**

    ```bash
    pip install cryptography numpy matplotlib pynput pytest
    ```
