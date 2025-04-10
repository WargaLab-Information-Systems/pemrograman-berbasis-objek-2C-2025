class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def info_mahasiswa(self):
        return f"Nama: {self.nama}, Nim: {self.nim}, Prodi: {self.prodi}, Alamat: {self.alamat}"
    
list_mahasiswa = []

for i in range(3):
    print(f"\nMasukkan data mahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nim = input("Nim: ")
    prodi = input("Jurusan/Prodi: ")
    alamat = input("Alamat: ")

    mahasiswa = Mahasiswa(nama, nim, prodi, alamat)
    list_mahasiswa.append(mahasiswa)

print("\nData Mahasiswa:")
for nomor, mhs in enumerate(list_mahasiswa, start=1):
    print(f"{nomor}. {mhs.info_mahasiswa()}")