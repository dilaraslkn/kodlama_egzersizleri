class Animals():
    def __init__(self, name, kind, habitat):
        self.name = name
        self.kind = kind
        self.habitat = habitat


    def __str__(self):
        return f"İsim: {self.name}\nTür: {self.kind}\nHabitatı: {self.habitat}"

    def ability(self):
        print(f"{self.name} yürüyebilir!")



class Dogs(Animals):
    def __init__(self, name, kind, habitat, color):
        super().__init__(name, kind, habitat)
        
        self.color = color

    def __str__(self):
        return f"İsim: {self.name}\nTür: {self.kind}\nHabitatı: {self.habitat}\nRengi: {self.color}"

    def ability(self):
        print(f"{self.name} yüzebilir!")

class Birds(Animals):
    
    def __init__(self, name, kind, habitat, flyability):
        super().__init__(name, kind, habitat)
        
        self.flyability = flyability

    def __str__(self):
        return f"İsim: {self.name}\nTür: {self.kind}\nHabitatı: {self.habitat}\nUçabilir mi?: {self.flyability}"


    def ability(self):

        if (self.flyability == "evet"):
            print(f"{self.name} uçabilir!")

        else:
            print(f"{self.name} uçamaz!")

class Horses(Animals):

    def __init__(self, name, kind, habitat, kindOfHorse):
        super().__init__(name, kind, habitat)
        
        self.kindOfHorse = kindOfHorse

    def __str__(self):
        return f"İsim: {self.name}\nTür: {self.kind}\nHabitatı: {self.habitat}\nAtın Türü: {self.kindOfHorse}"

    def ability(self):
        print(f"{self.name} çok hızlı koşabilir!")


dog1 = Dogs("Fino", "köpek", "karada yaşar", "siyah")
bird1 = Birds("Cikcik", "kuş", "havada yaşar", "evet")
bird2 = Birds("Gıdak", "kuş", "karada yaşar", "hayır")
horse1 = Horses("Rüzgar", "at", "karada yaşar", "mustang")

print(str(dog1))
print(str(bird1))

bird1.ability()

horse1.ability()


    
    
    
    

        
