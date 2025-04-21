class MataKuliah:
    def __init__(self, kode, nama, sks): 
        if self.validasi_sks(sks):   
            self.kode = kode
            self.nama = nama
            self.sks = sks
            self.valid = True 
        else:
            print(f" SKS '{sks}' untuk mata kuliah '{nama}' tidak valid (hanya boleh 2 atau 3). Data tidak disimpan.") 
            self.valid = False 

    @staticmethod 
    def validasi_sks(sks):
        return sks in [2, 3] 
    
class Mahasiswa:
    total = 0   
    def __init__(self, nama, nim, prodi):
        if self.validasi_nim(nim): 
            self.nama = nama
            self.nim = nim
            self.prodi = prodi   
            self.mata_kuliah = []  
            Mahasiswa.total += 1
            self.valid = True 
        else:
            print(f"\n salah NIM '{nim}' untuk mahasiswa '{nama}' tidak valid!")
            print("Alasan: NIM harus terdiri dari 10 digit dan diawali dengan '24'.")
            print(f"Data mahasiswa '{nama}' tidak disimpan.\n")
            self.valid = False

    def tambah_matkul(self, matkul):
        if matkul.valid:
            self.mata_kuliah.append(matkul) 
            
    def tampilkan(self):
        print(f"\n Mahasiswa: {self.nama} | NIM: {self.nim} | Prodi: {self.prodi}") 
        print("Mata kuliah yang diambil:")
        for mk in self.mata_kuliah:
                print(f"  - {mk.nama} ({mk.sks} SKS)")
        else:
            print("Tidak ada mata kuliah yang diambil.")

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("24") and len(nim) == 10 and nim.isdigit()

    @classmethod
    def total_mahasiswa(cls):
        return cls.total 

class Kampus:
    def __init__(self, nama, alamat): 
        self.nama = nama
        self.alamat = alamat 
        self.valid = self.validasi_nama_kampus(nama)
        if not self.valid:
            print(f"\n Salah Nama kampus '{nama}' tidak valid!")
            print("Alasan: Nama kampus tidak boleh mengandung angka.\n")

    @staticmethod
    def validasi_nama_kampus(nama):
        return all (not char.isdigit() for char in nama)

    @classmethod
    def info(cls, nama):
        print(f"\nKampus: {nama}")
        print(f"Total Mahasiswa: {Mahasiswa.total_mahasiswa()}")

daftar_matkul = [
    MataKuliah("MK001", "PBO", 3),
    MataKuliah("MK002", "Struktur Data", 3),
    MataKuliah("MK003", "Algoritma", 2),
    MataKuliah("MK004", "Basis Data", 3),
    MataKuliah("MK005", "Kalkulus", 3),
    MataKuliah("MK006", "Statistik", 2),
    MataKuliah("MK007", "Sistem Operasi", 3),
    MataKuliah("MK008", "Jaringan Komputer", 2),
]

daftar_mahasiswa = []
data_mhs = [
    ("Andi", "2h412345678", "Teknik Informatika"),
    ("Budi", "2412345679", "Sistem Informasi"),
    ("Citra", "2412345680", "Teknik Komputer"),
    ("Dina", "2412345681", "Teknik Informatika"),
    ("Eka", "2412345682", "Sistem Informasi"),
    ("Fahri", "2412345683", "Teknik Komputer"),
]

for nama, nim, prodi in data_mhs:
    mhs = Mahasiswa(nama, nim, prodi)
    if mhs.valid:
        for mk in daftar_matkul[:4]:
            mhs.tambah_matkul(mk)
        daftar_mahasiswa.append(mhs)

kampus = Kampus("Universitas Trunojoyo Madura66", "Jl.Raya Telang No.345")

print("\n---- DATA MAHASISWA -----")
for mhs in daftar_mahasiswa:
    mhs.tampilkan()

print("\n----- DATA KAMPUS -----")
kampus.info(kampus.nama)
print(f"Validasi Nama Kampus: {'Valid' if kampus.valid else 'Tidak Valid'}")