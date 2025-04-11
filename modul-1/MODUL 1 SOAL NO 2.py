class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama=nama
        self.nim=nim
        self.prodi=prodi

    def Tampilkan_data (self):
        print("========DATA MAHASISWA========")
        print(f"Nama :{self.nama}")
        print(f"nim  :{self.nim}")
        print(f"prodi:{self.prodi}")
        print("=" * 30)

mhs1 = Mahasiswa (input("Masukan nama1 :"), input("Masukan NIM mhs1: "), input("Masukan prodi mhs1: "))
mhs2 = Mahasiswa (input("Masukan nama2 :"), input("Masukan NIM mhs2: "), input("Masukan prodi mhs2: "))
mhs3 = Mahasiswa (input("Masukan nama3 :"), input("Masukan NIM mhs3: "), input("Masukan prodi mhs3: "))

mhs1.Tampilkan_data()
mhs2.Tampilkan_data()
mhs3.Tampilkan_data()