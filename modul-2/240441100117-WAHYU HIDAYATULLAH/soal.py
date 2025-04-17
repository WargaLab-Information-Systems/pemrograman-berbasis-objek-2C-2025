class Mahasiswa:
    data_mahasiswa = []

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError(f"NIM '{nim}' tidak valid. Harus diawali '23' dan harus 10 digit.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.data_mahasiswa.append(self)
        Kampus.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def info_mahasiswa(self):
        print(f"Nama          : {self.nama}")
        print(f"NIM           : {self.nim}")
        print(f"Prodi         : {self.prodi}")
        print("Matakuliah yang berhasil diambil:")
        for matkul in self.matkul_diambil:
            print(f"- {matkul.nama} ({matkul.kode_matkul}) {matkul.jumlah_sks} SKS")
        print("-" * 40)

    @classmethod
    def get_jumlah_mahasiswa(cls):
        return len(cls.data_mahasiswa)

    @staticmethod
    def validasi_nim(nim):
        return (
            len(nim) == 10 and
            nim[:2] == "23" and
            nim.isdigit()
        )


class Matakuliah:
    def __init__(self, kode_matkul, nama, jumlah_sks):
        if not Matakuliah.validasi_sks(jumlah_sks):
            raise ValueError(f"SKS '{jumlah_sks}' tidak valid. Harus 2 atau 3!")
        self.kode_matkul = kode_matkul
        self.nama = nama
        self.jumlah_sks = jumlah_sks

    @staticmethod
    def validasi_sks(jumlah_sks):
        return jumlah_sks in (2, 3)

class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama_kampus, alamat_kampus):
        if not Kampus.validasi_nama_kampus(nama_kampus):
            raise ValueError("Nama kampus tidak boleh mengandung angka!")
        self.nama_kampus = nama_kampus
        self.alamat_kampus = alamat_kampus

    @staticmethod
    def validasi_nama_kampus(nama_kampus):
        return all(not char.isdigit() for char in nama_kampus)

    @classmethod
    def info_kampus(cls, kampus_instance):
        print(f"Nama Kampus     : {kampus_instance.nama_kampus}")
        print(f"Alamat          : {kampus_instance.alamat_kampus}")
        print(f"Total Mahasiswa : {cls.jumlah_mahasiswa}")
        print("-" * 40)

matkul_list = [
    Matakuliah("MK001", "PBO", 3),
    Matakuliah("MK002", "APB", 3),
    Matakuliah("MK003", "DMJ", 2),
    Matakuliah("MK004", "PAI", 3),
    Matakuliah("MK005", "PBD", 2),
    Matakuliah("MK006", "PBW", 2),
    Matakuliah("MK007", "E-Business", 3),
    Matakuliah("MK008", "B.Inggris", 2),
]

kampus = Kampus("Universitas Trunojoyo Madura", "Jl. Raya Telang")

mahasiswa_list = [
    Mahasiswa("Wahyu", "2304411001", "Sistem Informasi"),
    Mahasiswa("Faisal", "2304411002", "Sistem Informasi"),
    Mahasiswa("Adyt", "2304411003", "Sistem Informasi"),
    Mahasiswa("Yoga", "2304411004", "Sistem Informasi"),
    Mahasiswa("Zaki", "2304411005", "Sistem Informasi"),
    Mahasiswa("Dafa", "2304411006", "Sistem Informasi")
]

for i, mhs in enumerate(mahasiswa_list):
    for j in range(4):
        index_matkul = (i + j) % len(matkul_list)
        mhs.tambah_matkul(matkul_list[index_matkul])

print("\n=== Data Mahasiswa ===\n")
for mhs in mahasiswa_list:
    mhs.info_mahasiswa()

print("\n=== Info Kampus ===\n")
Kampus.info_kampus(kampus)