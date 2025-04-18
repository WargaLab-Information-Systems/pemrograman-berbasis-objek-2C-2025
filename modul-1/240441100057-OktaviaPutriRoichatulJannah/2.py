class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def display(self):
        print()
        print(f"Nama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"Alamat   : {self.alamat}")

list_mahasiswa = []
for i in range (3):
    print(f"------ Masukkan data mahasiswa ke-{i+1} ------")
    nama = input("Masukkan Nama mahasiswa: ")
    while not nama:
        print("Nama tidak boleh kosong!")
        nama = input("Masukkan Nama mahasiswa: ")

    nim = input("Masukkan NIM mahasiswa: ")
    while not nim:
        print("NIM tidak boleh kosong!")
        nim = input("Masukkan NIM mahasiswa: ")

    jurusan = input("Masukkan Jurusan mahasiswa: ")
    while not jurusan:
        print("Jurusan tidak boleh kosong!")
        jurusan = input("Masukkan Jurusan mahasiswa: ")

    alamat = input("Masukkan Alamat mahasiswa: ")
    while not alamat:
        print("Alamat tidak boleh kosong!")
        alamat = input("Masukkan Alamat mahasiswa: ")
    print()

    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    list_mahasiswa.append(mahasiswa)

while True:
    tambah_data = input("Apakah anda ingin menambahkkan data mahasiswa lagi(y/n): ")
    if tambah_data == "y":
        nama = input("Masukkan Nama mahasiswa: ")
        while not nama:
            print("Nama tidak boleh kosong!")
            nama = input("Masukkan Nama mahasiswa: ")

        nim = input("Masukkan NIM mahasiswa: ")
        while not nim:
            print("NIM tidak boleh kosong!")
            nim = input("Masukkan NIM mahasiswa: ")

        jurusan = input("Masukkan Jurusan mahasiswa: ")
        while not jurusan:
            print("Jurusan tidak boleh kosong!")
            jurusan = input("Masukkan Jurusan mahasiswa: ")

        alamat = input("Masukkan Alamat mahasiswa: ")
        while not alamat:
            print("Alamat tidak boleh kosong!")
            alamat = input("Masukkan Alamat mahasiswa: ")

        mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
        list_mahasiswa.append(mahasiswa)
    
    elif tambah_data == "n":
        break

    else:
        print("Input tidak valid!! Silahkana masukkan y atau n")

line = "=" * 38
print()
print(line)
print("***** DATA MAHASISWA *****")
for mhs in list_mahasiswa:
    mhs.display()
print(line)