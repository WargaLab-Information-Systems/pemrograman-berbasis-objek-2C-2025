class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_data(self):
        print("\nData Mahasiswa:")
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Alamat  : {self.alamat}")


daftar_mahasiswa = []

jumlah_mahasiswa = 3
for i in range(jumlah_mahasiswa):
    print(f"\nMasukkan data mahasiswa ke-{i+1}")
    nama = input("Nama    : ")
    nim = input("NIM     : ")
    jurusan = input("Jurusan/Prodi : ")
    alamat = input("Alamat  : ")

    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    daftar_mahasiswa.append(mahasiswa)


print("\n========== Daftar Mahasiswa ==========")
for mhs in daftar_mahasiswa:
    mhs.tampilkan_data()