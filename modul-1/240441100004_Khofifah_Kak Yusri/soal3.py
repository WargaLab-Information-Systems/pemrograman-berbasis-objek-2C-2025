class Hewan:
    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara
    
    def bersuara(self):
        print(f"{self.nama} berjenis {self.jenis} berbunyi {self.suara}")

hewan_list = [
    ("Kucing", "Persia", "Meong"),
    ("Kambing", "Pygmy", "Mbeek-Mbeek"),
    ("Ayam", "Kampung", "Kukuruyuk")
]

objek_hewan = []
for nama, jenis, suara in hewan_list:
    objek_hewan.append(Hewan(nama, jenis, suara))

for hewan in objek_hewan:
    hewan.bersuara()
