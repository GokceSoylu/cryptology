import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def caesar_decrypt(text, shift=7):
    result = ''
    for c in text:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - shift - 97) % 26 + 97)
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - shift - 65) % 26 + 65)
        else:
            result += c
    return result

def ascii_minus_one(text):
    return ''.join(chr(ord(c) - 1) for c in text)

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted, AES.block_size).decode('utf-8')

# === STEP 1: Base64 decode ===
cipher_b64 = "yNjMHmg6dB9czTMOA2D6nA=="
cipher_bytes = base64.b64decode(cipher_b64)
print("1. After Base64 decode:", cipher_bytes)

# === STEP 2: AES decrypt ===
key = b'Secret16ByteKey!'
try:
    step2 = aes_decrypt(cipher_bytes, key)
    print("2. After AES decryption:", step2)
except Exception as e:
    print("AES decryption failed:", e)
    exit()

# === STEP 3: Reverse ===
step3 = step2[::-1]
print("3. After reversing:", step3)

# === STEP 4: Caesar -7 ===
step4 = caesar_decrypt(step3)
print("4. After Caesar decryption:", step4)

# === STEP 5: ASCII -1 ===
step5 = ascii_minus_one(step4)
print("5. After ASCII -1:", step5)

# === Final Output ===
print("Original message:", step5)
