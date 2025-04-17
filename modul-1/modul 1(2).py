class mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def info(self):
        print (f"{self.nama} NIM : {self.nim} JURUSAN : {self.jurusan} ALAMAT : {self.alamat}")

mahasiawa_list = []
for i in range(3):
    nama = input ("masukkan nama mahasiswa: ")
    nim = input ("masukkan nim: ")
    jurusan = input ("masukkan jurusan/prodi: ")
    alamat = input ("masukkan alamat: ")
    mhs = mahasiswa(nama, nim, jurusan, alamat)
    mahasiawa_list.append(mhs)
for mhs in mahasiawa_list:
    mhs.info()