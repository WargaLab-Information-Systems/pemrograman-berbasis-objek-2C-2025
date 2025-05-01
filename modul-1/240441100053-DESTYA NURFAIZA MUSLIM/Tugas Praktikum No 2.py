class mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"Nama : {self.nama}")
        print(f"NIM : {self.nim}")
        print(f"Prodi : {self.prodi}")
        print(f"Alamat : {self.alamat}")
        
mahasiswa_list = []
jumlah = int(input("Masukkan jumlah mahasiswa (minimal 3) : "))
while jumlah < 3:
    print("Jumlah data minimal 3. Ulangi lagi.")
    jumlah = int(input("Masukkan jumlah mahasiswa (minimal 3) : "))

for i in range (jumlah):
    print()
    nama = input(f"Masukkan Nama Mahasiswa ke-{i+1} : ")
    nim = input(f"Masukkan NIM Mahasiswa ke-{i+1} : ")
    prodi = input(f"Masukkan Prodi Mahasiswa ke-{i+1} : ")
    alamat = input(f"Masukkan Alamat Mahasiswa ke-{i+1} : ")
    mahasiswa_list.append(mahasiswa(nama,nim,prodi,alamat))

print()
for i in range(len(mahasiswa_list)):
    print(f"\nData Mahasiswa ke-{i+1} : ")
    mahasiswa_list[i].tampilkan_info()

