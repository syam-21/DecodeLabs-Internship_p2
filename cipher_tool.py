#!/usr/bin/env python3
"""
DecodeLabs Cybersecurity Project 2: Basic Encryption & Decryption
Author: Cybersecurity Analyst
"""

import sys

def caesar_encrypt(plaintext: str, shift: int) -> str:
    """
    Encrypts plaintext using the Caesar Cipher.
    Formula: En(x) = (x + shift) % 26
    Only alphabetic characters are shifted. Spaces, numbers, and punctuation remain unchanged.
    """
    encrypted_chars = []
    for char in plaintext:
        if char.isupper():
            # Shift within A-Z (ASCII 65 - 90)
            x = ord(char) - ord('A')
            en_x = (x + shift) % 26
            encrypted_chars.append(chr(en_x + ord('A')))
        elif char.islower():
            # Shift within a-z (ASCII 97 - 122)
            x = ord(char) - ord('a')
            en_x = (x + shift) % 26
            encrypted_chars.append(chr(en_x + ord('a')))
        else:
            # Step 8: Spaces, numbers, punctuation remain unchanged
            encrypted_chars.append(char)
    return "".join(encrypted_chars)

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypts ciphertext using the Caesar Cipher.
    Formula: Dn(x) = (x - shift) % 26
    Only alphabetic characters are shifted. Spaces, numbers, and punctuation remain unchanged.
    """
    # Decrypting is equivalent to shifting in the opposite direction
    return caesar_encrypt(ciphertext, -shift)

def vigenere_encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts plaintext using the Vigenère Cipher.
    The key is repeated/cycled over the alphabetic characters of the plaintext.
    """
    if not key:
        return plaintext
    
    # Standardize the key to lowercase shift integers
    key_shifts = [ord(char.lower()) - ord('a') for char in key if char.isalpha()]
    if not key_shifts:
        raise ValueError("Vigenère key must contain at least one alphabetic character.")
        
    encrypted_chars = []
    key_idx = 0
    key_len = len(key_shifts)
    
    for char in plaintext:
        if char.isalpha():
            shift = key_shifts[key_idx % key_len]
            if char.isupper():
                x = ord(char) - ord('A')
                en_x = (x + shift) % 26
                encrypted_chars.append(chr(en_x + ord('A')))
            else:
                x = ord(char) - ord('a')
                en_x = (x + shift) % 26
                encrypted_chars.append(chr(en_x + ord('a')))
            key_idx += 1
        else:
            encrypted_chars.append(char)
            
    return "".join(encrypted_chars)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts ciphertext using the Vigenère Cipher.
    """
    if not key:
        return ciphertext
        
    # Standardize the key to lowercase negative shift integers for decryption
    key_shifts = [-(ord(char.lower()) - ord('a')) for char in key if char.isalpha()]
    if not key_shifts:
        raise ValueError("Vigenère key must contain at least one alphabetic character.")
        
    decrypted_chars = []
    key_idx = 0
    key_len = len(key_shifts)
    
    for char in ciphertext:
        if char.isalpha():
            shift = key_shifts[key_idx % key_len]
            if char.isupper():
                x = ord(char) - ord('A')
                en_x = (x + shift) % 26
                decrypted_chars.append(chr(en_x + ord('A')))
            else:
                x = ord(char) - ord('a')
                en_x = (x + shift) % 26
                decrypted_chars.append(chr(en_x + ord('a')))
            key_idx += 1
        else:
            decrypted_chars.append(char)
            
    return "".join(decrypted_chars)

def print_header(title: str):
    print("=" * 60)
    print(f" {title} ".center(60, "="))
    print("=" * 60)

def main():
    print_header("DecodeLabs: Basic Encryption & Decryption Tool")
    
    while True:
        print("\nChoose an option:")
        print("1. Caesar Cipher (Standard Encryption/Decryption)")
        print("2. Vigenère Cipher (Advanced Challenge)")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        if choice == '3':
            print("\nExiting DecodeLabs Cipher Tool. Stay secure!")
            break
        elif choice == '1':
            print_header("Caesar Cipher Mode")
            # Step 1: Take user input as plaintext
            plaintext = input("Enter plaintext: ")
            
            # Step 10: Allow user to choose custom shift key
            while True:
                try:
                    key_input = input("Enter shift key (integer): ").strip()
                    shift = int(key_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer for the shift key.")
            
            # Step 2-5: Encrypt and Display
            ciphertext = caesar_encrypt(plaintext, shift)
            print(f"\n[+] Encrypted Text: {ciphertext}")
            
            # Step 6-7: Decrypt and Display
            decrypted = caesar_decrypt(ciphertext, shift)
            print(f"[+] Decrypted Text: {decrypted}")
            
            # Step 9: Validate
            if decrypted == plaintext:
                print("[✔] Validation Success: Decrypted text matches original plaintext.")
            else:
                print("[❌] Validation Failure: Decrypted text does not match original plaintext!")
                
        elif choice == '2':
            print_header("Vigenère Cipher Mode")
            plaintext = input("Enter plaintext: ")
            
            while True:
                key = input("Enter keyword (letters only): ").strip()
                if any(char.isalpha() for char in key):
                    break
                print("Invalid keyword. Key must contain at least one alphabetic character.")
            
            # Encrypt and Display
            ciphertext = vigenere_encrypt(plaintext, key)
            print(f"\n[+] Encrypted Text: {ciphertext}")
            
            # Decrypt and Display
            decrypted = vigenere_decrypt(ciphertext, key)
            print(f"[+] Decrypted Text: {decrypted}")
            
            # Validate
            if decrypted == plaintext:
                print("[✔] Validation Success: Decrypted text matches original plaintext.")
            else:
                print("[❌] Validation Failure: Decrypted text does not match original plaintext!")
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user. Exiting.")
        sys.exit(0)
