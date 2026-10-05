def tamBolen(num):
    tamBolenler = []
    i = 1
    while i <= num:
        if num % i == 0:
            tamBolenler.append(i)
        i += 1

    return tamBolenler




def check_asal(sayi):
    list1 = tamBolen(sayi)
    list2 = [1, sayi]  

    if list1 == list2:
        print(f"{sayi} bir asal sayıdır.")
    
    else:
        print(f"{sayi} bir asal sayı değildir.")
    

check_asal(int(input("bir sayı giriniz: ")))






















def check_asal(num):
    tamBolenler = []

