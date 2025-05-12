def reverse_cipher(text):
    return text[::-1]

def caesar_decrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def transposition_decrypt(ciphertext, key):
    num_cols = key
    num_rows = len(ciphertext) // key
    if len(ciphertext) % key != 0:
        num_rows += 1

    num_shaded_boxes = (num_cols * num_rows) - len(ciphertext)
    plaintext = [''] * num_cols
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1

        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)

# Şifreli metin
encrypted_message = 'kavvkaappyt_vpasuuZynlvtjy__hl_luaJh!_dlP_knlLb__ll_c_,buu_whP'

# 1. Adım: Reverse Cipher (ters çevir)
reversed_message = reverse_cipher(encrypted_message)

# 2. ve 3. Adım: Caesar ve Transposition brute-force
for caesar_key in range(1, 26):
    caesar_text = caesar_decrypt(reversed_message, caesar_key)
    for trans_key in range(2, 11):
        decrypted = transposition_decrypt(caesar_text, trans_key)
        print(f'Caesar Key: {caesar_key}, Transposition Key: {trans_key}')
        print(f'Decrypted Message: {decrypted}\n')
