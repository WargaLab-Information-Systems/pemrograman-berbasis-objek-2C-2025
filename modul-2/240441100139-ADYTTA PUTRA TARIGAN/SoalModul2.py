class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim):
        if Mahasiswa.validasi_nim(nim):
            self.nama = nama
            self.nim = nim
            Mahasiswa.jumlah_mahasiswa += 1
            Kampus.jumlah_mahasiswa += 1
        else:
            self.nama = "Tidak Valid"
            self.nim = "-"

        self.matkul = []

    def tambah_matkul(self, mk):
        self.matkul.append(mk)

    def info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Mata kuliah diambil:")
        for m in self.matkul:
            print("-", m.nama, m.kode, f"({m.sks} SKS)")
        print()

    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10 and nim.isdigit()


class MataKuliah:
    def __init__(self, kode, nama, sks):
        if MataKuliah.cek_sks_valid(sks):
            self.kode = kode
            self.nama = nama
            self.sks = sks
        else:
            self.nama = "Tidak Valid"
            self.sks = 0

    @staticmethod
    def cek_sks_valid(sks):
        return sks in [2, 3]

class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    def info(self):
        print("Nama Kampus:", self.nama)
        print("Alamat:", self.alamat)
        print("Total Mahasiswa:", Kampus.jumlah_mahasiswa)

    @classmethod
    def info_kampus(cls, nama):
        print(f"Nama Kampus: {nama}")
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def cek_nama_valid_static(nama):
        if any(char.isdigit() for char in nama):
            print("Nama kampus tidak valid (mengandung angka)")
        else:
            print("Nama kampus valid")

kampus = Kampus("UN1", "Bangkalan, Madura")

matkuls = [
    MataKuliah("501", "DMJ", 3),
    MataKuliah("502", "Apb", 2),
    MataKuliah("503", "Pbd", 3),
    MataKuliah("504", "Kewarganegaraan", 2),
    MataKuliah("505", "Inggris", 2),
    MataKuliah("506", "Pemrograman", 3),
    MataKuliah("507", "Basis Data", 3),
    MataKuliah("508", "Algoritma", 3)
]

m1 = Mahasiswa("Adytta", "2312345678")
m2 = Mahasiswa("Fauzi", "2312345679")
m3 = Mahasiswa("Teddy", "2312345680")
m4 = Mahasiswa("Abdul", "2312345681")
m5 = Mahasiswa("Ilham", "2312345682")
m6 = Mahasiswa("Syawal", "2312345683")

semua_mhs = [m1, m2, m3, m4, m5, m6]

for mhs in semua_mhs:
        mhs.tambah_matkul(matkuls[0])
        mhs.tambah_matkul(matkuls[1])
        mhs.tambah_matkul(matkuls[2])
        mhs.tambah_matkul(matkuls[3])


print("=== Data Mahasiswa ===")
for mhs in semua_mhs:
    mhs.info()

print("=== Data Kampus ===")
kampus.info()
Kampus.cek_nama_valid_static(kampus.nama)