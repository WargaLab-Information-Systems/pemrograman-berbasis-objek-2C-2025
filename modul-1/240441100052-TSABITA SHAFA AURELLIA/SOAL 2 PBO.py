class Mahasiswa :
    def __init__(self,nama, nim, jurusan,alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan 
        self. alamat = alamat
    def tampilkan_info (self):
        print(f"Nama: {self.nama}")
        print(f"Nim: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Alamat: {self.alamat}")
        print("-" * 30)

def main():
    daftar_mahasiswa = []

    for i in range(3):
        print (f"Masukan data mahasiswa ke -{i+1}:")
        nama = input("Nama:")
        nim = input("Nim:")
        jurusan  = input("Jurusan:")
        alamat = input("Alamat:")
        mhs = Mahasiswa (nama,nim,jurusan,alamat)
        daftar_mahasiswa.append(mhs)
        print("\n")

    print("=== Data Mahasiswa ===")
    for mhs in daftar_mahasiswa:
        mhs.tampilkan_info()
if __name__ == "__main__":
    main()
