class kucing :
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
    
    def mengeong(self):
        return f"Si Kucing {self.nama} itu suka mengeong malam-malam."
    
    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Warna : {self.warna}")

class singa :
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def mengaum(self):
        return f"Si Singa {self.nama} itu suka mengaum jika lapar."
    
    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Warna : {self.warna}")


class ayam :
    def __init__(self, nama, jenis,warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def berkokok(self):
        return f"Si Ayam {self.nama} itu selalu berkokok di pagi hari."
    
    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Jenis : {self.jenis}")
        print(f"Warna : {self.warna}")


kucing_data = [("Muhammad Sumbul", "Persia", "Putih"), ("Khalid Kashmiri", "Bengal", "Coklat")]
singa_data = [("Leo", "Sumatera", "Kuning"), ("Simba", "Barbary", "Coklat")]
ayam_data = [("Chiki", "Ayam Hutan", "Hitam"),("Bobby", "Ayam Petelur", "Putih")]

kucing_list = []
for data in kucing_data:
    kucing_list.append(kucing(*data))

singa_list = []
for data in singa_data:
    singa_list.append(singa(*data))

ayam_list = []
for data in ayam_data:
    ayam_list.append(ayam(*data))

for kucing in kucing_list:
    kucing.tampilkan_info()
    print(kucing.mengeong())
    print()

for singa in singa_list:
    singa.tampilkan_info()
    print(singa.mengaum())
    print()

for ayam in ayam_list:
    ayam.tampilkan_info()
    print(ayam.berkokok())
    print()
