print("""
*****************************
Faktöriyel Bulma Programı

Çıkmak için q ya basınız.
*****************************
""")




while True:
    n = (input("Bir sayı giriniz: "))
    faktöriyel = 1

    if n == "q":
        break

    n = int(n)
    if n == 0:
        faktöriyel = 1

    else:
        while n > 0:
            faktöriyel *= n
            n -= 1

    print(f"Faktöriyel: {faktöriyel}")
