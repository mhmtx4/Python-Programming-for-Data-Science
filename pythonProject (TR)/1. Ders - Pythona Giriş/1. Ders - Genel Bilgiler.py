# Ekrana "hello world" yazdırma işlemi
# Burada print() fonksiyonu ile parantez içerisindeki string'i ekrana yazdırıyoruz.
print("hello world")

# Sayılar (Numbers)
# 10 ve 9 birer tam sayı (integer). Ancak sadece yazıldıkları için herhangi bir işlem yapılmıyor.
# Eğer bir değer çıktı almak istiyorsak, print() ile yazdırmalıyız.
10
9
# "5" bir string, yani metin tipinde bir veri. Bunu ekrana yazdırmak için print() kullanıyoruz.
print("5")

# Veri tiplerini kontrol etme (Type checking)
# Python'da her veri bir tipe sahiptir. Bu tipleri görmek için type() fonksiyonu kullanılır.
# Aşağıda bazı örnekleri inceleyelim:

# 9 bir tam sayı (integer). Python bunu otomatik olarak tanır ve int tipi olarak işaretler.
print(type(9))  # <class 'int'> çıktısını alırız, çünkü 9 bir tam sayıdır.

# 9.5 bir ondalık sayı (float). Python bunu float tipi olarak tanımlar.
print(type(9.5))  # <class 'float'> çıktısını alırız, çünkü 9.5 bir ondalık sayıdır.

# "aaa" bir string, yani metin tipindedir. Python bunu string (str) tipi olarak tanımlar.
print(type("aaa"))  # <class 'str'> çıktısını alırız, çünkü "aaa" bir metindir.

# Değişkenler (Variables)
# Değişkenler bir değeri saklamak için kullanılır. Aşağıda a, b, ve c değişkenlerine farklı değerler atıyoruz:
a = 2  # a değişkenine 2 sayısını atadık.
b = 3  # b değişkenine 3 sayısını atadık.
c = "test"  # c değişkenine "test" metnini atadık.

# Matematiksel işlemler (Mathematical operations)
# Değişkenler üzerinde matematiksel işlemler yapabiliriz. Örneğin:

# Çarpma işlemi:
# a * b ifadesi, a ile b'nin çarpılması anlamına gelir.
# 2 * 3 = 6 sonucunu verir.
print(a * b)  # Sonuç olarak 6 yazdırılır.

# Toplama işlemi:
# a + b ifadesi, a ile b'nin toplanması anlamına gelir.
# 2 + 3 = 5 sonucunu verir.
print(a + b)  # Sonuç olarak 5 yazdırılır.

# Çıkarma işlemi:
# a - b ifadesi, a ile b'nin çıkarılması anlamına gelir.
# 2 - 3 = -1 sonucunu verir.
print(a - b)  # Sonuç olarak -1 yazdırılır.

# Özet:
# Eğer bir işlem yapılacaksa (örneğin toplama, çıkarma gibi),
# önce değişkenlere değer atanmalı ya da doğrudan işlem yapılarak çıktı alınmalıdır.
# Python her işlemi sırasıyla değerlendirir ve hesaplar.
