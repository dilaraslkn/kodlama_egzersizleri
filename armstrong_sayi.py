"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
(3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

print("""
********************************************
ARMSTRONG SAYI BULMA PROGRAMI

Çıkmak için q ya basın.
********************************************
""")

while True:
    n = input("Bir sayı giriniz: ")
    olusturan_rakamlar = []

    if n == "q":
        print("Aa neden çıktınız ki :(")
        break
    

    for i in n:
        olusturan_rakamlar.append(i)
    
    print(olusturan_rakamlar)
    total = 0
    for j in olusturan_rakamlar:
        j = int(j)
        j **= len(n)
        total += j 
    print(total)
    
    n = int(n)
    if total == n:
        print("Bu sayı bir Armstrong sayıdır.")

    else: 
        print("Bu sayı bir Armstrong sayı değildir.")















