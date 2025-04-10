class Burung:
    def __init__(self, nama, warna, jenis):
        self.nama = nama
        self.warna = warna
        self.jenis = jenis

    def info(self):
        print(f"Burung yang bernama {self.nama} memiliki warna {self.warna} dan berjenis {self.jenis}")

    def aksi(self):
        print(f"{self.nama} sedang terbang tinggi di udara")
        
    def suara(self):
        print(f"{self.nama} bersuara cuit-cuit")

class Kucing:
    def __init__(self, nama, warna, jenis):
        self.nama = nama
        self.warna = warna
        self.jenis = jenis

    def info(self):
        print(f"Kucing yang bernama {self.nama} memiliki warna {self.warna} dan berjenis {self.jenis}")

    def aksi(self):
        print(f"{self.nama} sedang bermain")
        
    def suara(self):
        print(f"{self.nama} bersuara meong")
        
class Anjing:
    def __init__(self, nama, warna, jenis):
        self.nama = nama
        self.warna = warna
        self.jenis = jenis

    def info(self):
        print(f"Anjing yang bernama {self.nama} memiliki warna {self.warna} dan berjenis {self.jenis}")

    def aksi(self):
        print(f"{self.nama} sedang berlari-lari dengan ceria")

    def suara(self):
        print(f"{self.nama} bersuara guk-guk")

hewan_list = [
    Kucing("ayu", "Abu-abu", "Persia"),
    Kucing("unyil", "Putih", "Munchkin"),
    Burung("Fajar", "Biru Cerah", "Lovebird"),
    Burung("Mimi", "Coklat", "Pipit"),
    Anjing("Faisal", "Hitam", "Pudel"),
    Anjing("Yoga", "Putih Hitam", "Buldog")
] 

for hewan in hewan_list:
    hewan.info()
    hewan.aksi()
    hewan.suara()
    print("=" * 30)