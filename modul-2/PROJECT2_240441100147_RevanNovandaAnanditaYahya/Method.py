class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul.append(matkul)

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        if self.matkul:
            print("Mata Kuliah yang diambil:")
            for matkul in self.matkul:
                print(f"- {matkul.nama}")

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"Jumlah mahasiswa yang sudah dibuat: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        if int(nim[:2]) == 23 and len(nim) == 10:
            return nim
        else:
            return

class Matakuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]

class Kampus:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    def tampilkan_info_kampus(self):
        print(f"Nama Kampus: {self.nama}")
        print(f"Alamat Kampus: {self.alamat}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)

def data_mahasiswa():
    while True:
        nama = input("Masukkan nama mahasiswa: ")

        while True:
                nim = input("Masukkan NIM mahasiswa (diawali '23' dan berisi 10 digit): ")
                if Mahasiswa.validasi_nim(nim):
                    break
                else:
                    print("Masukkan NIM dengan awalan '23' dan harus berisi 10 digit")

        prodi = input("Masukkan prodi mahasiswa: ")
        return Mahasiswa(nama, nim, prodi)

def data_kampus():
    while True:
        while True:
            nama = input("Masukkan nama kampus (tanpa angka): ")
            if Kampus.validasi_nama_kampus(nama):
                break
            else:
                print("Masukkan nama kampus tanpa angka.")
                
        alamat = input("Masukkan alamat kampus: ")        
        return Kampus(nama, alamat)

matkul_list = [
    Matakuliah("SI01", "PBO", 3),
    Matakuliah("SI02", "PBD", 3),
    Matakuliah("SI03", "B.Inggris", 3),
    Matakuliah("SI04", "PBW", 3),
    Matakuliah("SI05", "Ebussines", 2),
    Matakuliah("SI06", "Alpro", 3),
    Matakuliah("SI07", "APB", 2),
    Matakuliah("SI08", "DMJ", 3)
]

mahasiswa_list = []
while True:
    mahasiswa = data_mahasiswa()
    mahasiswa_list.append(mahasiswa)
    
    if len(mahasiswa_list) < 6:
        print(f"Data minimal belum tercapai")
    else:
        tambah = input("Data minimal sudah tercapai, tambah data? (ya/tidak): ")
        if tambah != "ya":
            break

for mhs in mahasiswa_list:
    print(f"\n{mhs.nama}, pilih mata kuliah:")
    while len(mhs.matkul) < 4:
        print(f"Pilihan Mata Kuliah ({len(mhs.matkul)}):")
        for i, matkul in enumerate(matkul_list, 1):
            print(f"{i}. {matkul.nama} ({matkul.sks} SKS)")
        
        try:
            pilihan = int(input("Pilih mata kuliah: "))
            if 1 <= pilihan <= len(matkul_list):
                mhs.tambah_matkul(matkul_list[pilihan - 1])  
            else:
                print("Pilihan tidak valid")
        except ValueError:
            print("Masukkan input yang sesuai")

kampus_list = []
while True:
    kampus = data_kampus()
    kampus_list.append(kampus)

    if len(kampus_list) < 1:
        print("Data minimal 1")
    else:
        tambah = input("Data minimal sudah tercapai, tambah data? (ya/tidak): ")
        if tambah != "ya":
            break


print("\nData Mahasiswa dan Mata Kuliah yang diambil")
for mhs in mahasiswa_list:
    mhs.tampilkan_biodata()
    print()

print("\nData Mata Kuliah")
for matkul in matkul_list:
    print(f"Kode: {matkul.kode}, Nama: {matkul.nama}, SKS: {matkul.sks}")
print()

print("\nData Kampus")
for kampus in kampus_list:
    kampus.tampilkan_info_kampus()
    print()

print("Validasi Data Kampus")
for kampus in kampus_list:    
    kampus.tampilkan_info_kampus()
    print("Validasi nama kampus:", Kampus.validasi_nama_kampus(kampus.nama))