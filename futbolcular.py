"""
"futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta
oynayan futbolcuları rastgele yerleştirin. 
Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
"""



with open("furbolcular.txt", "r", encoding = "utf-8") as file:

    for i in file:
        i = i.strip()
        liste = i.split(",")
        isim = liste[0]


        
        if (liste[1] == "Galatasaray"):
            with open("gs.txt", "a", encoding = "utf-8") as file2:   
                    file2.write(isim + "\n")

        elif (liste[1] == "Fenerbahçe"):
            with open("fb.txt", "a", encoding = "utf-8") as file3:
                    file3.write(isim + "\n")

        else:
            with open("bjk.txt", "a", encoding = "utf-8") as file4:
                    file4.write(isim + "\n")


            




    

