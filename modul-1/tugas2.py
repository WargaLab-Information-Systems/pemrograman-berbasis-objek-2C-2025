class mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
    
    def tampilkan_info(self):
        return f"Nama: {self.nama}, Nim: {self.nim}, jurusan: {self.jurusan}, Alamat: {self.alamat}"
    
def validasi_input(datamhs):
        while True:
             data = input(datamhs).strip()
             if data:
                  return data
             print("input tidak boleh kosong!")
            
def input_data_mahasiswa():
    nama = validasi_input("masukkan nama mahasiswa: ")
    nim = validasi_input("masukkan NIM mahasiswa: ")
    jurusan = validasi_input("masukkan jurusan/prodi mahasiswa: ")
    alamat = validasi_input("masukkan alamat mahasiswa: ")
    return mahasiswa(nama, nim, jurusan, alamat)

def tambah_data():
    while True:
        jawaban = input("apakah ingin menambahkan data mahasiswa? (ya/tidak):  ").strip().lower()
        if jawaban in ["ya", "tidak"]:
             return jawaban == "ya"
        print("pilihan tidak valid!, silahkan masukkaan 'ya' atau 'tidak'")

mahasiswa4 = []
jumlah_data_awal = 3

for i in range(jumlah_data_awal):
    print(f"\nMasukkan data mahasiswa ke-{i+1}:")
    mhs = input_data_mahasiswa()
    mahasiswa4.append(mhs)

while True:
    if not tambah_data():
        break
    print(f"\nMasukkan data mahasiswa ke-{len(mahasiswa4) + 1}:")
    mhs = input_data_mahasiswa()
    mahasiswa4.append(mhs)
    print()

print("\nInformasi mahasiswa:")
for idx, mhs in enumerate(mahasiswa4, start=1):
    print(f"Mahasiswa {idx}: {mhs.tampilkan_info()}")
