# a değişkenine 5 değeri atanıyor. Bu bir tamsayıdır (integer).
a = 5  # Değer belirleme

# b değişkenine 10.4 değeri atanıyor. Bu bir ondalıklı sayıdır (float).
b = 10.4  # Değer belirleme

# a'ya 3 ekleniyor ve sonucu hesaplanıyor. Sonuç: 5 + 3 = 8.
a + 3  # Basit toplama işlemi

# a'nın 2'ye bölünmesi. Sonuç: 5 / 2 = 2.5.
a / 2  # Bölme işlemi

# a'nın önce 2 ile çarpılması, sonra 3'e bölünmesi ve son olarak 1 eklenmesi.
# İşlem sırası: (5 * 2) / 3 + 1 = 3.33 + 1 = 4.33.
a * 2 / 3 + 1  # Çarpma, bölme ve toplama işlemleri

# a'nın karesi hesaplanıyor. Sonuç: 5 ** 2 = 25.
a ** 2  # Üssü (üs alma) işlemi

## Tip Dönüşümleri (Type Casting)

# a değişkeninin tamsayı olduğundan emin olmak için tip dönüşümü yapılır.
# Burada int() fonksiyonu zaten tamsayı olan a'nın tipini tekrar kontrol eder.
int(a)  # Tamsayıya çevirme

# b değişkeni ondalıklı sayı olduğundan, float() ile tipi kontrol edilir.
float(b)  # Ondalıklı sayıya çevirme

# Karmaşık bir işlem sonucu: a * 2 / 3 işlemi yapılır ve sonuç tamsayıya dönüştürülür.
# İşlem sonucu: (5 * 2) / 3 = 3.33, bu değer int() ile 3'e yuvarlanır.
int(a * 2 / 3)  # İşlem sonucunu tamsayıya çevirme

# Yeni bir işlem: a ve b'nin çarpımına 3 ekleniyor. Sonuç: (5 * 10.4) + 3 = 52 + 3 = 55.
c = a * b + 3  # a ve b değişkenlerinin çarpımı ve 3 eklenmesi

# c sonucunu tamsayıya dönüştürme. Burada c float türündedir ve int() ile tam sayıya yuvarlanır.
int(c)  # c'nin tamsayıya dönüştürülmesi
