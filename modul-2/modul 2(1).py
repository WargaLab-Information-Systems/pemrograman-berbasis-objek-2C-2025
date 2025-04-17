class MataKuliah:
    def __init__(self, kode, nama, sks):
        if MataKuliah.valid_sks(sks):
            self.kode = kode
            self.nama = nama
            self.sks = sks
        else:
            print(f"Mata kuliah '{nama}' dengan SKS {sks} tidak valid (harus 2 atau 3 SKS).")
            self.kode = None
            self.nama = None
            self.sks = None

    @staticmethod
    def valid_sks(sks):
        return sks in [2, 3]

class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if Mahasiswa.valid_nim(nim):
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.matkul = []
            Mahasiswa.total_mahasiswa += 1
        else:
            self.nama = None
            self.nim = None
            self.prodi =None

    def tambah_matkul(self, matkul):
        if matkul.nama:
            self.matkul.append(matkul)

    def tampilkan_info(self):
        if len(self.matkul) < 4:
            print(f"{self.nama} matakuliah kurang minimal menggambil 4")
            return
        
        print(f"Nama   : {self.nama}")
        print(f"NIM    : {self.nim}")
        print(f"Prodi  : {self.prodi}")
        print("Mata Kuliah Diambil:")
        for mk in self.matkul:
            print(f"- {mk.kode} {mk.nama} {mk.sks} SKS")
        print("-"*25)

    @classmethod
    def tampilkan_total(cls):
        print(f"Total Mahasiswa: {cls.total_mahasiswa}")

    @staticmethod
    def valid_nim(nim):
        return nim.startswith("23") and len(nim) == 10 and nim.isdigit()

class Kampus:
    jumlah_mahasiswa = 0 

    def __init__(self, nama, alamat):
        if Kampus.valid_nama(nama):
            self.nama = nama
            self.alamat = alamat
        else:
            self.nama = None
            self.alamat = alamat

        Kampus.jumlah_mahasiswa = Mahasiswa.total_mahasiswa

    @classmethod
    def tampilkan_info_kampus(cls, nama_kampus):
        print(f"Nama Kampus     : {nama_kampus}")
        print(f"Total Mahasiswa   : {cls.jumlah_mahasiswa}")

    @staticmethod
    def valid_nama(nama):
        return not any(char.isdigit() for char in nama)

# Minimal 8 objek MataKuliah
matkul_list = [
    MataKuliah("MK001", "PBO", 3),
    MataKuliah("MK002", "PBD", 2),
    MataKuliah("MK003", "DMJ", 3),
    MataKuliah("MK004", "PBW", 2),
    MataKuliah("MK005", "ABP", 2),
    MataKuliah("MK006", "PAI", 3),
    MataKuliah("MK007", "PTIK", 2),
    MataKuliah("MK008", "MOB", 2)
]

# Minimal 6 objek Mahasiswa
mhs1 = Mahasiswa("ANDI", "2312345678", "ELEKTRO")
mhs2 = Mahasiswa("BUDI", "2312345679", "MEKATRO")
mhs3 = Mahasiswa("CICI", "2312345680", "ELEKTRO")
mhs4 = Mahasiswa("DEDI", "2312345681", "INDUSTRI")
mhs5 = Mahasiswa("HERI",  "2312345682", "INDUSTRI")
mhs6 = Mahasiswa("SISI", "2312345683", "MEKATRO")

# Setiap mahasiswa harus mengambil minimal 4 mata kuliah
for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    mhs.tambah_matkul(matkul_list[0])
    mhs.tambah_matkul(matkul_list[1])
    mhs.tambah_matkul(matkul_list[2])
    mhs.tambah_matkul(matkul_list[3])

#Minimal 1 objek Kampus
kampus = Kampus("Universitas Pemrograman Nihhh", "Jl. Belajar Coding kuy No.1")

# menampilkan hasil
print("DATA MAHASISWA :")
for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    if mhs.nama:
        mhs.tampilkan_info()
    else:
        print("Data mahasiswa tidak valid.")

print("\n DATA KAMPUS :")
Kampus.tampilkan_info_kampus(kampus.nama)
print("Nama kampus valid:", Kampus.valid_nama(kampus.nama))