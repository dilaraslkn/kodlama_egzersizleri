import math 

from math import factorial, log2, pow

print("""
      
****************************
HESAP MAKİNESİ
****************************
İŞLEMLER:
1- FAKTÖRİYEL ALMA
2- 2 TABANINDA LOGARİTMA ALMA
3- KUVVETİNİ ALMA
4- ÇIKIŞ
""")



while True:
    islem = input("Bir işlem seçiniz: ")

    if islem == "1":
        sayi = input("bir sayı giriniz: ")
        print(factorial(int(sayi)))

    elif islem == "2":
        sayi = input("bir sayı giriniz: ")
        print(log2(int(sayi)))
    
    elif islem == "3": 
        sayi1 = input("üssü alınacak sayı: ")
        sayi2 = input("üssü: ")
        print(pow(int(sayi1),int(sayi2)))
    
    elif islem == "4":
        break
    
    else:
        print("geçersiz işlem!")

        
