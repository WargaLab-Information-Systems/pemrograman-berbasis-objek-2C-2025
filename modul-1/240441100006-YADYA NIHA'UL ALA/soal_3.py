class Ikan:
    def __init__(self, nama, jenis, habitat):
        self.nama = nama
        self.jenis = jenis
        self.habitat = habitat
    
    def berenang(self):
        print(f"{self.nama} adalah ikan jenis {self.jenis} yang berenang di {self.habitat}.")

class Burung:
    def __init__(self, nama, jenis, habitat, suara):
        self.nama = nama
        self.jenis = jenis
        self.habitat = habitat
        self.suara = suara
    
    def berkicau(self):
        print(f"{self.nama}, yang berjenis {self.jenis}, dan berkicau: '{self.suara}'")

class Serangga:
    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara

    def bersuara(self):
        print(f"{self.nama} adalah serangga {self.jenis} dengan bunyi '{self.suara}'")

daftar_ikan = [("Hiu", "Karnivora", "Laut dalam"), ("Cupang", "Omnivora", "Air tawar"), ("Lele", "Omnivora", "Sungai")]
daftar_burung = [("Elang", "Karnivora", "Pegunungan", "Kiieek!"), ("Merpati", "Herbivora", "Perkotaan", "Krru~ Krru~"), ("Beo", "Omnivora", "Hutan", "Halo!")]
daftar_serangga = [("Jangkrik", "Omnivora","Kriik kriik"), ("Kupu-kupu", "Herbivora", "Senyaaap"), ("Semut", "Omnivora", "... (tidak bersuara)")]

list_ikan = [Ikan(nama, jenis, habitat) for nama, jenis, habitat in daftar_ikan]
list_burung = [Burung(nama, jenis, habitat, suara) for nama, jenis, habitat, suara in daftar_burung]
list_serangga = [Serangga(nama, jenis, suara) for nama, jenis, suara in daftar_serangga]

print("\n")
    
for ikan in list_ikan:
    ikan.berenang()
print("\n")
    
for burung in list_burung:
    burung.berkicau()
print("\n")
    
for serangga in list_serangga:
    serangga.bersuara()
print("\n")