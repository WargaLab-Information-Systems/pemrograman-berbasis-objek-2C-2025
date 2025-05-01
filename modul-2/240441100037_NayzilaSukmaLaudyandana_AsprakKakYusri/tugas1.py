class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.cek_sks_valid(sks):
            raise ValueError(f"SKS untuk {nama} tidak valid. Harus 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def cek_sks_valid(sks):
        return sks in (2, 3)


class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError(f"NIM {nim} tidak valid.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.mata_kuliah = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul): #menambahkan matkul ke dalam daftar mata_kuliah yang dimiliki oleh objek mahasiswa.
        self.mata_kuliah.append(matkul)

    def tampilkan_info(self):
        print(f"\nNama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah yang diambil:")
        for mk in self.mata_kuliah:
            print(f"  - {mk.nama} ({mk.kode}, {mk.sks} SKS)")

    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10


class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            raise ValueError(f"Nama kampus '{nama}' tidak valid. Tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat
        Kampus.jumlah_mahasiswa = Mahasiswa.jumlah_mahasiswa

    @classmethod
    def tampilkan_info_kampus(cls, nama, alamat):
        print(f"\nNama Kampus: {nama}")
        print(f"Alamat Kampus: {alamat}")
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)


# DATA MATA KULIAH
mk1 = MataKuliah("IF101", "Pemrograman Dasar", 3)
mk2 = MataKuliah("IF102", "Struktur Data", 3)
mk3 = MataKuliah("IF103", "Basis Data", 2)
mk4 = MataKuliah("IF104", "PBO", 3)
mk5 = MataKuliah("IF105", "Web Dasar", 2)
mk6 = MataKuliah("IF106", "Sistem Operasi", 3)
mk7 = MataKuliah("IF107", "Matematika Diskrit", 2)
mk8 = MataKuliah("IF108", "Jaringan Komputer", 3)

daftar_matkul = [mk1, mk2, mk3, mk4, mk5, mk6, mk7, mk8]

# DATA MAHASISWA
m1 = Mahasiswa("Nayzila", "2312345678", "Sistem Informasi")
m2 = Mahasiswa("Sukma", "2312345679", "Teknik Informatika")
m3 = Mahasiswa("Khofifah", "2312345680", "Sistem Informasi")
m4 = Mahasiswa("Elfina", "2312345681", "Teknik Informatika")
m5 = Mahasiswa("Adib", "2312345682", "Sistem Informasi")
m6 = Mahasiswa("Vindi", "2312345683", "Teknik Informatika")

# Setiap mahasiswa minimal 4 matkul
m1.tambah_matkul(mk1)
m1.tambah_matkul(mk3)
m1.tambah_matkul(mk5)
m1.tambah_matkul(mk7)

m2.tambah_matkul(mk2)
m2.tambah_matkul(mk4)
m2.tambah_matkul(mk6)
m2.tambah_matkul(mk8)

m3.tambah_matkul(mk1)
m3.tambah_matkul(mk2)
m3.tambah_matkul(mk3)
m3.tambah_matkul(mk4)

m4.tambah_matkul(mk5)
m4.tambah_matkul(mk6)
m4.tambah_matkul(mk7)
m4.tambah_matkul(mk8)

m5.tambah_matkul(mk1)
m5.tambah_matkul(mk4)
m5.tambah_matkul(mk6)
m5.tambah_matkul(mk8)

m6.tambah_matkul(mk2)
m6.tambah_matkul(mk3)
m6.tambah_matkul(mk5)
m6.tambah_matkul(mk7)

# OBJEK KAMPUS
kampus1 = Kampus("Universitas Trunojoyo Madura ", "Bangkalan")

# TAMPILKAN SEMUA DATA
print("\n=== DATA MAHASISWA ===")
for m in [m1, m2, m3, m4, m5, m6]:
    m.tampilkan_info()

print("\n=== INFO KAMPUS ===")
Kampus.tampilkan_info_kampus(kampus1.nama, kampus1.alamat)

print("\nApakah nama kampus valid?", Kampus.validasi_nama_kampus(kampus1.nama))
