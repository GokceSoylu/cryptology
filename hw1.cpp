#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Crypto
{
public:
    virtual string encrypt(const string &text, const string &key) = 0;
    virtual string decrypt(const string &text, const string &key) = 0;
};

class ReverseCipher : public Crypto
{
public:
    string encrypt(const string &text, const string &key) override
    {
        string reversed = text;
        reverse(reversed.begin(), reversed.end());
        return reversed;
    }

    string decrypt(const string &text, const string &key) override
    {
        return encrypt(text, key);
    }
};

class CaesarCipher : public Crypto
{
public:
    string encrypt(const string &text, const string &key) override
    {
        int shift = stoi(key);
        string result;
        for (char ch : text)
        {
            if (isalpha(ch))
            {
                char base = islower(ch) ? 'a' : 'A';
                result += (char)(((ch - base + shift) % 26) + base);
            }
            else
            {
                result += ch;
            }
        }
        return result;
    }

    string decrypt(const string &text, const string &key) override
    {
        int shift = stoi(key);
        return encrypt(text, to_string(26 - shift));
    }
};

class VigenereCipher : public Crypto
{
public:
    string encrypt(const string &text, const string &key) override
    {
        string result;
        int keyIndex = 0;
        for (char ch : text)
        {
            if (isalpha(ch))
            {
                char base = islower(ch) ? 'a' : 'A';
                int shift = tolower(key[keyIndex % key.length()]) - 'a';
                result += (char)(((ch - base + shift) % 26) + base);
                keyIndex++;
            }
            else
            {
                result += ch;
            }
        }
        return result;
    }

    string decrypt(const string &text, const string &key) override
    {
        string result;
        int keyIndex = 0;
        for (char ch : text)
        {
            if (isalpha(ch))
            {
                char base = islower(ch) ? 'a' : 'A';
                int shift = tolower(key[keyIndex % key.length()]) - 'a';
                result += (char)(((ch - base - shift + 26) % 26) + base);
                keyIndex++;
            }
            else
            {
                result += ch;
            }
        }
        return result;
    }
};

int main()
{
    int choice;
    string text, key, action;
    Crypto *cipher = nullptr;

    cout << "Choose a cipher algorithm:" << endl;
    cout << "1 - Reverse Cipher" << endl;
    cout << "2 - Caesar Cipher" << endl;
    cout << "3 - Vigenere Cipher" << endl;
    cin >> choice;
    cin.ignore();

    cout << "Enter text: ";
    getline(cin, text);

    cout << "Encrypt or Decrypt (e/d): ";
    cin >> action;
    cin.ignore();

    switch (choice)
    {
    case 1:
        cipher = new ReverseCipher();
        break;
    case 2:
        cout << "Enter key (number): ";
        cin >> key;
        cin.ignore();
        cipher = new CaesarCipher();
        break;
    case 3:
        cout << "Enter key (word): ";
        cin >> key;
        cin.ignore();
        cipher = new VigenereCipher();
        break;
    default:
        cout << "Invalid choice" << endl;
        return 1;
    }

    if (action == "e")
    {
        cout << "Encrypted text: " << cipher->encrypt(text, key) << endl;
    }
    else if (action == "d")
    {
        cout << "Decrypted text: " << cipher->decrypt(text, key) << endl;
    }
    else
    {
        cout << "Invalid action" << endl;
    }

    delete cipher;
    return 0;
}
