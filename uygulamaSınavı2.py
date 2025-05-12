import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def caesar_decrypt(ciphertext, shift=7):
    decrypted = ''
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        elif 'a' <= char <= 'z':
            decrypted += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted += char
    return decrypted

def ascii_minus_one(s):
    return ''.join(chr(ord(c) - 1) for c in s)

def aes_decrypt_ecb(ciphertext_bytes, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext_bytes)
    return unpad(decrypted, AES.block_size).decode()

# 1. Base64 decode
cipher_b64 = "yNjMHmg6dB9czTMOA2D6nA=="
cipher_bytes = base64.b64decode(cipher_b64)
print("1. After Base64 decode:", cipher_bytes)

# 2. AES decrypt
key = b'Secret16ByteKey!'
try:
    step2 = aes_decrypt_ecb(cipher_bytes, key)
    print("2. After AES decryption:", step2)
except Exception as e:
    print("AES decryption failed:", e)
    exit()

# 3. Reverse
step3 = step2[::-1]
print("3. After reversing:", step3)

# 4. Caesar -7
step4 = caesar_decrypt(step3)
print("4. After Caesar decryption:", step4)

# 5. ASCII -1
step5 = ascii_minus_one(step4)
print("5. After ASCII -1:", step5)

print("Original message:", step5)
