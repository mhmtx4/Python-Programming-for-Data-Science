## SAYILAR (NUMBERS)

# x değişkenine 50 değeri atanıyor, bu bir tamsayıdır (integer)
x = 50
# type() fonksiyonu, x değişkeninin tipini kontrol eder. Burada x tamsayıdır (int).
type(x)

# x değişkenine 10.7 değeri atanıyor, bu bir ondalıklı sayıdır (float).
x = 10.7
# type() fonksiyonu, x değişkeninin tipini kontrol eder. Burada x ondalıklı sayıdır (float).
type(x)

# x değişkenine karmaşık bir sayı atanıyor. 2 reel kısmı, 2j ise sanal kısmıdır.
x = 2j + 2
# type() fonksiyonu, x değişkeninin tipini kontrol eder. Burada x karmaşık bir sayıdır (complex).
type(x)

## METİNLER (STRINGS)

# x değişkenine "hello" string değeri atanıyor. Bu bir metindir (string).
x = "hello"
# type() fonksiyonu, x değişkeninin tipini kontrol eder. Burada x string (metin) türündedir.
type(x)

## MANTIKSAL DEĞERLER (BOOLEANS)

# Python'da True ve False boolean (mantıksal) değerlerdir.
True  # Doğru anlamına gelir.
False  # Yanlış anlamına gelir.

# type() fonksiyonu, True değerinin tipini kontrol eder. Boolean (bool) veri tipindedir.
type(True)

# Python'da karşılaştırma işlemi: 5, 4'e eşit mi? Sonuç False olur.
5 == 4  # Yanlış, False döner.

# Python'da karşılaştırma işlemi: 3, 2'ye eşit mi? Sonuç False olur.
3 == 2  # Yanlış, False döner.

# Python'da karşılaştırma işlemi: 1, 1'e eşit mi? Sonuç True olur.
1 == 1  # Doğru, True döner.

# type() fonksiyonu, karşılaştırma sonucunun tipini kontrol eder. Bu karşılaştırma boolean (bool) tipindedir.
type(3 == 2)

## LİSTELER (LIST)

# x değişkenine ["a", "b", "c"] şeklinde bir liste atanıyor.
# Listeler sıralı ve değiştirilebilir veri yapılarıdır.
x = ["a", "b", "c"]
# type() fonksiyonu, x değişkeninin tipini kontrol eder. Burada x liste (list) türündedir.
type(x)

## SÖZLÜKLER (DICTIONARIES)

# x değişkenine bir sözlük (dictionary) atanıyor. 
# Sözlükler anahtar-değer (key-value) çiftlerinden oluşur.
x = {"name": "Peter", "Age": 36}
# type() fonksiyonu, x değişkeninin tipini kontrol eder. Burada x bir sözlük (dict) türündedir.
type(x)

## DEMETLER (TUPLES)

# x değişkenine bir demet (tuple) atanıyor.
# Demetler sıralı fakat değiştirilemeyen (immutable) veri yapılarıdır.
x = ("name", "Peter", "Age")
# type() fonksiyonu, x değişkeninin tipini kontrol eder. Burada x demet (tuple) türündedir.
type(x)

## KÜMELER (SETS)

# x değişkenine bir küme (set) atanıyor.
# Kümeler sırasız ve benzersiz elemanlardan oluşan veri yapılarıdır.
x = {"name", "Peter", "Age"}
# type() fonksiyonu, x değişkeninin tipini kontrol eder. Burada x küme (set) türündedir.
type(x)
