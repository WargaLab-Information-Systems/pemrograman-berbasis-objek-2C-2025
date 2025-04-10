#soal no 1
# class manusia():
#     def __init__(self, nama, umur, alamat,):
#         self.nama = nama
#         self.umur = umur
#         self.alamat = alamat
#     def berjalan(self):
#         return f"{self.nama} sedang berjalan"
#     def berlari(self):
#         return f"{self.nama} sedang berlari"
    
# manusia1 = manusia("rahmad", 25, "Jl. Kebon Jeruk")
# manusia2 = manusia("ahmad", 26, "Jl. Kebon apel")
# manusia3 = manusia("rafi", 27, "Jl. Kebon anggur")
# manusia4 = manusia("mahmud", 28, "Jl. Kebon salak")
# manusia5 = manusia("rafa", 29, "Jl. Kebon durian")

# print(manusia1.berjalan())
# print(manusia1.berlari())
# print("nama", manusia1.nama, "umur", manusia1.umur, "alamat", manusia1.alamat)


# soal no 2
# class Mahasiswa:
#     def __init__(self, nama, nim, prodi):
#         self.nama = nama
#         self.nim = nim
#         self.prodi = prodi

#     def tampilkan(self):
#         return f"nama: {self.nama}, nim: {self.nim}, prodi: {self.prodi}"


# inputmahasiswa = []
# for i in range(3):
#     nama = input ("masukkan nama: ") 
#     nim = input ("masukkan nim: ")
#     prodi = input ("masukkan prodi: ")
#     mahasiswa = Mahasiswa(nama, nim, prodi)
#     inputmahasiswa.append(mahasiswa)

# print("Saat ini:")
# for Mahasiswa in inputmahasiswa:
#     Mahasiswa.tampilkan()

# # soal no 3
# class Anjing:
#     def __init__(self, nama, jenis, warna):
#         self.nama = nama
#         self.jenis = jenis
#         self.warna = warna

#     def berlari(self):
#         return f"{self.nama}, dengan jenis {self.jenis} suka berlari."

#     def tampilkan(self):
#         return f"Nama: {self.nama}, Jenis: {self.jenis}, Warna: {self.warna}\n{self.berlari()}"


# class Kucing:
#     def __init__(self, nama, jenis, suara):
#         self.nama = nama
#         self.jenis = jenis
#         self.suara = suara

#     def suara_hewan(self):
#         return f"Jenis ini {self.nama}, bersuara seperti {self.suara}."

#     def tampilkan(self):
#         return f"Nama: {self.nama}, Jenis: {self.jenis}\n{self.suara_hewan()}"

# class Burung:
#     def __init__(self, nama, jenis, suara):
#         self.nama = nama
#         self.jenis = jenis
#         self.suara = suara

#     def terbang(self):
#         return f"Jenis burung {self.jenis} sedang terbang."

#     def tampilkan(self):
#         return f"Nama: {self.nama}, Jenis: {self.jenis}, Suara: {self.suara}\n{self.terbang()}"

# datahewan = []

# print("anjing")
# for _ in range(3):
#     nama = input("Masukkan nama: ")
#     jenis = input("Masukkan jenis: ")
#     warna = input("Masukkan warna: ")
#     anjing = Anjing(nama, jenis, warna)
#     datahewan.append(anjing)


# print("kucing")
# for _ in range(3):
#     nama = input("Masukkan nama: ")
#     jenis = input("Masukkan jenis: ")
#     suara = input("Masukkan suara: ")
#     kucing = Kucing(nama, jenis, suara)
#     datahewan.append(kucing)

# print("burung")
# for _ in range(3):
#     nama = input("Masukkan nama: ")
#     jenis = input("Masukkan jenis: ")
#     suara = input("Masukkan suara: ")
#     burung = Burung(nama, jenis, suara)
#     datahewan.append(burung)
# print()

# for hewan in datahewan:
#     print(hewan.tampilkan())




        
      
