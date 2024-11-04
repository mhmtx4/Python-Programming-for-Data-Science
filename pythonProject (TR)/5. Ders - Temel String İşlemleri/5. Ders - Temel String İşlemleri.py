# Python'da Temel String (Dize) İşlemleri

# Bir string oluşturma
benim_string = "Merhaba, Dünya!"

# String'deki karakterlere erişim
ilk_karakter = benim_string[0]  # 'M'
son_karakter = benim_string[-1]  # '!'

# String dilimleme
alt_dize = benim_string[0:7]  # 'Merhaba'

# String birleştirme
selamlama = "Merhaba"
isim = "Ahmet"
tam_selamlama = selamlama + ", " + isim + "!"  # 'Merhaba, Ahmet!'

# String uzunluğu
uzunluk = len(benim_string)  # 14

# String metotları
buyuk_harf = benim_string.upper()  # 'MERHABA, DÜNYA!'
kucuk_harf = benim_string.lower()  # 'merhaba, dünya!'
baslik_harf = benim_string.title()  # 'Merhaba, Dünya!'

# Boşlukları temizleme
bosluklu_string = "   Merhaba, Dünya!   "
temizlenmis_string = bosluklu_string.strip()  # 'Merhaba, Dünya!'

# Alt dizeyi değiştirme
degistirilmis_string = benim_string.replace("Dünya", "Python")  # 'Merhaba, Python!'

# String'i bölme
bolunmus_string = benim_string.split(", ")  # ['Merhaba', 'Dünya!']

# Bir liste halindeki stringleri birleştirme
kelimeler = ["Merhaba", "Dünya"]
birlesmis_string = " ".join(kelimeler)  # 'Merhaba Dünya'

# Alt dize var mı kontrol etme
icerir_merhaba = "Merhaba" in benim_string  # True
icerir_python = "Python" in benim_string  # False

# String formatlama
isim = "Ahmet"
yas = 30
formatli_string = f"Benim adım {isim} ve {yas} yaşındayım."  # 'Benim adım Ahmet ve 30 yaşındayım.'

# Çok satırlı stringler
cok_satirli_string = """Bu bir
çok satırlı
stringdir."""

print(cok_satirli_string)
