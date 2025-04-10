class mahasiswa:
    def __init__(self):
        self.nama = ""
        self.nim = ""
        self.prodi = ""
        self.alamat = ""

    def input_mahasiswa(self):
        print("-----INPUT DATA MAHASISWA-----")
        self.nama = input("Masukkan Nama Mahasiswa         : ")
        self.nim = input("Masukkan NIM Mahasiswa          : ")
        self.prodi = input("Masukkan Prodi/Jurusan Mahasiswa: ")
        self.alamat = input("Masukkan Alamat Mahasiswa       : ")
        print()
    def tampilkan_mahasiswa(self):
        print("\n---DATA MAHASISWA---")
        print(f"Nama Mahasiswa  : {self.nama}")
        print(f"NIM Mahasiswa   : {self.nim}")
        print(f"Prodi Mahasiswa : {self.prodi}")
        print(f"Alamat Mahasiswa: {self.alamat}")
mhs1 = mahasiswa()
mhs2 = mahasiswa()
mhs3 = mahasiswa()
mhs1.input_mahasiswa()
mhs2.input_mahasiswa()
mhs3.input_mahasiswa()
mhs1.tampilkan_mahasiswa()
mhs2.tampilkan_mahasiswa()
mhs3.tampilkan_mahasiswa()
