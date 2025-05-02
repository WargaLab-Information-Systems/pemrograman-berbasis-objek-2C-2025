class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not self.cek_sks(sks):
            raise ValueError(f"SKS {sks} tidak valid. Hanya boleh 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def cek_sks(sks):
        return sks in (2, 3)

class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError(f"NIM {nim} tidak valid. Harus dimulai dengan '23', terdiri dari 10 digit dan berupa angka.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah yang Diambil:")
        for mk in self.matkul_diambil:
            print(f"  - {mk.kode} | {mk.nama} | {mk.sks} SKS")

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"Jumlah Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10 and nim.isdigit()


class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama_kampus, alamat):
        if not Kampus.validasi_nama_kampus(nama_kampus):
            raise ValueError("Nama kampus tidak valid (tidak boleh mengandung angka).")
        self.nama_kampus = nama_kampus
        self.alamat = alamat
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
        Kampus.jumlah_mahasiswa += 1

    @classmethod
    def tampilkan_info_kampus(cls, nama_kampus):
        print(f"Nama Kampus: {nama_kampus}")
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)

try:
    kampus1 = Kampus("Universitas Trunojoyo Madura", "Jalan Setiabudhi No. 229, Bandung")


    mhs1 = Mahasiswa("Asep", "2301010010", "Teknik Informatika")
    mhs2 = Mahasiswa("Budi", "2301010020", "Sistem Informasi")
    mhs3 = Mahasiswa("Cici", "2301010030", "Teknik Komputer")
    mhs4 = Mahasiswa("Doni", "2301010040", "Teknik Elektro")
    mhs5 = Mahasiswa("Eka", "2301010050", "Teknik Mesin")
    mhs6 = Mahasiswa("Fani", "2301010060", "Teknik Sipil")

    list_mahasiswa = [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]

    for mhs in list_mahasiswa:
        kampus1.tambah_mahasiswa(mhs)

    mk1 = MataKuliah("MK001", "Pemrograman Dasar", 3)
    mk2 = MataKuliah("MK002", "Basis Data", 2)
    mk3 = MataKuliah("MK003", "Jaringan Komputer", 3)
    mk4 = MataKuliah("MK004", "Sistem Operasi", 2)
    mk5 = MataKuliah("MK005", "Rekayasa Perangkat Lunak", 3)
    mk6 = MataKuliah("MK006", "Analisis dan Perancangan Sistem", 2)
    mk7 = MataKuliah("MK007", "Kecerdasan Buatan", 3)
    mk8 = MataKuliah("MK008", "Keamanan Jaringan", 2)

    mhs1.matkul_diambil = [mk1, mk2, mk3, mk4]
    mhs2.matkul_diambil = [mk1, mk2, mk3, mk4, mk6]
    mhs3.matkul_diambil = [mk1, mk2, mk3, mk4, mk5]
    mhs4.matkul_diambil = [mk1, mk2, mk3, mk4, mk5, mk7]
    mhs5.matkul_diambil = [mk1, mk2, mk3, mk4, mk5, mk8]
    mhs6.matkul_diambil = [mk1, mk2, mk3, mk4, mk5, mk6]

except ValueError as e:
    print(f"Terjadi kesalahan saat membuat objek. Detail: {e}")

print("\n=== DATA MAHASISWA ===")
for mhs in list_mahasiswa:
    mhs.tampilkan_biodata()
    print()

print("=== DATA KAMPUS ===")
Kampus.tampilkan_info_kampus(kampus1.nama_kampus)
print(f"Apakah nama kampus valid? {'Ya' if Kampus.validasi_nama_kampus(kampus1.nama_kampus) else 'Tidak'}\n")

Mahasiswa.tampilkan_jumlah_mahasiswa()
