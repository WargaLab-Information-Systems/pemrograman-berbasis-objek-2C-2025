class MataKuliah:
    def __init__(self, nama, sks):
        if not MataKuliah.validasi_sks(sks):
            raise ValueError(f"SKS untuk mata kuliah {nama} tidak valid: {sks}")
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]

    def __str__(self):
        return f"{self.nama} - ({self.sks} SKS)"


class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError(f"NIM tidak valid: {nim}")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.mata_kuliah = []
        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.mata_kuliah.append(matkul)

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah:")
        for mk in self.mata_kuliah:
            print(f"{mk}")
        print()

    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return isinstance(nim, str) and nim.startswith("23") and len(nim) == 10


class Kampus:
    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            raise ValueError(f"Nama kampus tidak valid: {nama}")
        self.nama = nama
        self.alamat = alamat

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)

    @classmethod
    def tampilkan_info_kampus(cls, kampus):
        print(f"Nama Kampus: {kampus.nama}")
        print(f"Alamat: {kampus.alamat}")
        print(f"Total Mahasiswa: {Mahasiswa.jumlah_mahasiswa()}")
        print(f"Nama kampus valid: {Kampus.validasi_nama_kampus(kampus.nama)}")
        print()


#  Buat 8 objek MataKuliah dan simpan ke dalam daftar
mk1 = MataKuliah("Pemrograman", 3)
mk2 = MataKuliah("Bahasa Inggris", 2)
mk3 = MataKuliah("Algoritma", 3)
mk4 = MataKuliah("Basis Data", 3)
mk5 = MataKuliah("Jaringan", 2)
mk6 = MataKuliah("AI Dasar", 3)
mk7 = MataKuliah("Statistika", 2)
mk8 = MataKuliah("Pancasila", 3)

daftar_matkul = [mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8]

m1 = Mahasiswa("Rudy", "2312345678", "Informatika")
m2 = Mahasiswa("Opet", "2312345679", "Sistem Informasi")
m3 = Mahasiswa("Sinta", "2312345680", "Teknik Komputer")
m4 = Mahasiswa("Ledy", "2312345681", "Informatika")
m5 = Mahasiswa("Nia", "2312345682", "Sistem Informasi")
m6 = Mahasiswa("Tio", "2312345683", "Teknik Komputer")

for i, mhs in enumerate([m1, m2, m3, m4, m5, m6]):
    mhs.tambah_matkul(daftar_matkul[i % 8])
    mhs.tambah_matkul(daftar_matkul[(i + 1) % 8])
    mhs.tambah_matkul(daftar_matkul[(i + 2) % 8])
    mhs.tambah_matkul(daftar_matkul[(i + 3) % 8])

kampus1 = Kampus("Universitas Trunojoyo Madura", "Jl. Telang No. 6, Madura")

print("=== DATA MAHASISWA ===\n")
for mhs in [m1, m2, m3, m4, m5, m6]:
    mhs.tampilkan_info()

print("=== DATA KAMPUS ===\n")
Kampus.tampilkan_info_kampus(kampus1)
