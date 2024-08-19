# GlobalAI_PythonBootcamp
Taş kağıt makas oyunu

tas_kagit_makas_TUBA_CALCİ(): adlı bir fonksiyon oluşturdum.
Öncelikle oyunun giriş yazısı ve kurallarını belirten yazı ekledim.

ilk olarak oynananOyun değişkenine 0 değerini atadım. Her oyun oynandığında while döngüsü içinde bu sayı 1 artacak.
oyuncuGalibiyeti, bilgisayarGalibiyeti ve turSayisi değişkenlerine de 0 değerlerini verdim. Duruma göre artacak şekilde ayarladım.

["taş", "kağıt", "makas"] şeklinde secenekler adında bir liste tanımladım.

yeni bir while döngüsünde oyun devam edecek. bu döngü bilgisayarGalibiyet veya oyuncuGalibiyet 2 olana kadar dönecek.

Ardından oyuncuHamle ile oyuncudan bir girdi istedik. çıkmak istiyorsa çıkış yazmalı. burada return olacak.
ardından bilgisayarHamle'ye secenekler listesinden random seçim yaptırdık.

Taş, kağıt, makas kazanma durumuna göre koşulları oluşturduk.
Berabere durumunda ekrana beraberlik yazılacak.
Oyuncu veya bilgisayar kazanırsa kazanan ekrana yazdırılacak ve galibiyet değişkeni 1 artacak.

ardından ekrana genel durum yazdırılacak.


ardından galibiyet durumu ekrana yazdırılacak.

oyuna devam edip etmeme isteği de kullaniciYeniİstek ile kullanıcıya sorulacak.
Hayır derse break ile döngüden çıkılacak.
Bilgisayara da bu istek random ile sorulacak.
Hayır derse döngüden çıkılacak.

Evet demeleri durumunda döngü devam edecek.

Galibiyet durumlarında ekrana yazdırılan Oynanan Oyun: {oynananOyun} ve Tur sayısı: {turSayisi} kısmında oyunun ne kadar sürdüğü yani kaç oyun ve kaç tur oynadıkları da ekrana yazdırılmış olacak.
