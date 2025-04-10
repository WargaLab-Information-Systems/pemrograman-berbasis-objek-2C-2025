class kucing:
    def __init__(self, jenis, makanan, suara):
        self.jenis = jenis
        self.makanan = makanan
        self.suara = suara

    def tampilkan_info(self):
        print(f"kucing - Jenis: {self.jenis}, Makanan: {self.makanan}, Suara: {self.suara} ")

class anjing:
    def __init__(self, jenis, makanan, suara):
        self.jenis = jenis
        self.makanan = makanan
        self.suara = suara

    def tampilkan_info(self):
        print(f"Anjing - Jenis: {self.jenis}, Makanan: {self.makanan}, Suara: {self.suara} ")

class sapi:
    def __init__(self, jenis, makanan, suara):
        self.jenis = jenis
        self.makanan = makanan
        self.suara = suara

    def tampilkan_info(self):
        print(f"sapi - Jenis: {self.jenis}, Makanan: {self.makanan}, Suara: {self.suara} ")

data_kucing =[("Persia", "Ikan", "Meong"), ("Anggora", "Daging", "miaww"), ("Kampung", "Tempe", "Meoong")]
data_anjing = [("Bulldog", "Tulang", "GukGuk"),("Beagle", "Ayam", "Guk"), ("Maltese", "Tulang", "GukGukGuk")]
data_sapi = [("Limousin", "Rumput", "Moo"), ("Simmental", "Rumput", "Mooo"), ("Brahma", "Rumput", "Moooo")]

print("=== Data Kucing ===")
for jenis, makanan, suara in data_kucing:
    hewan_kucing = kucing(jenis, makanan, suara)
    hewan_kucing.tampilkan_info()

print("=== Data Anjing ===")
for jenis, makanan, suara in data_anjing:
    hewan_anjing = anjing(jenis, makanan, suara)
    hewan_anjing.tampilkan_info()

print("=== Data Sapi ===")
for jenis, makanan, suara in data_sapi:
    hewan_sapi = sapi(jenis, makanan, suara)
    hewan_sapi.tampilkan_info()