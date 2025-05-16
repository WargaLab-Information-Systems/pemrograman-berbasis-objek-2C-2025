class Kucing:
    def __init__(self, nama, jenis, warna):  
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def bersuara(self):
        print(f"{self.nama} adalah kucing jenis {self.jenis} dan berwarna {self.warna} yang bersuara: Meow")

    def aksi(self):
        print(f"{self.nama} sedang makan ikan.")
        print("\n=============================")


class Anjing:
    def __init__(self, nama, jenis, warna): 
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
        

    def bersuara(self):
        print(f"{self.nama} adalah anjing jenis {self.jenis} dan berwarna {self.warna} yang bersuara: Guk")

    def aksi(self):
        print(f"{self.nama} sedang berlari mengejar sesuatu.")
        print("\n=============================")

class Burung:
    def __init__(self, nama, jenis, warna): 
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def bersuara(self):
        print(f"{self.nama} adalah burung jenis {self.jenis} dan berwarna {self.warna} yang bersuara: Cuit")

    def aksi(self):
        print(f"{self.nama} sedang terbang di langit.")


# Membuat objek dari ketiga class
hewan1 = Kucing("Moggie","persia","putih")
hewan2 = Anjing("Coco", "Pudel","coklat")
hewan3 = Burung("Elvis", "Cendrawasih","kuning")

hewan_list = [hewan1, hewan2, hewan3]

print("\n==== Contoh Hewan ====")
for hewan in hewan_list:
    hewan.bersuara()
    hewan.aksi()