class Urun:
    def __init__(self,isim,fiyat,stok):
        self.isim=isim
        self.fiyat=fiyat
        self.stok=stok
    def bilgi(self):
        print(f"Ürün:{self.isim},Fiyat:{self.fiyat},Stok:{self.stok}")
class Elektronik(Urun):
    def __init__(self,isim,fiyat,stok,garanti):
        super().__init__(isim,fiyat,stok)
        self.garanti=garanti
    def bilgi(self):
        super().bilgi()
        print(f"Garanti:{self.garanti} yıl")
class Giyim(Urun):
    def __init__(self,isim,fiyat,stok,beden):
        super().__init__(isim,fiyat,stok)
        self.beden=beden
    def bilgi(self):
        super().bilgi()
        print(f"Beden:{self.beden}")
telefon=Elektronik("Akıllı telefon",5000,30,2)
tişört=Giyim("Tişört",100,50,"M")
telefon.bilgi()
print()
tişört.bilgi()
