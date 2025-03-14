# cryptology Course Notes 

# Şifreleme Algoritmaları: Reverse, Caesar ve Vigenere

## Genel Bakış
Bu Java programı, kullanıcıların mesajlarını **Reverse Cipher (Ters Çevirme Şifreleme)**, **Caesar Cipher** veya **Vigenere Cipher** yöntemleriyle şifrelemelerine ve şifrelerini çözmelerine olanak tanır. Program, nesne yönelimli programlama (OOP) yaklaşımını benimseyerek kullanıcı dostu bir arayüz sunar.

## Özellikler
- **Reverse Cipher, Caesar Cipher ve Vigenere Cipher** desteği.
- Kullanıcının **şifreleme** veya **şifre çözme** işlemini seçebilmesi.
- **OOP tabanlı tasarım** ile esnek ve modüler yapı.
- Kullanıcıdan alınan anahtar ile şifreleme işlemlerini özelleştirme.

## Nasıl Çalışır?
1. Kullanıcı şifreleme yöntemini seçer:
   - `1` → **Reverse Cipher (Ters Çevirme Şifreleme)**
   - `2` → **Caesar Cipher (Sezar Şifreleme)**
   - `3` → **Vigenere Cipher**
2. Kullanıcı işlenecek metni girer.
3. Kullanıcı işlemi seçer:
   - `e` → **Şifreleme**
   - `d` → **Şifre Çözme**
4. Seçilen yönteme göre işlem gerçekleştirilir ve sonuç ekrana yazdırılır.

## Şifreleme Algoritmalarının Açıklaması

### Reverse Cipher
**Reverse Cipher (Ters Çevirme Şifreleme)**, en basit şifreleme yöntemlerinden biridir. Metindeki karakterler ters çevrilerek şifreleme yapılır.

- **Şifreleme:** Metin karakterleri ters çevrilir.
- **Şifre Çözme:** Aynı işlem tekrar uygulanarak orijinal metin elde edilir.

**Örnek:**
```
Düz Metin: HELLO
Şifreli Metin: OLLEH
```

### Caesar Cipher
**Caesar Cipher (Sezar Şifreleme)**, her harfi belirli bir kaydırma miktarı kadar ileri alarak şifreleme yapan bir yöntemdir.

- **Şifreleme:** Harfler, belirlenen `n` kadar kaydırılır.
- **Şifre Çözme:** Aynı `n` kadar geriye kaydırılarak orijinal metin elde edilir.

**Örnek:**
```
Düz Metin: HELLO
Anahtar: 3
Şifreli Metin: KHOOR
```

### Vigenere Cipher
**Vigenere Cipher**, harf çiftleriyle çalışan bir polialfabetik şifreleme yöntemidir. Kullanıcının belirttiği bir **kelime anahtar** olarak kullanılır.

- **Şifreleme:** Anahtar kelimenin harflerine göre her harf farklı bir şekilde kaydırılır.
- **Şifre Çözme:** Aynı anahtar ile ters kaydırma işlemi uygulanarak orijinal metin elde edilir.

**Örnek:**
```
Düz Metin: HELLO
Anahtar: KEY
Şifreli Metin: RIJVS
```

## Kullanım
Java programını çalıştırın ve aşağıdaki adımları takip edin:
```sh
Şifreleme Yöntemini Seçin (1: Reverse, 2: Caesar, 3: Vigenere): 2
Metni Girin: HELLO
İşlem Seçin (e: Şifreleme, d: Şifre Çözme): e
Anahtar Girin: 3
Sonuç: KHOOR
```

## Gereksinimler
- Java Development Kit (JDK) 8+
- Java derleyicisi ve çalışma ortamı

## Geliştirici
Bu proje **Gökçe Soylu**, Bilgisayar Mühendisliği öğrencisi tarafından geliştirilmiştir.




# Transpozisyon ve Playfair Şifreleme/Şifre Çözme

## Genel Bakış
Bu Java programı, kullanıcıların mesajlarını **Transpozisyon Şifreleme** veya **Playfair Şifreleme** kullanarak şifrelemelerine ve şifrelerini çözmelerine olanak tanır. Program, nesne yönelimli programlama (OOP) yaklaşımını benimseyerek kullanıcı dostu bir arayüz sunar.

## Özellikler
- **Transpozisyon Şifreleme** ve **Playfair Şifreleme** desteği.
- Kullanıcının **şifreleme** veya **şifre çözme** işlemini seçebilmesi.
- **OOP tabanlı tasarım** ile esnek ve modüler yapı.
- Otomatik metin işleme ve formatlama.

## Nasıl Çalışır?
1. Kullanıcı şifreleme yöntemini seçer:
   - `1` → **Transpozisyon Şifreleme**
   - `2` → **Playfair Şifreleme**
2. Kullanıcı işlenecek metni girer.
3. Kullanıcı işlemi seçer:
   - `1` → **Şifreleme**
   - `2` → **Şifre Çözme**
4. Program, seçilen algoritmayı uygular ve sonucu ekrana yazdırır.

## Şifreleme Algoritmalarının Açıklaması

### Transpozisyon Şifreleme
**Transpozisyon Şifreleme**, mesajın karakterlerini belirli bir anahtar düzenine göre yeniden sıralayan bir yöntemdir. 

- **Şifreleme:** Mesaj, belirlenen sütun sayısına göre bir tabloya yerleştirilir ve sütun sütun okunarak şifreli metin oluşturulur.
- **Şifre Çözme:** Şifreli metin, aynı sütun düzeninde tabloya yerleştirilerek satır satır okunur ve orijinal mesaj elde edilir.

**Örnek:**
```
Mesaj: HELLOWORLD
Anahtar: 4
Tablo:
H E L L
O W O R
L D X X
Şifreli Metin: HOLWELXODRX
```

### Playfair Şifreleme
**Playfair Şifreleme**, harf çiftleri (digragraf) kullanarak şifreleme yapan bir yöntemdir. Bu yöntem, bir **5x5 matris** oluşturarak çalışır ve anahtar kelimeye dayanır.

- **Şifreleme:**
  1. Metin harf çiftlerine ayrılır, aynı harf yan yana gelirse 'X' eklenir.
  2. Çiftler matris kurallarına göre değiştirilir:
     - Aynı **satırda** bulunan harfler sağa kaydırılır.
     - Aynı **sütunda** bulunan harfler aşağı kaydırılır.
     - Farklı satır ve sütundaysa, harfler dikdörtgenin karşı köşelerine yerleştirilir.
- **Şifre Çözme:** Aynı kurallar tersine uygulanarak çözülür.

**Örnek:**
```
Anahtar Kelime: KEYWORD
Matris:
K E Y W O
R D A B C
F G H I L
M N P Q S
T U V X Z
Düz Metin: HELLO → HE LO
Şifreli Metin: DM OS
```

## Kullanım
Java programını çalıştırın ve aşağıdaki adımları takip edin:
```sh
Şifreleme Yöntemini Seçin (1: Transpozisyon, 2: Playfair): 1
Metni Girin: HELLO
İşlem Seçin (1: Şifreleme, 2: Şifre Çözme): 1
Sonuç: HOLWELXODRX
```

## Gereksinimler
- Java Development Kit (JDK) 8+
- Java derleyicisi ve çalışma ortamı

## Geliştirici
Bu proje **Gökçe Soylu**, Bilgisayar Mühendisliği öğrencisi tarafından geliştirilmiştir.

