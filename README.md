# Vigenère Cipher in Python

## Project Description

This project implements the Vigenère cipher in Python for an Information Security assignment. It supports two encryption modes: basic alphabetic mode and advanced printable ASCII mode.

## Features

- **Basic Mode:** Encrypts and decrypts English letters using the Vigenère cipher.
- **Advanced ASCII Mode:** Encrypts and decrypts printable ASCII characters, including letters, numbers, spaces, and punctuation.
- **Encryption and Decryption:** Uses a repeating key for both operations.
- **Input Validation:** Checks keys, messages, and menu selections.
- **Interactive Menu:** Allows users to choose a mode, select an operation, and exit the program.
- **Case Preservation:** Basic mode preserves uppercase and lowercase letters.
- **GitHub Version Control:** The project includes meaningful commits documenting implementation, documentation, and menu improvements.

## Requirements

- Python 3
- No external Python libraries are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python main.py
```

4. Choose a mode:
   - Enter `1` for Basic Mode.
   - Enter `2` for Advanced ASCII Mode.
   - Enter `3` to exit.
5. Enter your message and encryption key.
6. Choose `E` to encrypt or `D` to decrypt.

## How the Algorithm Works

### Basic Mode

The basic mode uses the 26 English alphabet letters, assigning each letter a position from 0 to 25.

Encryption formula:

`C = (P + K) mod 26`

Decryption formula:

`P = (C - K) mod 26`

Where:
- `P` is the plaintext letter position.
- `C` is the ciphertext letter position.
- `K` is the key letter position.
- `mod 26` keeps the result within the alphabet.

Spaces, numbers, and punctuation are preserved without encryption in this mode.

### Advanced ASCII Mode

The advanced mode supports printable ASCII characters with codes from 32 to 126, giving 95 possible characters.

The program subtracts 32 from each character's code to obtain a position from 0 to 94. It then performs the Vigenère calculation using modulo 95 and adds 32 to convert the result back to a printable character.

Encryption formula:

`C = (P + K) mod 95`

Decryption formula:

`P = (C - K) mod 95`

The ASCII mode encrypts spaces, numbers, and punctuation as well as letters.

## Testing

The program can be tested by encrypting a message and then decrypting the resulting ciphertext using the same key. Successful decryption should reproduce the original message.

Example:

- Original message: `Hello World!`
- Key: `KEY`
- Basic encrypted result: `Rijvs Uyvjn!`
- Decrypted result: `Hello World!`

## Limitations

The Vigenère cipher is a classical educational cipher and is not suitable for protecting real confidential information.

## Purpose

The purpose of this project is to demonstrate classical encryption, decryption, repeating keys, modular arithmetic, ASCII character processing, and input validation.
