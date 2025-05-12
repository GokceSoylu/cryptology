import base64

# Caesar decrypt
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

# ROT13 decrypt
def rot13(text):
    return text.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

# XOR decrypt
def xor_decrypt(data: bytes, key: str) -> str:
    key_bytes = key.encode()
    decrypted = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])
    print("2. XOR raw bytes:", decrypted)  # <-- ekledik
    return decrypted.decode('latin1')


# Transposition decrypt
def transposition_decrypt(text, key):
    import math
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)
    num_shaded = (num_cols * num_rows) - len(text)

    # Get order of columns based on key
    col_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    col_positions = [i[0] for i in col_order]

    # Create empty columns
    columns = [''] * num_cols
    k = 0
    for i in range(num_cols):
        col_len = num_rows
        if col_positions[i] >= num_cols - num_shaded:
            col_len -= 1
        columns[col_positions[i]] = text[k:k+col_len]
        k += col_len

    # Read row-wise
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
xor_step = xor_decrypt(decoded_bytes, "k3y!")
print("2. After XOR decryption:", xor_step)

# Step 3: Reverse
reversed_step = xor_step[::-1]
print("3. After reverse:", reversed_step)

# Step 4: ROT13
rot13_step = rot13(reversed_step)
print("4. After ROT13:", rot13_step)

# Step 5: Caesar decrypt (shift -4)
caesar_step = caesar_decrypt(rot13_step, shift=4)
print("5. After Caesar decryption:", caesar_step)

# Step 6: Transposition decryption with key "CIPHER"
final_plaintext = transposition_decrypt(caesar_step, "CIPHER")
print("Original message:", final_plaintext)
