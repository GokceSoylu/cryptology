import base64
from Crypto.Cipher import AES

# 1. Base64 decode
cipher_b64 = "yNjMHmg6dB9czTMOA2D6nA=="
cipher_bytes = base64.b64decode(cipher_b64)
print("1. After Base64 decode:", cipher_bytes)

# 2. AES decrypt without unpadding
key = b'Secret16ByteKey!'
cipher = AES.new(key, AES.MODE_ECB)
decrypted = cipher.decrypt(cipher_bytes)

print("2. Raw AES decrypted bytes:", decrypted)
try:
    text = decrypted.decode('utf-8')
    print("2b. AES decrypted (utf-8):", text)
except:
    print("2b. AES decrypted: Not UTF-8 — raw bytes shown above")
