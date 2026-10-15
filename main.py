
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ASCII_START = 32
ASCII_SIZE = 95


def is_valid_basic_key(key):
    return bool(key) and key.isascii() and key.isalpha()


def is_valid_ascii_key(key):
    return (
        bool(key.strip())
        and all(ASCII_START <= ord(char) <= 126 for char in key)
    )


def is_printable_ascii(message):
    return all(ASCII_START <= ord(char) <= 126 for char in message)


def encrypt_basic(message, key):
    result = ""
    key = key.upper()
    key_position = 0

    for char in message:
        if char.upper() in ALPHABET:
            plain_position = ALPHABET.index(char.upper())
            key_position_value = ALPHABET.index(
                key[key_position % len(key)]
            )

            encrypted_position = (
                plain_position + key_position_value
            ) % 26

            encrypted_char = ALPHABET[encrypted_position]

            if char.islower():
                encrypted_char = encrypted_char.lower()

            result += encrypted_char
            key_position += 1
        else:
            result += char

    return result


def decrypt_basic(message, key):
    result = ""
    key = key.upper()
    key_position = 0

    for char in message:
        if char.upper() in ALPHABET:
            cipher_position = ALPHABET.index(char.upper())
            key_position_value = ALPHABET.index(
                key[key_position % len(key)]
            )

            decrypted_position = (
                cipher_position - key_position_value
            ) % 26

            decrypted_char = ALPHABET[decrypted_position]

            if char.islower():
                decrypted_char = decrypted_char.lower()

            result += decrypted_char
            key_position += 1
        else:
            result += char

    return result


def encrypt_ascii_character(char, key_char):
    plain_position = ord(char) - ASCII_START
    key_position = ord(key_char) - ASCII_START

    encrypted_position = (
        plain_position + key_position
    ) % ASCII_SIZE

    return chr(encrypted_position + ASCII_START)


def decrypt_ascii_character(char, key_char):
    cipher_position = ord(char) - ASCII_START
    key_position = ord(key_char) - ASCII_START

    decrypted_position = (
        cipher_position - key_position
    ) % ASCII_SIZE

    return chr(decrypted_position + ASCII_START)


def encrypt_ascii(message, key):
    result = ""

    for i, char in enumerate(message):
        key_char = key[i % len(key)]
        result += encrypt_ascii_character(char, key_char)

    return result


def decrypt_ascii(message, key):
    result = ""

    for i, char in enumerate(message):
        key_char = key[i % len(key)]
        result += decrypt_ascii_character(char, key_char)

    return result


def run_basic():
    message = input("Enter your message: ")
    key = input("Enter an English-letter key: ").strip()

    if not is_valid_basic_key(key):
        print("Error: The key must contain English letters only.")
        return

    operation = input("Enter E to encrypt or D to decrypt: ").strip().upper()

    if operation == "E":
        print("Result:", encrypt_basic(message, key))
    elif operation == "D":
        print("Result:", decrypt_basic(message, key))
    else:
        print("Error: Choose E or D.")


def run_ascii():
    message = input("Enter your printable ASCII message: ")
    key = input("Enter a printable ASCII key: ")

    if not is_valid_ascii_key(key):
        print("Error: Enter a non-empty printable ASCII key.")
        return

    if not is_printable_ascii(message):
        print("Error: The message must contain printable ASCII characters only.")
        return

    operation = input("Enter E to encrypt or D to decrypt: ").strip().upper()

    if operation == "E":
        print("Result:", encrypt_ascii(message, key))
    elif operation == "D":
        print("Result:", decrypt_ascii(message, key))
    else:
        print("Error: Choose E or D.")


def main():
    print("=== Vigenere Cipher ===")
    print("1. Basic mode (English letters)")
    print("2. Advanced mode (printable ASCII)")

    choice = input("Choose a mode (1 or 2): ").strip()

    if choice == "1":
        run_basic()
    elif choice == "2":
        run_ascii()
    else:
        print("Error: Choose 1 or 2.")


if __name__ == "__main__":
    main()
