class Hewan:
    def __init__(self, nama, makanan, suara):
        self.nama = nama
        self.makanan= makanan
        self.suara = suara
    
    def bersuara(self):
        print(f"{self.nama} berbunyi {self.suara}")

hewan_list = [
    ("ikan koi", "cacing", "blubuk blubuk"),
    ("Paus", "cumi,udang,ikan kecil", "rawrrrr"),
    ("monyet", "pisang", "uuaa uuaa")
]

objek_hewan = []
for nama, makanan, suara in hewan_list:
    objek_hewan.append(Hewan(nama, makanan, suara))

for hewan in objek_hewan:
    hewan.bersuara()
