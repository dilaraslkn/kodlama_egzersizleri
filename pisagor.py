"""1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.
(a <= 100,b <= 100)"""




def pisagor():
    sonuclar = []
    sayilar = list(range(1,101))

    for i in sayilar:
        for j in sayilar:
            for k in sayilar:
                if i<j<k and  i**2 + j**2 == k**2:
                    sonuclar.append((i,j,k))
    return sonuclar

print(pisagor())



