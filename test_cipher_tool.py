#!/usr/bin/env python3
"""
Unit tests for DecodeLabs Cybersecurity Project 2: Basic Encryption & Decryption
"""

import unittest
from cipher_tool import caesar_encrypt, caesar_decrypt, vigenere_encrypt, vigenere_decrypt

class TestCipherTool(unittest.TestCase):
    
    def test_caesar_basic(self):
        # Test standard encryption/decryption
        text = "Hello World"
        shift = 3
        
        encrypted = caesar_encrypt(text, shift)
        self.assertEqual(encrypted, "Khoor Zruog")
        
        decrypted = caesar_decrypt(encrypted, shift)
        self.assertEqual(decrypted, text)
        
    def test_caesar_edge_cases(self):
        # Step 8: Spaces, numbers, punctuation remain unchanged
        text = "Hello World 123!@#"
        shift = 5
        
        encrypted = caesar_encrypt(text, shift)
        self.assertEqual(encrypted, "Mjqqt Btwqi 123!@#")
        
        decrypted = caesar_decrypt(encrypted, shift)
        self.assertEqual(decrypted, text)
        
        # Test shift = 0
        self.assertEqual(caesar_encrypt(text, 0), text)
        self.assertEqual(caesar_decrypt(text, 0), text)
        
        # Test shift = 26 (should be same as 0 due to modulo 26)
        self.assertEqual(caesar_encrypt(text, 26), text)
        self.assertEqual(caesar_decrypt(text, 26), text)
        
        # Test negative shifts
        self.assertEqual(caesar_encrypt("ABC", -1), "ZAB")
        self.assertEqual(caesar_decrypt("ZAB", -1), "ABC")
        
        # Test very large shifts
        self.assertEqual(caesar_encrypt("ABC", 54), caesar_encrypt("ABC", 2))
        
    def test_vigenere_basic(self):
        # Test Vigenère cipher encryption/decryption
        text = "ATTACKATDAWN"
        key = "LEMON"
        
        encrypted = vigenere_encrypt(text, key)
        self.assertEqual(encrypted, "LXFOPVEFRNHR")
        
        decrypted = vigenere_decrypt(encrypted, key)
        self.assertEqual(decrypted, text)
        
    def test_vigenere_edge_cases(self):
        # Spaces and non-alphabetic chars should remain unchanged
        text = "Hello, World! 123"
        key = "key"
        
        encrypted = vigenere_encrypt(text, key)
        # H(7) + k(10) = R(17)
        # e(4) + e(4) = i(8)
        # l(11) + y(24) = j(9)
        # l(11) + k(10) = v(21)
        # o(14) + e(4) = s(18)
        # , space
        # W(22) + y(24) = U(20)
        # o(14) + k(10) = y(24)
        # r(17) + e(4) = v(21)
        # l(11) + y(24) = j(9)
        # d(3) + k(10) = n(13)
        self.assertEqual(encrypted, "Rijvs, Uyvjn! 123")
        
        decrypted = vigenere_decrypt(encrypted, key)
        self.assertEqual(decrypted, text)
        
        # Case insensitive key test
        encrypted_upper_key = vigenere_encrypt(text, "KEY")
        self.assertEqual(encrypted_upper_key, encrypted)

if __name__ == "__main__":
    unittest.main()
