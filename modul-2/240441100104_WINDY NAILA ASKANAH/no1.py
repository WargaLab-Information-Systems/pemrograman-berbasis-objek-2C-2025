class Mahasiswa:
    Total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError("NIM harus dimulai dengan '23' dan 10 digit")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.Total_mahasiswa += 1

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
        return cls.Total_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10 and nim.isdigit()
    
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


class Kampus:
    Total_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            raise ValueError("Nama kampus tidak boleh ada angkanya")
        self.nama = nama
        self.alamat = alamat
        Kampus.Total_mahasiswa = Mahasiswa.get_jumlah_mahasiswa()

    @classmethod
    def tampilkan_info_kampus(cls, nama_kampus):
        print(f"\nNama Kampus: {nama_kampus}")
        print(f"Total Mahasiswa: {cls.Total_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)

matkul_list = [
    MataKuliah("MK001", "B.ING", 2),
    MataKuliah("MK002", "PBW", 3),
    MataKuliah("MK003", "EBC", 3),
    MataKuliah("MK004", "PBO", 3),
    MataKuliah("MK005", "APB", 2),
    MataKuliah("MK006", "DMJ", 2),
    MataKuliah("MK007", "PAI", 2),
    MataKuliah("MK008", "PBD", 3)
]

mhs1 = Mahasiswa("windy", "2312344783", "Sistem informasi")
mhs1.tambah_matkul(matkul_list[0])
mhs1.tambah_matkul(matkul_list[2])
mhs1.tambah_matkul(matkul_list[4])
mhs1.tambah_matkul(matkul_list[5])

mhs2 = Mahasiswa("naila", "2311118888", "Sistem Informasi")
mhs2.tambah_matkul(matkul_list[1])
mhs2.tambah_matkul(matkul_list[3])
mhs2.tambah_matkul(matkul_list[6])
mhs2.tambah_matkul(matkul_list[7])

mhs3 = Mahasiswa("askanah", "2300009876", " Sistem Informasi")
mhs3.tambah_matkul(matkul_list[0])
mhs3.tambah_matkul(matkul_list[2])
mhs3.tambah_matkul(matkul_list[5])
mhs3.tambah_matkul(matkul_list[6])

mhs4 = Mahasiswa("sica", "2312123434", "Teknik Informatika")
mhs4.tambah_matkul(matkul_list[1])
mhs4.tambah_matkul(matkul_list[3])
mhs4.tambah_matkul(matkul_list[4])
mhs4.tambah_matkul(matkul_list[7])

mhs5 = Mahasiswa("tari", "2311227788", "Teknik Informatika")
mhs5.tambah_matkul(matkul_list[2])
mhs5.tambah_matkul(matkul_list[4])
mhs5.tambah_matkul(matkul_list[6])
mhs5.tambah_matkul(matkul_list[0])

mhs6 = Mahasiswa("dwi", "2310981234", "Sistem Informasi")
mhs6.tambah_matkul(matkul_list[3])
mhs6.tambah_matkul(matkul_list[5])
mhs6.tambah_matkul(matkul_list[7])
mhs6.tambah_matkul(matkul_list[1])

kampus = Kampus("Universitas Trunojoyo Madura", "Jl. Raya Telang")

for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    mhs.tampilkan_info()

Kampus.tampilkan_info_kampus(kampus.nama)
print("Nama kampus valid:", Kampus.validasi_nama_kampus(kampus.nama))