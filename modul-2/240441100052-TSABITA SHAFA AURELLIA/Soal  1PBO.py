class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not self.validasi_nim(nim):
            raise ValueError("NIM tidak valid. Harus dimulai dengan '23' dan 10 digit.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.mata_kuliah_diambil = []
        Mahasiswa.jumlah_mahasiswa += 1 

    def tambah_mata_kuliah(self, mata_kuliah):
        self.mata_kuliah_diambil.append(mata_kuliah)

    def tampilkan_biodata(self):
        print(f"\nNama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Prodi    : {self.prodi}")
        print("Mata Kuliah yang Diambil:")
        for mk in self.mata_kuliah_diambil:
            print(f"- {mk.kode} : {mk.nama} ({mk.sks} SKS)")

    @classmethod
    def get_jumlah_mahasiswa(cls):  
        return cls.jumlah_mahasiswa

    @staticmethod
    def validasi_nim(nim):
         return len(nim) == 10 and nim[:2]=="23"


class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not self.validasi_sks(sks):
            raise ValueError(f"SKS tidak valid untuk matkul {nama}. Harus 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]


class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama_kampus, alamat_kampus):
        if not self.validasi_nama_kampus(nama_kampus):
            raise ValueError(f"Nama kampus tidak valid: {nama_kampus}")
        self.nama_kampus = nama_kampus
        self.alamat_kampus = alamat_kampus

    @classmethod
    def tampilkan_nama_kampus(cls, nama_kampus):
        print(f"\nNama Kampus      : {nama_kampus}")
        print(f"Jumlah Mahasiswa : {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama_kampus):
        return not any(char.isdigit() for char in nama_kampus)


mahasiswa_list = [
    Mahasiswa("Andi", "2312345678", "Informatika"),
    Mahasiswa("Budi", "2312345679", "Sistem Informasi"),
    Mahasiswa("Citra", "2312345680", "Teknik Komputer"),
    Mahasiswa("Dina", "2312345681", "Informatika"),
    Mahasiswa("Eka", "2312345682", "Sains Data"),
    Mahasiswa("Fajar", "2312345683", "Informatika"),
]

daftar_matkul = [
    MataKuliah("MK001", "Pemrograman Dasar", 3),
    MataKuliah("MK002", "Matematika Diskrit", 3),
    MataKuliah("MK003", "Struktur Data", 3),
    MataKuliah("MK004", "Algoritma", 3),
    MataKuliah("MK005", "Basis Data", 2),
    MataKuliah("MK006", "Sistem Operasi", 3),
    MataKuliah("MK007", "Jaringan Komputer", 2),
    MataKuliah("MK008", "Kecerdasan Buatan", 3),
]

kampus1 = Kampus("Universitas Trunojoyo", "Jl. Telang")

for i in range(len(mahasiswa_list)):
    mhs = mahasiswa_list[i]
    for j in range(4):
        mhs.tambah_mata_kuliah(daftar_matkul[(i + j) % len(daftar_matkul)])


Kampus.jumlah_mahasiswa = Mahasiswa.get_jumlah_mahasiswa()


print("\n--- DATA MAHASISWA ---")
for mhs in mahasiswa_list:
    mhs.tampilkan_biodata()

print("\n--- DATA KAMPUS ---")
Kampus.tampilkan_nama_kampus(kampus1.nama_kampus)
print(f"Alamat Kampus     : {kampus1.alamat_kampus}")
print(f"Nama Kampus Valid : {Kampus.validasi_nama_kampus(kampus1.nama_kampus)}")
