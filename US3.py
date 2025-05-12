import base64
import itertools

def reverse_cipher(text):
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

def transposition_decrypt(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    grid = [''] * len(text)
    key_order = sorted(range(cols), key=lambda k: key[k])
    index = 0
    for col_index in key_order:
        for row in range(rows):
            pos = row * cols + col_index
            if pos < len(text):
                grid[pos] = text[index]
                index += 1
    return ''.join(grid)

def xor_decrypt(text, key):
    result = ''
    key_len = len(key)
    for i in range(len(text)):
        result += chr(ord(text[i]) ^ ord(key[i % key_len]))
    return result

def rot13_decrypt(text):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') - 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') - 13) % 26) + ord('A'))
        else:
            result += char
    return result

encrypted_message_b64 = "SkNfVVVWdGp0dVVXbHV6YQ=="
xor_key = "k3y!"
transposition_key = "CIPHER"
caesar_shift = 4

# Decryption process (order needs to be determined)
possible_orders = list(itertools.permutations([
    "base64", "reverse", "caesar", "transposition", "xor", "rot13"
]))

for order in possible_orders:
    decrypted_text = encrypted_message_b64
    steps = {}

    for step in order:
        if step == "base64":
            decrypted_text = base64.b64decode(decrypted_text).decode('utf-8')
            steps[step] = decrypted_text
        elif step == "reverse":
            decrypted_text = reverse_cipher(decrypted_text)
            steps[step] = decrypted_text
        elif step == "caesar":
            decrypted_text = caesar_decrypt(decrypted_text, caesar_shift)
            steps[step] = decrypted_text
        elif step == "transposition":
            decrypted_text = transposition_decrypt(decrypted_text, transposition_key)
            steps[step] = decrypted_text
        elif step == "xor":
            decrypted_text = xor_decrypt(decrypted_text, xor_key)
            steps[step] = decrypted_text
        elif step == "rot13":
            decrypted_text = rot13_decrypt(decrypted_text)
            steps[step] = decrypted_text
    else:
        print("Decryption Order:", order)
        for desc, text in steps.items():
            print(f"After {desc} decryption: {text}")
        print("Original message:", decrypted_text)
        break