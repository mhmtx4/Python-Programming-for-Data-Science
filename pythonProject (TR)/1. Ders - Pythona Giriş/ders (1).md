
# Python Temelleri

Bu Python kodunda, programlamanın temel konularını ele alıyoruz. Burada değişkenler, veri tipleri, 
matematiksel işlemler ve konsola çıktı verme gibi temel işlemler detaylıca anlatılacaktır. 
Amacımız, Python’un nasıl çalıştığını anlamak ve temel işlemleri öğrenmek.

## 1. print() Fonksiyonu:
Python'da print() fonksiyonu, ekrana bir şeyler yazdırmak için kullanılır. Örneğin:

```python
print("hello world")
```

Bu kod çalıştırıldığında, terminalde `hello world` yazısı görünecektir. print() fonksiyonu içine 
aldığımız her şeyi ekrana basar. Bu bir sayı, metin veya başka bir şey olabilir.

## 2. Sayılar (Numbers):
Python’da sayılar iki temel türe ayrılır: tam sayılar (integers) ve ondalıklı sayılar (floats).

- **Tam Sayılar (Integers)**: Bunlar eksi sonsuzdan artı sonsuza kadar olan tam sayılardır. Örnek: `5`, `-3`, `0`.
- **Ondalıklı Sayılar (Floats)**: Bunlar virgülden sonra değeri olan sayılardır. Örnek: `9.5`, `-1.2`.

Eğer bir sayıyı direkt kodun içine yazarsak Python bunu işler fakat eğer çıktısını görmek istersek
print() ile yazdırmamız gerekir. Örneğin, `10` sayısını sadece yazarak çıktı almayız, ama
`print(10)` derseniz terminalde `10` görünecektir.

## 3. Veri Tipleri (Data Types):
Python’da her şey bir veri tipine sahiptir. Bir sayı, metin veya daha karmaşık bir yapı olabilir.
Veri tiplerini kontrol etmek için `type()` fonksiyonu kullanılır.

- `type(9)`: Bu fonksiyon, 9’un veri tipini sorgular. Çıktı olarak `<class 'int'>` döner çünkü 9 bir tam sayıdır.
- `type(9.5)`: Bu da bir ondalık sayı olduğu için `<class 'float'>` dönecektir.
- `type("aaa")`: String (yani metin) tipi sorgulaması yapılır ve sonuç `<class 'str'>` olacaktır.

## 4. Değişkenler (Variables):
Programlama dillerinde değişkenler, veri saklamak için kullanılır. Bir değer bir değişkene atandığında, 
o değeri daha sonra tekrar kullanabiliriz.

```python
a = 2
b = 3
c = "test"
```

Yukarıdaki örnekte, `a` değişkenine 2, `b` değişkenine 3 ve `c` değişkenine "test" stringi atanmıştır. 
Python'da değişkenlere herhangi bir veri tipi atanabilir. Ayrıca Python değişken tiplerini otomatik olarak 
tanır; bizim manuel olarak tip belirtmemize gerek yoktur.

## 5. Matematiksel İşlemler (Mathematical Operations):
Python'da temel matematiksel işlemler çok basittir. Değişkenler arasında toplama, çıkarma, çarpma gibi 
işlemleri doğrudan yapabiliriz.

- `a * b`: Bu ifade, `a` ve `b` değişkenlerinin çarpılması anlamına gelir. Eğer `a = 2` ve `b = 3` ise, 
sonuç `6` olacaktır.

- `a + b`: Bu, `a` ve `b` değişkenlerinin toplanmasıdır. Sonuç `5` olur.

- `a - b`: Bu ifade, `a` ve `b` değişkenlerinin çıkarılmasını ifade eder. Sonuç `-1` olur.

Matematiksel işlemler sırasında, işlemin sırası önemlidir. Eğer toplama, çıkarma veya çarpma işlemi yapıyorsak, 
değişkenlere atanmış değerler üzerinden işlem yapılır.

## Özet:
Bu kod Python’un temel yapı taşlarını anlamak için iyi bir başlangıçtır. print() ile ekrana çıktı verebilir, 
değişkenlerle çalışabilir ve matematiksel işlemler yapabiliriz. Her adımı dikkatle inceleyerek Python’un temel işleyişini kavrayabilirsiniz.
