"""Burada list comprehension kullanarak 1'den 100'e kadar olan sayılardan 
sadece çift sayıları bir listeye atmayı yapmayı çalışın"""



cift_sayilar = []

for i in range(1,101):

    if i % 2 == 0:
        cift_sayilar.append(i)
    
print(cift_sayilar)
