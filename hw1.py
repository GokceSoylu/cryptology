class Crypto:
    def encrypt(self, text, key):
        raise NotImplementedError("Encrypt method must be implemented")
    
    def decrypt(self, text, key):
        raise NotImplementedError("Decrypt method must be implemented")

class ReverseCipher(Crypto):
    def encrypt(self, text, key=None):
        return text[::-1]
    
    def decrypt(self, text, key=None):
        return text[::-1]

class CaesarCipher(Crypto):
    def encrypt(self, text, key):
        return ''.join(chr((ord(char) - 97 + key) % 26 + 97) if char.islower() else chr((ord(char) - 65 + key) % 26 + 65) if char.isupper() else char for char in text)
    
    def decrypt(self, text, key):
        return ''.join(chr((ord(char) - 97 - key) % 26 + 97) if char.islower() else chr((ord(char) - 65 - key) % 26 + 65) if char.isupper() else char for char in text)

class VigenereCipher(Crypto):
    def encrypt(self, text, key):
        key = key.lower()
        encrypted_text = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - 97
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 + shift) % 26 + 65)
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text
    
    def decrypt(self, text, key):
        key = key.lower()
        decrypted_text = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - 97
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 - shift) % 26 + 65)
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text

def main():
    print("Choose a cipher algorithm:")
    print("1 - Reverse Cipher")
    print("2 - Caesar Cipher")
    print("3 - Vigenere Cipher")
    
    choice = input("Enter choice: ")
    text = input("Enter text: ")
    action = input("Encrypt or Decrypt (e/d): ")
    
    if choice == "1":
        cipher = ReverseCipher()
        key = None
    elif choice == "2":
        key = int(input("Enter key (number): "))
        cipher = CaesarCipher()
    elif choice == "3":
        key = input("Enter key (word): ")
        cipher = VigenereCipher()
    else:
        print("Invalid choice")
        return
    
    if action == 'e':
        print("Encrypted text:", cipher.encrypt(text, key))
    elif action == 'd':
        print("Decrypted text:", cipher.decrypt(text, key))
    else:
        print("Invalid action")

if __name__ == "__main__":
    main()
