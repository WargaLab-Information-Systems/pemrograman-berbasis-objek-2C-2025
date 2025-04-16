# Class MataKuliah
class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.validasi_sks(sks):
            raise ValueError("SKS harus bernilai 2 atau 3")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]

# Class Mahasiswa
class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError("NIM tidak valid. Harus dimulai dengan '23' dan 10 digit")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_info(self):
        print(f"\nNama: {self.nama}\nNIM: {self.nim}\nProdi: {self.prodi}")
        print("Mata Kuliah Diambil:")
        for mk in self.matkul_diambil:
            print(f"-{mk.kode} {mk.nama}  {mk.sks} SKS")
        print("="*30)

    @classmethod
    def get_jumlah_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10 and nim.isdigit()

# Class Kampus
class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            raise ValueError("Nama kampus tidak boleh mengandung angka")
        self.nama = nama
        self.alamat = alamat
        Kampus.jumlah_mahasiswa = Mahasiswa.get_jumlah_mahasiswa()

    @classmethod
    def tampilkan_info_kampus(cls, nama_kampus):
        print(f"\nNama Kampus: {nama_kampus}")
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)

#membuat 8 objek matakuliah
matkul_list = [
    MataKuliah("MK001", " AlPro", 3),
    MataKuliah("MK002", "PBW", 2),
    MataKuliah("MK003", "PBO", 3),
    MataKuliah("MK004", "EBC", 3),
    MataKuliah("MK005", "APB", 3),
    MataKuliah("MK006", "DMJ", 2),
    MataKuliah("MK007", "PBD", 2),
    MataKuliah("MK008", "PAI", 3)
]

#membuat 6 objek mahasiswa dan menambahkan 4 mata kuliah ke masing-masing mahasiswa
mhs1 = Mahasiswa("Andi", "2312345678", " Teknik Informatika")
mhs1.tambah_matkul(matkul_list[0])
mhs1.tambah_matkul(matkul_list[2])
mhs1.tambah_matkul(matkul_list[4])
mhs1.tambah_matkul(matkul_list[5])

mhs2 = Mahasiswa("Budi", "2311112233", "Sistem Informasi")
mhs2.tambah_matkul(matkul_list[1])
mhs2.tambah_matkul(matkul_list[3])
mhs2.tambah_matkul(matkul_list[6])
mhs2.tambah_matkul(matkul_list[7])

mhs3 = Mahasiswa("Cici", "2300001111", " Tenik lInformatika")
mhs3.tambah_matkul(matkul_list[0])
mhs3.tambah_matkul(matkul_list[2])
mhs3.tambah_matkul(matkul_list[5])
mhs3.tambah_matkul(matkul_list[6])

mhs4 = Mahasiswa("Dedi", "2312121212", "Teknik Informatika")
mhs4.tambah_matkul(matkul_list[1])
mhs4.tambah_matkul(matkul_list[3])
mhs4.tambah_matkul(matkul_list[4])
mhs4.tambah_matkul(matkul_list[7])

mhs5 = Mahasiswa("Eka", "2311223344", "Sistem Informasi")
mhs5.tambah_matkul(matkul_list[2])
mhs5.tambah_matkul(matkul_list[4])
mhs5.tambah_matkul(matkul_list[6])
mhs5.tambah_matkul(matkul_list[0])

mhs6 = Mahasiswa("Fajar", "2310987654", "Teknik Informatika")
mhs6.tambah_matkul(matkul_list[3])
mhs6.tambah_matkul(matkul_list[5])
mhs6.tambah_matkul(matkul_list[7])
mhs6.tambah_matkul(matkul_list[1])

#1 objek kampus
kampus = Kampus("Universitas Trunojoyo Madura", "Jl. Raya Tellang")

#menampilkan info mahasiswa
for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    mhs.tampilkan_info()

#menampilkan info kampus
Kampus.tampilkan_info_kampus(kampus.nama)
print("Nama kampus valid:", Kampus.validasi_nama_kampus(kampus.nama))
