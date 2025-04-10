class Kucing:
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def suara(self):
        return f"{self.nama} mengeong: Meong!"

    def info(self):
        return f"Kucing bernama {self.nama}, umur {self.umur} tahun, warna {self.warna}."


class Anjing:
    def __init__(self, nama, ras, umur):
        self.nama = nama
        self.ras = ras
        self.umur = umur

    def suara(self):
        return f"{self.nama} menggonggong: Guk Guk!"

    def info(self):
        return f"Anjing bernama {self.nama}, ras {self.ras}, umur {self.umur} tahun."


class Burung:
    def __init__(self, nama, jenis, warna_bulu):
        self.nama = nama
        self.jenis = jenis
        self.warna_bulu = warna_bulu

    def suara(self):
        return f"{self.nama} berkicau: Cuit cuit!"

    def info(self):
        return f"Burung bernama {self.nama}, jenis {self.jenis}, warna bulu {self.warna_bulu}."

daftar_hewan = []

for i in range(3):
    print(f"\nInput data hewan ke-{i+1}:")
    jenis = input("Pilih jenis hewan (kucing/anjing/burung): ")

    if jenis == "kucing":
        nama = input("Nama kucing: ")
        umur = input("Umur kucing: ")
        warna = input("Warna kucing: ")
        kucing = Kucing(nama, umur, warna)
        daftar_hewan.append(kucing)

    elif jenis == "anjing":
        nama = input("Nama anjing: ")
        ras = input("Ras anjing: ")
        umur = input("Umur anjing: ")
        anjing = Anjing(nama, ras, umur)
        daftar_hewan.append(anjing)

    elif jenis == "burung":
        nama = input("Nama burung: ")
        jenis_burung = input("Jenis burung: ")
        warna = input("Warna bulu burung: ")
        burung = Burung(nama, jenis_burung, warna)
        daftar_hewan.append(burung)

    else:
        print("Jenis hewan tidak dikenali, lewati input ini.")

print("\n--- Informasi Semua Hewan ---")
for hewan in daftar_hewan:
    print(hewan.info())
    print(hewan.suara())
