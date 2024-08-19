import random
def tas_kagit_makas_TUBA_CALCİ():


    print("Taş-kağıt-makas oyununa hoş gelniniz. ")
    print("Taş-kağıt-makas arasından 1 seçim yapacaksınız. Karşınızda bir bilgisayar var.")
    print("Kağıt taşı yener. Makas kağıdı yener. Taş makası yener.")
    print("2 tur oynanacak. 2'ye ulaşan kazanır")
    print("Oyundan çıkmak istediğinde 'çıkış' yaz")
    print("her tur sonunda devam ediğ etmek istemediğiniz sorulacak")




    oynananOyun = 0

    while True:
        print("oyuna hoş geldiniz.")
        oynananOyun += 1

        oyuncuGalibiyet = 0
        bilgisayarGalibiyet = 0
        turSayisi = 0

        secenekler = ["taş", "kağıt", "makas"]

        while (bilgisayarGalibiyet < 2) and(oyuncuGalibiyet < 2):
            turSayisi += 1

            oyuncuHamle = input("taş-kağıt-makas? veya 'çıkış'")
            if oyuncuHamle == "çıkış":
                print("Çıkış yapılıyor...")
                return
            

            bilgisayarHamle = random.choice(secenekler)
            print(f"Bilgisayar: {bilgisayarHamle}")

            if (oyuncuHamle) == (bilgisayarHamle):
                print(f"Oyuncu: {oyuncuHamle} Bilgisayar: {bilgisayarHamle} - SONUÇ: Berabere")  
            elif (oyuncuHamle == "taş") and (bilgisayarHamle == "makas") or \
                (oyuncuHamle == "kağıt") and (bilgisayarHamle == "taş") or \
                (oyuncuHamle == "makas") and (bilgisayarHamle == "kağıt"):
                print("Oyuncu kazandı")
                oyuncuGalibiyet += 1
            else:
                bilgisayarGalibiyet += 1

            print(f"Durum: Oyuncu: {oyuncuGalibiyet} - Bilgisayar: {bilgisayarGalibiyet}")



        if(oyuncuGalibiyet == 2):
            print(f"Oyuncu kazandı. Oynanan Oyun: {oynananOyun} ve Tur sayısı: {turSayisi}")
        else:
            print(f"Bilgisayar kazandı.Oynanan Oyun: {oynananOyun} ve Tur sayısı: {turSayisi}")



        kullaniciYeniİstek = input("Oyuna devam edilsin mi? (evet/hayır)")
        if kullaniciYeniİstek == "hayır":
            print("Çıkış yapılıyor...")
            break

        bilgisayarYeniİstek = random.choice(["evet", "hayır"])
        print(f"Bilgisayarın kararı: {bilgisayarYeniİstek}")
        if bilgisayarYeniİstek == "hayır":
            print("Çıkış yapılıyor...")
            break





        


        


tas_kagit_makas_TUBA_CALCİ()

















