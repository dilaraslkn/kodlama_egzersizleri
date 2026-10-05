"""
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.
liste = ["345","sadas","324a","14","kemal"]
Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. 
Bunu yaparken try,except bloklarını kullanmayı unutmayın
"""


liste = ["345","sadas","324a","14","kemal"]

def rakam():
    list = []
    for i in liste:
        try:
            int(i)
            list.append(i)
            
        except:
            print(f"{i} sadece rakamlardan oluşmuyor")
    print(list)

rakam()

