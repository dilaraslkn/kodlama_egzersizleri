"""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. 
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)."""

def tamBolen(num):
    tamBolenler = []
    i = 1
    while i < num:
        if num % i == 0:
            tamBolenler.append(i)
        i += 1

    return tamBolenler


def mukemmelSayi(sayi):
    sum = 0
    for i in tamBolen(sayi):
        sum += i
        
    return sum == sayi
       

result = list(range(1, 1000))

print(list(filter(mukemmelSayi, result)))   # fonksiyonun sadece adını yaz



