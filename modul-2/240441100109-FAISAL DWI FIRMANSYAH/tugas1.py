class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if Mahasiswa.cek_nim_valid(nim):
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.matkul_diambil = []
            Mahasiswa.jumlah_mahasiswa += 1
        else:
            print(f"NIM '{nim}' tidak valid (harus mulai dengan '23' dan 10 digit). Objek tidak dibuat.")
            self.nama = None
            self.nim = None
            self.prodi = None
            self.matkul_diambil = []

    def tambah_matkul(self, matkul):
        if matkul and matkul.nama:
            self.matkul_diambil.append(matkul)

    def tampilkan_biodata(self):
        if self.nama:
            print(f"Nama: {self.nama}, NIM: {self.nim}, Prodi: {self.prodi}")
            print("Mata Kuliah yang diambil:")
            for matkul in self.matkul_diambil:
                print(f"- {matkul.nama} ({matkul.sks} SKS)")

    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def cek_nim_valid(nim):
        return nim.startswith("23") and len(nim) == 10

class MataKuliah:
    def __init__(self, kode, nama, sks):
        if MataKuliah.cek_sks_valid(sks):
            self.kode = kode
            self.nama = nama
            self.sks = sks
        else:
            print(f"SKS untuk mata kuliah '{nama}' tidak valid (harus 2 atau 3). Objek tidak dibuat.")
            self.kode = None
            self.nama = None
            self.sks = None

    @staticmethod
    def cek_sks_valid(sks):
        return sks in (2, 3)

class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        if Kampus.cek_nama_kampus_valid(nama):
            self.nama = nama
            self.alamat = alamat
        else:
            print(f"Nama kampus '{nama}' tidak valid (tidak boleh mengandung angka). Objek tidak dibuat.")
            self.nama = None
            self.alamat = None

    @classmethod
    def tampilkan_info_kampus(cls, kampus):
        if kampus.nama:
            print(f"Nama Kampus: {kampus.nama}, Alamat: {kampus.alamat}")
            print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def cek_nama_kampus_valid(nama):
        angka = set("0123456789")
        for char in nama:
            if char in angka:
                return False
        return True


matkuls = [
    MataKuliah("SI001", "Algoritma Pemrograman", 3),
    MataKuliah("SI002", "Matematika Diskrit", 3),
    MataKuliah("SI003", "Statistika", 2),
    MataKuliah("SI004", "Logika Engineering", 2),
    MataKuliah("SI005", "Desain Manajemen Jaringan", 3),
    MataKuliah("SI006", "PBO", 2),
    MataKuliah("SI007", "PBW", 3),
    MataKuliah("SI008", "Sistem Operasi", 3),
]

mahasiswas = [
    Mahasiswa("Yoga", "2312345678", "Informatika"),
    Mahasiswa("Zaki", "2312345679", "Sistem Informasi"),
    Mahasiswa("Ambaki", "2312345680", "Teknik Komputer"),
    Mahasiswa("Rusdit", "2312345681", "Teknik Elektro"),
    Mahasiswa("Eka", "2312345682", "Informatika"),
    Mahasiswa("Wahyu", "2312345683", "Sistem Informasi"),
]

for i, mhs in enumerate(mahasiswas):
    if mhs.nama:
        for j in range(4):
            mhs.tambah_matkul(matkuls[(i + j) % len(matkuls)])
        Kampus.jumlah_mahasiswa += 1

kampus = Kampus("Universitas Trunojoyo Madura", "Jl. Raya Telang No.345")

print("=== Data Mahasiswa ===")
for mhs in mahasiswas:
    mhs.tampilkan_biodata() 
    print()

print("=== Info Kampus ===")
Kampus.tampilkan_info_kampus(kampus)
print("Nama kampus valid:", Kampus.cek_nama_kampus_valid(kampus.nama if kampus.nama else ""))