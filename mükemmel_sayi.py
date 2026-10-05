"""Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. 
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""

print("""
********************************************
MÜKEMMEL SAYI BULMA PROGRAMI

Çıkmak için q ya basın.
********************************************
""")

while True:
    n = input("Bir sayı giriniz: ")
    tam_bolenler = []
    
    if n == "q":
        print("Aa neden çıktınız ki :(")
        break
    
    n = int(n)
    i = 1
    while i < n:
        if n % i == 0:
            tam_bolenler.append(i)
        i += 1
    print(f"kendisi hariç tam bölenleri: {tam_bolenler}")

    total = 0
    for j in tam_bolenler:
        total += j


    if total == n:
        print("Bu bir mükemmel sayıdır.")
    else:
        print("mükemmel sayı değildir.")
        
    

    


