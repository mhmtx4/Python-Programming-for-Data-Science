# SANAL ORTAM LİSTELEMESİ
# Bu komut, conda tarafından yönetilen mevcut sanal ortamları listeler.
# Sanal ortamlar, projeler arası bağımsızlık sağlar, her proje için ayrı Python ve paket sürümleri kullanmanıza olanak tanır.
conda env list

# SANAL ORTAM OLUŞTURMA
# Bu komut ile yeni bir sanal ortam oluşturulur. "-n" parametresi ile ortamın ismi belirlenir.
# Sanal ortam oluşturmak, bağımsız bir çalışma alanı sağlamak için çok önemlidir.
conda create -n isim

# Ortamı bir YAML dosyası kullanarak oluşturmak da mümkündür.
# "environment.yaml" dosyası, ortamın kurulacağı paketleri ve sürümleri içerir.
conda env create -f environment.yaml

# SANAL ORTAMI AKTİF ETME (ORTAMA GİRİŞ)
# Bu komut, belirli bir sanal ortamı aktif hale getirir.
# Aktif olan ortamda, o ortama özgü Python ve yüklü paketler kullanılır.
conda activate isim

# SANAL ORTAMI DEAKTİF ETME (ORTAMDAN ÇIKIŞ)
# Bu komut ile aktif olan sanal ortamdan çıkılır.
# Çıkıldığında sistem genelindeki Python ve paketler tekrar kullanıma açılır.
conda deactivate

# SANAL ORTAM SİLME
# Belirtilen sanal ortamı sistemden tamamen kaldırır.
# "-n" parametresi ile silinecek ortamın adı belirtilir.
conda env remove -n isim

# ORTAM İÇİNDEKİ PAKETLERİ GÖRME
# Bu komut, aktif olan sanal ortamda yüklü tüm paketlerin listesini verir.
# Bu liste, paketlerin isimlerini, sürümlerini ve hangi kanaldan yüklendiklerini gösterir.
conda list

# ORTAMA PAKET YÜKLEME
# Sanal ortama belirli bir paketi yükler.
# Yüklemek istediğin paketin ismini belirterek, conda repolarından indirip kurmasını sağlarsın.
conda install isim

# Bir örnek:
conda install numpy

# AYNI ANDA BİRDEN FAZLA PAKET YÜKLEME
# Birden fazla paketi aynı anda yüklemek de mümkündür. Paketin isimlerini aralarına boşluk koyarak yazabilirsin.
conda install numpy scipy pandas

# PAKET SİLME
# Sanal ortamdan belirli bir paketi kaldırır.
# Paketin ismini belirttiğinde, o paket ortamdan tamamen silinir.
conda remove isim

# İSTENİLEN SÜRÜM PAKETİ YÜKLEME
# Belirli bir paketin istenilen sürümünü yükler.
# "=" işareti ile paket sürümü belirtilir. Eğer belirtilmezse en son sürüm yüklenir.
conda install numpy=1.20.1

# PAKET YÜKSELTME
# Sanal ortamda yüklü olan bir paketi en son sürümüne günceller.
conda upgrade isim

# Örnek:
conda upgrade numpy

# TÜM PAKETLERİ YÜKSELTME
# Bu komut, sanal ortamda yüklü olan tüm paketleri en son sürümlerine günceller.
conda upgrade --all

# PIP İLE PAKET YÖNETİMİ
# Conda dışında, pip kullanarak da paket yükleyebilirsin.
# Pip, özellikle Python dünyasında yaygın olarak kullanılan bir paket yöneticisidir.

# PIP İLE PAKET YÜKLEME
# Bu komut, pip kullanarak bir Python paketini indirip kurar.
pip install paketadı

# Örnek:
pip install pandas

# PIP İLE BELİRLİ SÜRÜMDE PAKET YÜKLEME
# Belirli bir paket sürümünü yüklemek için "==" işaretini kullanırsın.
pip install paketadı==sürüm

# Örnek:
pip install pandas==2.1.1

# ENV OLUŞTURMA (CONDA İLE)
# Bu komut, mevcut sanal ortamı "environment.yaml" adlı bir dosyaya dışa aktarır.
# Bu dosya, ortamın tam bir yedeği gibi çalışır, böylece başka bir yerde aynı ortamı yeniden oluşturabilirsin.
conda env export > environment.yaml

# DOSYALARI GÖRÜNTÜLEME (Klasör içindekileri listeleme)
# Bu komut, o anki dizinde bulunan dosyaları listeler. 
# "dir" komutu özellikle Windows işletim sistemlerinde kullanılır.
dir
