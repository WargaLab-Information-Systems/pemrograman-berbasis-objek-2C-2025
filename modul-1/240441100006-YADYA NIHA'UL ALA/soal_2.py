class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def data(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Program Studi: {self.prodi}")
        print(f"Alamat: {self.alamat}")
        print(("-----------------------------"))
def main():
    daftar_mhs = []

    while True:
        print(f"\nMasukkan Data Mahasiswa:")
        nama = input("Nama: ")  
        nim = input("NIM: ")
        prodi = input("Program Studi: ")
        alamat = input("Alamat: ")

        mahasiswa = Mahasiswa(nama, nim, prodi, alamat)
        daftar_mhs.append(mahasiswa)

        lanjut = input("Apakah anda ingin menambah data lagi? (y/n): ").lower()
        if lanjut != 'y':
            break
    
    print(f"\n------ Data Mahasiswa ------")
    for mhs in daftar_mhs:
        mhs.data()

if __name__ == "__main__":
    main()