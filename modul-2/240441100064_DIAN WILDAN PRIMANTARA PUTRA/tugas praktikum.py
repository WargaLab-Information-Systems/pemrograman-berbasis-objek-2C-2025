class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError(f"NIM tidak valid untuk mahasiswa {nama}! ")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.mata_kuliah = []
        Mahasiswa.jumlah_mahasiswa += 1
        Kampus.total_mahasiswa += 1

    def tambah_mata_kuliah(self, mata_kuliah):
        if mata_kuliah not in self.mata_kuliah:
            self.mata_kuliah.append(mata_kuliah)

    def tampilkan_biodata(self):
        print("\nMahasiswa:", self.nama)
        print("NIM:", self.nim)
        print("Prodi:", self.prodi)
        print("Mata Kuliah:")
        for mk in self.mata_kuliah:
            if mk.sks == 4:
                print(f"  - {mk.kode} - {mk.nama} ({mk.sks} SKS) Invalid")
            else:
                print(f"  - {mk.kode} - {mk.nama} ({mk.sks} SKS)")

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print("Jumlah mahasiswa:", cls.jumlah_mahasiswa)

    @staticmethod
    def validasi_nim(nim):
        return nim[:2] == "23" and len(nim) == 10 and nim.isdigit()

class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]

class Kampus:
    total_mahasiswa = 0

    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampilkan_info(cls, kampus):
        print("Kampus:", kampus.nama)
        print("Alamat:", kampus.alamat)
        print("Total Mahasiswa:", cls.total_mahasiswa)

    @staticmethod
    def validasi_nama_kampus(nama):
        return nama.replace(" ","").isalpha()

kampus = Kampus("Universitas Trunojoyo Madura", "Jalan Raya, Telang")

mk1 = MataKuliah("CS101", "Alpro", 3)
mk2 = MataKuliah("CS102", "Pbo", 3)
mk3 = MataKuliah("CS103", "Pbw", 3)
mk4 = MataKuliah("CS104", "Pbd", 3)
mk5 = MataKuliah("CS105", "LE", 2)
mk6 = MataKuliah("CS106", "Ebc", 3)
mk7 = MataKuliah("CS107", "Pai", 2)
mk8 = MataKuliah("CS108", "Dmj", 4)

mahasiswa_list = []

data_mhs = [
    ("Dian",  "2304411064", "SI"),
    ("Jefri", "2304411114", "SI"),
    ("Hilmiy", "2304411066", "SI"),
    ("Rendi", "2304411023", "SI"),
    ("Dimas", "2304411098", "SI"),
    ("Putra", "2304411054",  "SI"), 
]

for nama, nim, prodi in data_mhs:
    try:
        mhs = Mahasiswa(nama, nim, prodi)
        mahasiswa_list.append(mhs)
    except ValueError as e:
        print(f"Error: {e}")

if len(mahasiswa_list) >= 6:
    mahasiswa_list[0].tambah_mata_kuliah(mk1)
    mahasiswa_list[0].tambah_mata_kuliah(mk2)
    mahasiswa_list[0].tambah_mata_kuliah(mk3)
    mahasiswa_list[0].tambah_mata_kuliah(mk4)

    mahasiswa_list[1].tambah_mata_kuliah(mk2)
    mahasiswa_list[1].tambah_mata_kuliah(mk3)
    mahasiswa_list[1].tambah_mata_kuliah(mk5)
    mahasiswa_list[1].tambah_mata_kuliah(mk6)

    mahasiswa_list[2].tambah_mata_kuliah(mk1)
    mahasiswa_list[2].tambah_mata_kuliah(mk4)
    mahasiswa_list[2].tambah_mata_kuliah(mk7)
    mahasiswa_list[2].tambah_mata_kuliah(mk8)

    mahasiswa_list[3].tambah_mata_kuliah(mk3)
    mahasiswa_list[3].tambah_mata_kuliah(mk4)
    mahasiswa_list[3].tambah_mata_kuliah(mk5)
    mahasiswa_list[3].tambah_mata_kuliah(mk6)

    mahasiswa_list[4].tambah_mata_kuliah(mk1)
    mahasiswa_list[4].tambah_mata_kuliah(mk2)
    mahasiswa_list[4].tambah_mata_kuliah(mk7)
    mahasiswa_list[4].tambah_mata_kuliah(mk8)

    mahasiswa_list[5].tambah_mata_kuliah(mk2)
    mahasiswa_list[5].tambah_mata_kuliah(mk4)
    mahasiswa_list[5].tambah_mata_kuliah(mk6)
    mahasiswa_list[5].tambah_mata_kuliah(mk8)

print("\n--- INFORMASI KAMPUS ---")
Kampus.tampilkan_info(kampus)
print("Nama kampus valid:", Kampus.validasi_nama_kampus(kampus.nama))

print("\n--- INFORMASI MAHASISWA ---")
Mahasiswa.tampilkan_jumlah_mahasiswa()

print("\n--- BIODATA MAHASISWA ---")
for mhs in mahasiswa_list:
    mhs.tampilkan_biodata()