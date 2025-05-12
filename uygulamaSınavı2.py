import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def caesar_decrypt(text, shift=7):
    result = ''
    for c in text:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - shift - ord('a')) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - shift - ord('A')) % 26 + ord('A'))
        else:
            result += c
    return result

def ascii_minus_one(text):
    return ''.join(chr(ord(c) - 1) for c in text)

# Step 1: Base64 decode
cipher_b64 = "yNjMHmg6dB9czTMOA2D6nA=="
cipher_bytes = base64.b64decode(cipher_b64)
print("1. After Base64 decode:", cipher_bytes)

# Step 2: AES decrypt
key = b'Secret16ByteKey'
cipher = AES.new(key, AES.MODE_ECB)
decrypted_bytes = cipher.decrypt(cipher_bytes)
try:
    unpadded = unpad(decrypted_bytes, AES.block_size)
except ValueError as e:
    print("Padding error:", e)
    exit(1)
print("2. After AES decryption:", unpadded)

# Step 3: ASCII -1
step3 = ascii_minus_one(unpadded.decode('latin1'))  # keep latin1 to preserve full byte range
print("3. After ASCII -1:", step3)

# Step 4: Caesar decrypt
step4 = caesar_decrypt(step3)
print("4. After Caesar decryption:", step4)

# Step 5: Reverse
original_message = step4[::-1]
print("Original message:", original_message)
