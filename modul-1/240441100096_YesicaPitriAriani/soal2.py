class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"prodi: {self.jurusan}")
        print(f"alamat: {self.alamat}")

def main():
    daftar_mahasiswa = []
    
    for i in range(3):
        print(f"masukkan data mahasiswa ke-{i + 1}:")
        nama = input("masukkan nama mahasiswa: ")
        nim = input("masukkan NIM mahasiswa: ")
        jurusan = input("masukkan prodi mahasiswa: ")
        alamat = input("masukkan alamat mahasiswa: ")
        
        mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
        daftar_mahasiswa.append(mahasiswa)
        print()

    print("\ndata semua mahasiswa:")
    for mahasiswa in daftar_mahasiswa:
        print(f"\nMahasiswa ke-{i}")
        mahasiswa.tampilkan_info()

main()


