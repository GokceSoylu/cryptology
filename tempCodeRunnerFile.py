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

import base64
from Crypto.Cipher import AES

# 1. Base64 decode
cipher_b64 = "yNjMHmg6dB9czTMOA2D6nA=="
cipher_bytes = base64.b64decode(cipher_b64)
print("1. After Base64 decode:", cipher_bytes)

# 2. AES decrypt (no padding)
key = b'Secret16ByteKey!'
cipher = AES.new(key, AES.MODE_ECB)
aes_raw = cipher.decrypt(cipher_bytes)
print("2. Raw AES decrypted bytes:", aes_raw)

# 3. Try decoding raw AES output as Latin-1 to preserve byte values
step3 = aes_raw.decode('latin1')
print("3. As Latin-1 string:", step3)

# 4. Caesar -7
step4 = caesar_decrypt(step3)
print("4. After Caesar decryption:", step4)

# 5. ASCII -1
step5 = ascii_minus_one(step4)
print("5. After ASCII -1:", step5)

# 6. Reverse
original_message = step5[::-1]
print("Original message:", original_message)
