import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def ascii_minus_one(s):
    return ''.join(chr(ord(c)-1) for c in s)

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

def aes_decrypt_ecb(ciphertext_bytes, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext_bytes)
    try:
        return unpad(decrypted, AES.block_size).decode()
    except ValueError:
        return None

# Başlangıç: base64 decode
cipher_b64 = "yNjMHmg6dB9czTMOA2D6nA=="
step1 = base64.b64decode(cipher_b64)
print("1. After Base64 decode:", step1)

# Şimdi olası tüm işlem sıralarını deneyerek brute force ilerleyelim.
# Doğru sırada yapılmadığında bazı adımlar (özellikle AES) hata verecektir.

# Step2: AES decrypt (doğru sıra olasılığı)
key = b'Secret16ByteKey'
step2 = aes_decrypt_ecb(step1, key)
if step2:
    print("2. After AES decryption:", step2)

    # Step3: reverse
    step3 = step2[::-1]
    print("3. After reversing:", step3)

    # Step4: Caesar -7
    step4 = caesar_decrypt(step3, shift=7)
    print("4. After Caesar decryption:", step4)

    # Step5: ASCII -1
    step5 = ascii_minus_one(step4)
    print("5. After ASCII -1:", step5)

    print("Original message:", step5)
else:
    print("AES decryption failed at this order. Try other ordering.")
