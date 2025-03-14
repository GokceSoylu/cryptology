import java.util.*;

// Base interface for encryption and decryption
interface Cipher {
    String encrypt(String text);

    String decrypt(String text);
}

// Transposition Cipher Implementation
class TranspositionCipher implements Cipher {
    private int key;

    public TranspositionCipher(int key) {
        this.key = key;
    }

    @Override
    public String encrypt(String text) {
        int length = text.length();
        int rows = (int) Math.ceil((double) length / key);
        char[][] grid = new char[rows][key];
        int index = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < key; j++) {
                if (index < length) {
                    grid[i][j] = text.charAt(index++);
                } else {
                    grid[i][j] = 'X'; // Padding
                }
            }
        }

        StringBuilder cipherText = new StringBuilder();
        for (int j = 0; j < key; j++) {
            for (int i = 0; i < rows; i++) {
                cipherText.append(grid[i][j]);
            }
        }
        return cipherText.toString();
    }

    @Override
    public String decrypt(String text) {
        int length = text.length();
        int rows = (int) Math.ceil((double) length / key);
        char[][] grid = new char[rows][key];
        int index = 0;

        for (int j = 0; j < key; j++) {
            for (int i = 0; i < rows; i++) {
                if (index < length) {
                    grid[i][j] = text.charAt(index++);
                }
            }
        }

        StringBuilder plainText = new StringBuilder();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < key; j++) {
                plainText.append(grid[i][j]);
            }
        }
        return plainText.toString().replace("X", "");
    }
}

// Playfair Cipher Implementation
class PlayfairCipher implements Cipher {
    private char[][] matrix;
    private String key;

    public PlayfairCipher(String key) {
        this.key = key;
        generateMatrix();
    }

    private void generateMatrix() {
        matrix = new char[5][5];
        Set<Character> used = new LinkedHashSet<>();
        String keyString = key.toUpperCase().replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ";

        for (char c : keyString.toCharArray()) {
            if (used.size() < 25 && c >= 'A' && c <= 'Z') {
                used.add(c);
            }
        }

        Iterator<Character> it = used.iterator();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                matrix[i][j] = it.next();
            }
        }
    }

    private String processText(String text) {
        text = text.toUpperCase().replace("J", "I").replaceAll("[^A-Z]", "");
        StringBuilder sb = new StringBuilder(text);
        for (int i = 0; i < sb.length() - 1; i += 2) {
            if (sb.charAt(i) == sb.charAt(i + 1)) {
                sb.insert(i + 1, 'X');
            }
        }
        if (sb.length() % 2 != 0) {
            sb.append('X');
        }
        return sb.toString();
    }

    private String cipher(String text, boolean encrypt) {
        text = processText(text);
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < text.length(); i += 2) {
            char a = text.charAt(i), b = text.charAt(i + 1);
            int[] posA = findPosition(a), posB = findPosition(b);

            if (posA[0] == posB[0]) {
                result.append(matrix[posA[0]][(posA[1] + (encrypt ? 1 : 4)) % 5]);
                result.append(matrix[posB[0]][(posB[1] + (encrypt ? 1 : 4)) % 5]);
            } else if (posA[1] == posB[1]) {
                result.append(matrix[(posA[0] + (encrypt ? 1 : 4)) % 5][posA[1]]);
                result.append(matrix[(posB[0] + (encrypt ? 1 : 4)) % 5][posB[1]]);
            } else {
                result.append(matrix[posA[0]][posB[1]]);
                result.append(matrix[posB[0]][posA[1]]);
            }
        }
        return result.toString();
    }

    private int[] findPosition(char c) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (matrix[i][j] == c) {
                    return new int[] { i, j };
                }
            }
        }
        return null;
    }

    @Override
    public String encrypt(String text) {
        return cipher(text, true);
    }

    @Override
    public String decrypt(String text) {
        return cipher(text, false);
    }
}

// Main class to interact with user
public class CipherTest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Choose Cipher (1: Transposition, 2: Playfair): ");
        int choice = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter text: ");
        String text = scanner.nextLine();

        System.out.print("Choose action (1: Encrypt, 2: Decrypt): ");
        int action = scanner.nextInt();

        Cipher cipher = (choice == 1) ? new TranspositionCipher(4) : new PlayfairCipher("KEYWORD");
        String result = (action == 1) ? cipher.encrypt(text) : cipher.decrypt(text);

        System.out.println("Result: " + result);
    }
}
