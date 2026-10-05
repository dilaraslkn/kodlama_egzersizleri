"""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. 
Bu fonksiyon, eğer sayı çift ise *return* ile bu değeri dönsün. 
Ancak sayı tek sayı ise fonksiyon *raise* ile *ValueError* hatası fırlatsın. 
Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın 
ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın
"""


def cift(number):
    if (number % 2 != 0):
        raise ValueError("Bu sayı çift bir sayı değildir!")
    
    return number

sayilar = [1,4,89,34,90,23,67,456,871]


for i in sayilar:
    try:
        print(cift(i))
    except ValueError:
        pass






    
