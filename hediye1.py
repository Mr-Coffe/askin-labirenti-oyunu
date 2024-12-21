import time

def clear_screen():
  """Terminal ekranını temizler."""
  print("\033c", end="")

def print_slow(text, delay=0.04):
    """Metni yavaş yavaş yazdırır."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def giris_mesaji():
    clear_screen()
    print_slow("Aşkın Labirenti'ne hoş geldin, sevgili maceraperest...")
    print_slow("Bu labirent, kalbimizin en gizli köşelerini, hem flört anılarımızı hem de şimdiki aşkımızı saklıyor...")
    print_slow("Acaba bu labirentin büyüsüne kapılmaya hazır mıyız?")
    while True:
        isim = input("Lütfen adını gir (Medine/Bora): ").lower()
        if isim in ["medine", "bora"]:
           return isim
        else:
            print_slow("Lütfen 'Medine' veya 'Bora' yazarak başla.")

def labirent_girisi(oyuncu_ismi):
    clear_screen()
    print_slow("Labirentin girişindeyiz, kalplerimiz heyecanla çarpıyor...")
    print_slow("Etrafımız devasa duvarlarla çevrili, yollar sanki kalbimizin derinliklerine uzanıyor.")
    print_slow("Ama el ele, bu aşk labirentinin sırlarını çözeceğimize inanıyorum.")
    print_slow("")
    if oyuncu_ismi == "medine":
      print_slow("Labirentin ilk sırrı, bizim ilk tanıştığımız, o büyülü an...")
      print_slow("Hangi film serisi kalbimize dokunmuş, bizi birbirimize yakınlaştırmıştı?")

      while True:
        cevap = input("> ").lower()
        if cevap == "twilight":
           print_slow("Doğru! Vampirler ve kurt adamlar, bizim aşkımızın perdesini aralamıştı.")
           break
        else:
          print_slow("Yanlış cevap. Labirentin duvarları sana sanki seni yutacakmış gibi geliyor,tekrar dene.")
      print_slow("")
      print_slow("Şimdi ise aşkımızın melodisine ihtiyacımız var...")
      print_slow("Hangi şarkılar kalbimizi bir araya getiren notalar gibiydi?")
      sarkilar = ["the neighborhood", "aşk ağlama ben ağlarım", "senden daha güzel", "seni kendime sakladım", "dinle beni bi", "sen varsın diye"]
      while True:
        cevap = input(f"Şarkıyı tahmin et ({', '.join(sarkilar)}): ").lower()
        if cevap in sarkilar:
            if cevap == "the neighborhood":
                print_slow("Doğru! 'Sweater Weather' o gün içimizi ısıtmış, aşkımızın sesini fısıldamıştı.")
            elif cevap == "aşk ağlama ben ağlarım":
                print_slow("Doğru! Bu şarkı sanki bizim iç sesimiz, kalbimizin fısıltısı.")
            elif cevap == "senden daha güzel":
               print_slow("Doğru! Gözlerindeki güzellik, bu labirenti aydınlatıyor.")
            elif cevap == "seni kendime sakladım":
                 print_slow("Doğru! Seni kalbime kazıdım, bu labirentte kaybolmam mümkün değil.")
            elif cevap == "dinle beni bi":
                print_slow("Doğru! Sadece seni dinliyorum, sen benim pusulam oldun.")
            elif cevap == "sen varsın diye":
                 print_slow("Doğru! Senin varlığın, bu labirenti bir cennete dönüştürüyor.")
            break
        else:
            print_slow("Yanlış cevap, kalbinin sesini tekrar dinle, bir şansın daha var.")
            while True:
                cevap2 = input("Tekrar dene: ").lower()
                if cevap2 in sarkilar:
                   if cevap2 == "the neighborhood":
                        print_slow("Doğru! 'Sweater Weather' o gün içimizi ısıtmış, aşkımızın sesini fısıldamıştı.")
                   elif cevap2 == "aşk ağlama ben ağlarım":
                       print_slow("Doğru! Bu şarkı sanki bizim iç sesimiz, kalbimizin fısıltısı.")
                   elif cevap2 == "senden daha güzel":
                       print_slow("Doğru! Gözlerindeki güzellik, bu labirenti aydınlatıyor.")
                   elif cevap2 == "seni kendime sakladım":
                        print_slow("Doğru! Seni kalbime kazıdım, bu labirentte kaybolmam mümkün değil.")
                   elif cevap2 == "dinle beni bi":
                        print_slow("Doğru! Sadece seni dinliyorum, sen benim pusulam oldun.")
                   elif cevap2 == "sen varsın diye":
                       print_slow("Doğru! Senin varlığın, bu labirenti bir cennete dönüştürüyor.")
                   break
                else:
                     print_slow("Yanlış cevap. Ama merak etme, ben sana yardım edeceğim, bu labirentte asla yalnız kalmayacağız.")
                     break
            break

      print_slow("Labirentin duvarları arasında bir şiir yankılanıyor:")
      print_slow("""
      Gözlerin gökyüzü, kalbin bir deniz,
      Aşkınla açtım ben sonsuz bir yol.
      Sen varsın ya, karanlık aydınlanır,
      Benimle ol, bu labirentte sonsuz kal.
      """)
    elif oyuncu_ismi == "bora":
        print_slow("Labirentin ilk sırrı, senin büyülendiğin o dünya...")
        print_slow("Hangi film, hayal gücünü harekete geçirmiş, kalbini heyecanlandırmıştı?")
        while True:
            cevap = input("> ").lower()
            if cevap == "labirent":
               print_slow("Doğru! Labirentlerin gizemli dünyası, senin de kalbine kazınmış.")
               break
            else:
                print_slow("Yanlış cevap, kalbinin sesini tekrar dinle. Tekrar dene.")
        print_slow("")
        print_slow("Şimdi ise, bu aşk labirentindeki melodiyi hatırlayalım...")
        print_slow("Hangi şarkılar kalbimizin ritmi gibiydi?")
        sarkilar = ["raf", "aşk ağlama ben ağlarım", "senden daha güzel", "seni kendime sakladım", "dinle beni bi", "sen varsın diye"]
        while True:
             cevap = input(f"Şarkıyı tahmin et ({', '.join(sarkilar)}): ").lower()
             if cevap in sarkilar:
                if cevap == "raf":
                    print_slow("Doğru! 'Güneş' içimizi ısıtmış, labirentin karanlığını aydınlatmıştı.")
                elif cevap == "aşk ağlama ben ağlarım":
                    print_slow("Doğru! Bu şarkı sanki bizim iç sesimiz, kalbimizin fısıltısı.")
                elif cevap == "senden daha güzel":
                    print_slow("Doğru! Gözlerindeki güzellik, bu labirenti aydınlatıyor.")
                elif cevap == "seni kendime sakladım":
                    print_slow("Doğru! Seni kalbime kazıdım, bu labirentte kaybolmam mümkün değil.")
                elif cevap == "dinle beni bi":
                    print_slow("Doğru! Sadece seni dinliyorum, sen benim pusulam oldun.")
                elif cevap == "sen varsın diye":
                    print_slow("Doğru! Senin varlığın, bu labirenti bir cennete dönüştürüyor.")
                break
             else:
                  print_slow("Yanlış cevap, kalbinin sesini tekrar dinle, bir şansın daha var.")
                  while True:
                        cevap2 = input("Tekrar dene: ").lower()
                        if cevap2 in sarkilar:
                           if cevap2 == "raf":
                                print_slow("Doğru! 'Güneş' içimizi ısıtmış, labirentin karanlığını aydınlatmıştı.")
                           elif cevap2 == "aşk ağlama ben ağlarım":
                                 print_slow("Doğru! Bu şarkı sanki bizim iç sesimiz, kalbimizin fısıltısı.")
                           elif cevap2 == "senden daha güzel":
                                 print_slow("Doğru! Gözlerindeki güzellik, bu labirenti aydınlatıyor.")
                           elif cevap2 == "seni kendime sakladım":
                                print_slow("Doğru! Seni kalbime kazıdım, bu labirentte kaybolmam mümkün değil.")
                           elif cevap2 == "dinle beni bi":
                                print_slow("Doğru! Sadece seni dinliyorum, sen benim pusulam oldun.")
                           elif cevap2 == "sen varsın diye":
                                print_slow("Doğru! Senin varlığın, bu labirenti bir cennete dönüştürüyor.")
                           break
                        else:
                             print_slow("Yanlış cevap. Ama merak etme, ben sana yardım edeceğim, bu labirentte asla yalnız kalmayacağız.")
                             break
                  break
    print_slow("Labirentin duvarları arasında bir aşk şiiri yankılanıyor:")
    print_slow("""
        Sen bir labirent, ben yolunu kaybetmiş,
        Aşkınla buldum kendimi, canım.
        Gözlerin bir ışık, yolumu aydınlatan,
        Sen varsın ya, labirentte sonsuz kalalım.
    """)
    return "avm_bulusmasi_labirent"

def avm_bulusmasi_labirent():
    clear_screen()
    print_slow("Labirentin ortasında, sanki bir Avm'ye adım attık...")
    print_slow("LCW ve Defacto'nun yanından geçerken, kalplerimiz birbirine daha çok yaklaştı.")
    print_slow("Yemek yedik, kahvelerimizi yudumladık, sohbetler ettik... O gün, sanki labirentte bir vaha gibiydik.")
    print_slow("Sonra bir sarılış... Aşkımızın tohumları, o an filizlenmeye başlamıştı.")
    return "sevgili_olma_labirent"

def sevgili_olma_labirent():
    clear_screen()
    print_slow("Labirentin sonunda, aşkımızın en özel anına ulaştık...")
    print_slow("17 Aralık'ı 18 Aralık'a bağlayan gece, saat 1 gibi... Kalplerimiz bir oldu.")
    print_slow("Artık bu labirentte sonsuza dek birlikte yolculuk yapacağız, sevgili olarak...")
    print_slow("Seni çok seviyorum, hayatımın anlamı! ❤️")
    return "bitti"

# Oyunun başlangıcı
konum = "giris"
oyuncu_ismi = None


while konum != "bitti":
    if konum == "giris":
        oyuncu_ismi = giris_mesaji()
        konum = "labirent_girisi"
    elif konum == "labirent_girisi":
        konum = labirent_girisi(oyuncu_ismi)
    elif konum == "avm_bulusmasi_labirent":
        konum = avm_bulusmasi_labirent()
    elif konum == "sevgili_olma_labirent":
         konum = sevgili_olma_labirent()
    else:
        print_slow("Hata! Bilinmeyen bir yere girdin.")
        break

print_slow("Oyun bitti. Seni her zaman, her yerde seviyorum! ❤️")