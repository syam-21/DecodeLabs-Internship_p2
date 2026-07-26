# Cipher Tool - Basic Encryption & Decryption

A Python-based encryption and decryption tool implementing classic cipher algorithms for cybersecurity learning and practice.

## Project Overview

This project is part of DecodeLabs Cybersecurity Internship Program (Project 2). It provides implementations of two fundamental encryption algorithms:

1. **Caesar Cipher** - A substitution cipher that shifts alphabetic characters by a fixed amount
2. **Vigenère Cipher** - A polyalphabetic substitution cipher using a repeating keyword

## Features

- ✅ Caesar Cipher encryption and decryption
- ✅ Vigenère Cipher encryption and decryption
- ✅ Preserves spaces, numbers, and punctuation
- ✅ Case-sensitive character handling
- ✅ Comprehensive unit tests
- ✅ Support for edge cases (negative shifts, large shifts, etc.)

## Installation

No external dependencies required. This project uses only Python's standard library.

```bash
# Clone or download the repository
cd Cyber_InternShip/CYBER_P2

# Verify Python 3 is installed
python3 --version
```

## Usage

### Caesar Cipher

```python
from cipher_tool import caesar_encrypt, caesar_decrypt

# Encryption
plaintext = "Hello World"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
print(ciphertext)  # Output: Khoor Zruog

# Decryption
decrypted = caesar_decrypt(ciphertext, shift)
print(decrypted)   # Output: Hello World
```

### Vigenère Cipher

```python
from cipher_tool import vigenere_encrypt, vigenere_decrypt

# Encryption
plaintext = "ATTACKATDAWN"
key = "LEMON"
ciphertext = vigenere_encrypt(plaintext, key)
print(ciphertext)  # Output: LXFOPVEFRNHR

# Decryption
decrypted = vigenere_decrypt(ciphertext, key)
print(decrypted)   # Output: ATTACKATDAWN
```

## Algorithm Details

### Caesar Cipher
- **Encryption**: `En(x) = (x + shift) % 26`
- **Decryption**: `Dn(x) = (x - shift) % 26`
- Only alphabetic characters are shifted
- Case is preserved (A-Z and a-z handled separately)

### Vigenère Cipher
- Uses a repeating key to determine shift values for each character
- Key is cycled through only alphabetic characters in the plaintext
- Non-alphabetic characters are preserved and don't consume key positions
- Case-insensitive key handling with case preservation in output

## Testing

Run the unit tests to verify functionality:

```bash
python3 test_cipher_tool.py
```

### Test Coverage

- Caesar Cipher basic encryption/decryption
- Caesar Cipher edge cases (shift of 0, 26, negative shifts, large shifts)
- Vigenère Cipher basic encryption/decryption
- Vigenère Cipher with spaces, punctuation, and numbers
- Case sensitivity and case preservation
- Empty key validation

## Project Files

- **cipher_tool.py** - Main implementation of encryption/decryption functions
- **test_cipher_tool.py** - Comprehensive unit tests
- **README.md** - This file

## Security Note

⚠️ **Important**: These classic ciphers (Caesar and Vigenère) are not secure for real-world use. They are vulnerable to various cryptanalysis techniques and should only be used for educational purposes.

For production systems, use modern cryptographic libraries like:
- `cryptography` package
- `PyCryptodome` package
- Built-in `hashlib` and `hmac` modules

## Author

DecodeLabs Cybersecurity Analyst

## License

Educational Use Only
