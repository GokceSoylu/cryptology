import base64
from Crypto.Cipher import AES
import itertools

encrypted_message_b64 = "yNjMHmg6dB9czTMOA2D6nA=="
aes_key = b'Secret16ByteKey'

def reverse_string(text):
    return text[::-1]

def caesar_decrypt(text, shift):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
        else:
            result += char
    return result

def ascii_minus_one(text):
    result = ''
    for char in text:
        result += chr(ord(char) - 1)
    return result

def aes_decrypt(ciphertext_b64, key):
    ciphertext = base64.b64decode(ciphertext_b64)
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    padding_length = plaintext[-1]
    return plaintext[:-padding_length].decode('utf-8')

# Decryption Attempts (Finding the right order)
possible_orders = list(itertools.permutations([
    "base64", "aes", "caesar", "reverse", "ascii"
]))

for order in possible_orders:
    decrypted_text = encrypted_message_b64
    steps = {} # Store intermediate results

    for step in order:
        if step == "base64":
            try:
                decrypted_text = base64.b64decode(decrypted_text).decode('utf-8')
                steps[step] = decrypted_text
            except:
                break # Invalid order
        elif step == "aes":
            try:
                decrypted_text = aes_decrypt(decrypted_text, aes_key)
                steps[step] = decrypted_text
            except:
                break # Invalid order
        elif step == "caesar":
            decrypted_text = caesar_decrypt(decrypted_text, 7)
            steps[step] = decrypted_text
        elif step == "reverse":
            decrypted_text = reverse_string(decrypted_text)
            steps[step] = decrypted_text
        elif step == "ascii":
            decrypted_text = ascii_minus_one(decrypted_text)
            steps[step] = decrypted_text
    else: # If the loop completes without a break, we found a valid order
        print("Decryption Order:", order)
        for desc, text in steps.items():
            print(f"After {desc} decryption: {text}")
        print("Original message:", decrypted_text)
        break