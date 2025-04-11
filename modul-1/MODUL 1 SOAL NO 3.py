class Musang:
    def __init__(self, warna, jenis_kelamin, pemilik):
        self.warna = warna
        self.jenis_kelamin = jenis_kelamin
        self.pemilik = pemilik

    def tampilkan_hewan(self):
        print("=== Musang ===")
        print("Warna        :", self.warna)
        print("Jenis Kelamin:", self.jenis_kelamin)
        print("Pemilik      :", self.pemilik)
        print("=" * 30)

class Ayam:
    def __init__(self, warna, jenis_kelamin, pemilik):
        self.warna = warna
        self.jenis_kelamin = jenis_kelamin
        self.pemilik = pemilik

    def tampilkan_hewan(self):
        print("=== Ayam ===")
        print("Warna        :", self.warna)
        print("Jenis Kelamin:", self.jenis_kelamin)
        print("Pemilik      :", self.pemilik)
        print("=" * 30)

class Bebek:
    def __init__(self, warna, jenis_kelamin, pemilik):
        self.warna = warna
        self.jenis_kelamin = jenis_kelamin
        self.pemilik = pemilik

    def tampilkan_hewan(self):
        print("=== Bebek ===")
        print("Warna        :", self.warna)
        print("Jenis Kelamin:", self.jenis_kelamin)
        print("Pemilik      :", self.pemilik)
        print("=" * 30)

while True:
    jenis_hewan = input("Masukkan jenis hewan (Musang/Ayam/Bebek) atau 'selesai' untuk berhenti: ").lower()

    if jenis_hewan == "selesai":
        break

    if jenis_hewan not in ["musang", "ayam", "bebek"]:
        print("Jenis hewan tidak valid. Silakan masukkan 'Musang', 'Ayam', atau 'Bebek'.")
        continue

    warna = input("Masukkan warna hewan: ")
    jenis_kelamin = input("Masukkan jenis kelamin: ")
    pemilik = input("Masukkan nama pemilik: ")

    if jenis_hewan == "musang":
        musang = Musang(warna, jenis_kelamin, pemilik)
        musang.tampilkan_hewan()
    elif jenis_hewan == "ayam":
        ayam = Ayam(warna, jenis_kelamin, pemilik)
        ayam.tampilkan_hewan()
    elif jenis_hewan == "bebek":
        bebek = Bebek(warna, jenis_kelamin, pemilik)
        bebek.tampilkan_hewan()
