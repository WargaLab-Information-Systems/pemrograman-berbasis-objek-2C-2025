class Anjing:
    def __init__(self, nama, umur, ras):
        self.nama = nama
        self.umur = umur
        self.ras = ras

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)
        print("Ras :", self.ras)


class Kelinci:
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def tampilkan_info(self):
        print("Nama  :", self.nama)
        print("Umur  :", self.umur)
        print("Warna :", self.warna)


class Ikan:
    def __init__(self, nama, umur, habitat):
        self.nama = nama
        self.umur = umur
        self.habitat = habitat

    def tampilkan_info(self):
        print("Nama    :", self.nama)
        print("Umur    :", self.umur)
        print("Habitat :", self.habitat)


data_anjing = [
    ("Milo", 1, "Buldog"),
    ("Coco", 2, "Pudel"),
    ("Snowy", 1, "Husky")
]

data_kelinci = [
    ("Nana", 3, "Putih"),
    ("Cici", 1, "Hitam"),
    ("Luna", 2, "Coklat")
]

data_ikan = [
    ("Nemo", 11, "Laut"),
    ("Koi", 5, "Aquarium"),
    ("Cupang", 10, "Air tawar")
]

print("=== Data Anjing ===")
for nama, umur, ras in data_anjing:
    anjing = Anjing(nama, umur, ras)
    anjing.tampilkan_info()
    print()


print("=== Data Kelinci ===")
for nama, umur, warna in data_kelinci:
    kelinci = Kelinci(nama, umur, warna)
    kelinci.tampilkan_info()
    print()

print("=== Data Ikan ===")
for nama, umur, habitat in data_ikan:
    ikan = Ikan(nama, umur, habitat)
    ikan.tampilkan_info()
    print()
