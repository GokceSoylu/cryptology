import java.util.Scanner;

abstract class Crypto {
    abstract String encrypt(String text, String key);

    abstract String decrypt(String text, String key);
}

class ReverseCipher extends Crypto {
    @Override
    String encrypt(String text, String key) {
        return new StringBuilder(text).reverse().toString();
    }

    @Override
    String decrypt(String text, String key) {
        return new StringBuilder(text).reverse().toString();
    }
}

class CaesarCipher extends Crypto {
    @Override
    String encrypt(String text, String key) {
        int shift = Integer.parseInt(key);
        StringBuilder result = new StringBuilder();
        for (char ch : text.toCharArray()) {
            if (Character.isLetter(ch)) {
                char base = Character.isLowerCase(ch) ? 'a' : 'A';
                result.append((char) ((ch - base + shift) % 26 + base));
            } else {
                result.append(ch);
            }
        }
        return result.toString();
    }

    @Override
    String decrypt(String text, String key) {
        int shift = Integer.parseInt(key);
        return encrypt(text, String.valueOf(26 - shift));
    }
}

class VigenereCipher extends Crypto {
    @Override
    String encrypt(String text, String key) {
        StringBuilder result = new StringBuilder();
        key = key.toLowerCase();
        int keyIndex = 0;
        for (char ch : text.toCharArray()) {
            if (Character.isLetter(ch)) {
                char base = Character.isLowerCase(ch) ? 'a' : 'A';
                int shift = key.charAt(keyIndex % key.length()) - 'a';
                result.append((char) ((ch - base + shift) % 26 + base));
                keyIndex++;
            } else {
                result.append(ch);
            }
        }
        return result.toString();
    }

    @Override
    String decrypt(String text, String key) {
        StringBuilder result = new StringBuilder();
        key = key.toLowerCase();
        int keyIndex = 0;
        for (char ch : text.toCharArray()) {
            if (Character.isLetter(ch)) {
                char base = Character.isLowerCase(ch) ? 'a' : 'A';
                int shift = key.charAt(keyIndex % key.length()) - 'a';
                result.append((char) ((ch - base - shift + 26) % 26 + base));
                keyIndex++;
            } else {
                result.append(ch);
            }
        }
        return result.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose a cipher algorithm:");
        System.out.println("1 - Reverse Cipher");
        System.out.println("2 - Caesar Cipher");
        System.out.println("3 - Vigenere Cipher");

        int choice = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter text: ");
        String text = scanner.nextLine();

        System.out.print("Encrypt or Decrypt (e/d): ");
        String action = scanner.nextLine();

        Crypto cipher = null;
        String key = "";

        switch (choice) {
            case 1:
                cipher = new ReverseCipher();
                break;
            case 2:
                System.out.print("Enter key (number): ");
                key = scanner.nextLine();
                cipher = new CaesarCipher();
                break;
            case 3:
                System.out.print("Enter key (word): ");
                key = scanner.nextLine();
                cipher = new VigenereCipher();
                break;
            default:
                System.out.println("Invalid choice");
                scanner.close();
                return;
        }

        if (action.equals("e")) {
            System.out.println("Encrypted text: " + cipher.encrypt(text, key));
        } else if (action.equals("d")) {
            System.out.println("Decrypted text: " + cipher.decrypt(text, key));
        } else {
            System.out.println("Invalid action");
        }

        scanner.close();
    }
}
