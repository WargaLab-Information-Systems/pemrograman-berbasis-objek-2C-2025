class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan/Prodi: {self.jurusan}")
        print(f"Alamat: {self.alamat}")
        print('-' * 40)

def input_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    jurusan = input("Masukkan jurusan/prodi mahasiswa: ")
    alamat = input("Masukkan alamat mahasiswa: ")

    return Mahasiswa(nama, nim, jurusan, alamat)

mahasiswa1 = input_mahasiswa()
mahasiswa2 = input_mahasiswa()
mahasiswa3 = input_mahasiswa()

mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()
mahasiswa3.tampilkan_info()
