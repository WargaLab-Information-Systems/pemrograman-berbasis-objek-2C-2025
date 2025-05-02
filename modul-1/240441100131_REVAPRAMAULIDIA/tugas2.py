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

mahasiswa_list = []

for i in range(3):
    print(f"Masukkan data mahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    while True:
        nim_input = input("NIM: ")
        if nim_input.isdigit(): 
            nim = int(nim_input)
            print("NIM valid:", nim)
            break  
        else:
            print("Input bukan angka,silakan masukkan NIM yang benar")
    jurusan = input("Jurusan/Prodi: ")
    alamat = input("Alamat: ")

    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    mahasiswa_list.append(mahasiswa)

    print("\nInformasi Mahasiswa:")
    for mhs in mahasiswa_list:
        mhs.tampilkan_info()
