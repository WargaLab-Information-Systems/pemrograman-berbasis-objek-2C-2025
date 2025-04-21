class Mahasiswa:
    total_mahasiswa = 0
    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.cek_nim(nim):
            raise ValueError(f"NIM {nim} tidak valid.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_info(self):
        print(f"Nama: {self.nama}\nNIM: {self.nim}\nProdi: {self.prodi}")
        print("Daftar Mata Kuliah:")
        for mk in self.matkul_diambil:
            print(f"- {mk.kode} | {mk.nama} | {mk.sks} SKS")
        print()

    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def cek_nim(nim):
        return nim.startswith("23") and len(nim) == 10 and nim.isdigit()

class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.cek_sks_valid(sks):
            raise ValueError(f"SKS untuk {nama} tidak valid. Hanya boleh 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def cek_sks_valid(sks):
        return sks in [2, 3]

class Kampus:
    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            raise ValueError("Nama kampus tidak valid, tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampilkan_info(cls, kampus_obj):
        print(f"Nama Kampus: {kampus_obj.nama}")
        print(f"Alamat: {kampus_obj.alamat}")
        print(f"Total Mahasiswa: {Mahasiswa.jumlah_mahasiswa()}\n")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)


data_matkul = [
    ("MK101", "Algoritma Pemrograman", 3),
    ("MK102", "Struktur Data", 3),
    ("MK103", "Matematika Diskrit", 2),
    ("MK184", "Basis Data", 3),
    ("MK105", "Jaringan Komputer", 3),
    ("MK206", "Sistem Operasi", 3),
    ("MK107", "Kalkulus", 2),
    ("MK908", "Kecerdasan Buatan", 3)
]

matkul_list = [MataKuliah(kode, nama, sks) for kode, nama, sks in data_matkul]

m1 = Mahasiswa("Yesica", "2312345678", "Sistem Informasi")
m2 = Mahasiswa("Liaa", "2312345679", "Teknik Informatika")
m3 = Mahasiswa("Putra", "2312345680", "Teknik Mesin")
m4 = Mahasiswa("Dina", "2312356815", "Manajemen")
m5 = Mahasiswa("Disha", "2312345682", "Hukum")
m6 = Mahasiswa("Fani", "2312345683", "Sistem Informasi")

mahasiswa_list = [m1, m2, m3, m4, m5, m6]

m1.tambah_matkul(matkul_list[0])
m1.tambah_matkul(matkul_list[1])
m1.tambah_matkul(matkul_list[6])
m1.tambah_matkul(matkul_list[3])

m2.tambah_matkul(matkul_list[1])
m2.tambah_matkul(matkul_list[2])
m2.tambah_matkul(matkul_list[3])
m2.tambah_matkul(matkul_list[4])

m3.tambah_matkul(matkul_list[0])
m3.tambah_matkul(matkul_list[4])
m3.tambah_matkul(matkul_list[2])
m3.tambah_matkul(matkul_list[6])

m4.tambah_matkul(matkul_list[2])
m4.tambah_matkul(matkul_list[5])
m4.tambah_matkul(matkul_list[6])
m4.tambah_matkul(matkul_list[7])


m5.tambah_matkul(matkul_list[1])
m5.tambah_matkul(matkul_list[2])
m5.tambah_matkul(matkul_list[3])
m5.tambah_matkul(matkul_list[5])

m6.tambah_matkul(matkul_list[0])
m6.tambah_matkul(matkul_list[1])
m6.tambah_matkul(matkul_list[5])
m6.tambah_matkul(matkul_list[7])

kampus1 = Kampus("Universitas Trunojoyo Madura", "Jalan Raya Telang N0.1")

print("=== INFO MAHASISWA DAN MATAKULIAH ===\n")
for mhs in mahasiswa_list:
    mhs.tampilkan_info()

print("=== INFO KAMPUS ===\n")
Kampus.tampilkan_info(kampus1)
print(f"Nama Kampus Valid? {'Ya' if Kampus.validasi_nama_kampus(kampus1.nama) else 'Tidak'}")

