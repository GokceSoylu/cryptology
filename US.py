import itertools

def reverse_cipher(text):
    return text[::-1]

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
        else:
            shifted_char = char
        result += shifted_char
    return result

def transposition_cipher(text, cols):
    if cols <= 1:
        return text
    rows = (len(text) + cols - 1) // cols
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(cols):
            if index < len(text):
                grid[r][c] = text[index]
                index += 1

    decrypted_text = [''] * len(text)
    index_decrypted = 0
    for c in range(cols):
        for r in range(rows):
            if r < len(grid) and c < len(grid[r]) and grid[r][c] != '':
                decrypted_text[index_decrypted] = grid[r][c]
                index_decrypted += 1
    return "".join(decrypted_text).rstrip()

def is_english(text):
    # A very basic check, can be improved with more sophisticated methods
    common_words = ["the", "a", "is", "are", "and", "of", "to", "in", "it", "that"]
    word_count = 0
    for word in text.lower().split():
        if word in common_words:
            word_count += 1
    return word_count >= 2 # Adjust this threshold as needed

encrypted_message = "kavvkaappyt_vpasuuZynlvtjy__hl_luaJh!_dlP_knlLb__ll_c_,buu_whP"

for cols in range(2, 11):
    decrypted_transposition = transposition_cipher(encrypted_message, cols)
    for shift in range(1, 26):
        decrypted_caesar = caesar_cipher(decrypted_transposition, shift)
        decrypted_reverse = reverse_cipher(decrypted_caesar)
        if is_english(decrypted_reverse):
            print(f"Possible Original Message (Cols: {cols}, Shift: {shift}): {decrypted_reverse}")

print("Brute-force decryption complete.")