"""Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın."""


a = int(input("Bir sayı giriniz: "))
b = int(input("Bir sayı giriniz: "))


def tamBolen(num):
    tamBolenler = []
    i = 1
    while i <= num:
        if num % i == 0:
            tamBolenler.append(i)
        i += 1

    return tamBolenler

def ebob(sayi1, sayi2):
    ortakBolenler = []
    for i in tamBolen(sayi1):
        for j in tamBolen(sayi2):
            if i == j:
                ortakBolenler.append(i)
    return max(ortakBolenler)

print(ebob(a, b))
