class mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def informasi_mahasiswa(self):
        print(f"Nama    : ",self.nama)
        print(f"NIM     : ",self.nim)
        print(f"Prodi   : ",self.prodi)
        print(f"Alamat  : ",self.alamat)
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
jumlah = 3
daftar = []
for i in range(jumlah):
    print(f"\nMasukkan Data Mahasiswa ke-{i+1}")
    nama = input("Nama   : ")
    nim = input("NIM    : ")
    prodi = input("Prodi  : ")
    alamat = input("Alamat : ")

    mhs = mahasiswa(nama, nim, prodi, alamat)
    daftar.append(mhs)

print("\nData Mahasiswa")
for mhs in daftar:
    mhs.informasi_mahasiswa()