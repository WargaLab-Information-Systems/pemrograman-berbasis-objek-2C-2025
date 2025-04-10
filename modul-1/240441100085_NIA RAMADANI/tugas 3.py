class Kucing:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def suara(self):
        print(f"{self.nama} kucing isti berjenis {self.jenis} berteriak: Meong\n")

class Harimau:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def suara(self):
        print(f"{self.nama} harimau milik alshad ahmad yang berwarna {self.warna} itu sedang mengaum: Raawrr\n")

class Sapi:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat

    def suara(self):
        print(f"{self.nama} sapi milik irfan hakim seberat {self.berat} kg itu akan disembelih dan berteriak : Mooo")

kucing1 = Kucing("Ciko", "Persia")
harimau1 = Harimau("Jinora", "Hitam putih")
sapi1 = Sapi("Momo", 1000)

hewan_list = [kucing1, harimau1, sapi1]

print("\n===================== SUARA HEWAN =====================\n")
for hewan in hewan_list:
    hewan.suara()
