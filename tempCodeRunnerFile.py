import base64

def caesar_decrypt(text, shift):
    result = ''
    for c in text:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += c
    return result

def rot13(text):
    return text.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

def xor_decrypt(data: bytes, key: str) -> str:
    key_bytes = key.encode()
    decrypted = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])
    print("2. XOR raw bytes:", decrypted)
    return decrypted.decode('latin1')

def transposition_decrypt(text, key):
    import math
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
    num_shaded = (num_cols * num_rows) - len(text)

    col_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    col_positions = [i[0] for i in col_order]

    columns = [''] * num_cols
    k = 0
    for i in range(num_cols):
        col_len = num_rows
        if col_positions[i] >= num_cols - num_shaded:
            col_len -= 1
        columns[col_positions[i]] = text[k:k+col_len]
        k += col_len

    plaintext = ''
    for r in range(num_rows):
        for c in range(num_cols):
            if r < len(columns[c]):
                plaintext += columns[c][r]
    return plaintext

# Step 1: Base64 decode
cipher_b64 = "SkNfVVVWdGp0dVVXbHV6YQ=="
decoded_bytes = base64.b64decode(cipher_b64)
print("1. After Base64 decode:", decoded_bytes)

# Step 2: XOR decrypt
xor_out = xor_decrypt(decoded_bytes, "k3y!")
print("3. After XOR decrypt:", xor_out)

# Step 3: Reverse
step3 = xor_out[::-1]
print("4. After reverse:", step3)

# Step 4: Caesar -4
step4 = caesar_decrypt(step3, 4)
print("5. After Caesar decryption:", step4)

# Step 5: ROT13
step5 = rot13(step4)
print("6. After ROT13:", step5)

# Step 6: Transposition Decryption
original_message = transposition_decrypt(step5, "CIPHER")
print("Original message:", original_message)
# Orijinal hali
print("Original message:", original_message)

# Unicode escape versiyonu
print("Original message (escaped):", original_message.encode('unicode_escape').decode())

