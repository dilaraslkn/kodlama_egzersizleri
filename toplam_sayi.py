"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. 
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın
"""


print("""
********************************************
TOPLAM BULMA PROGRAMI

Toplam sonucu bulmak için q ya basın.
********************************************
""")


toplam = []
total = 0
while True:
    n = (input("Bir sayı giriniz: "))


    if n == "q":
        print(f"Yazdığınız bütün sayılar: {toplam}")
        print(f"Yazdığınız sayıların toplamı: {total}")
        break

    toplam.append(n)

    for i in toplam:
        i = int(i)
        total += i 
    
    
   