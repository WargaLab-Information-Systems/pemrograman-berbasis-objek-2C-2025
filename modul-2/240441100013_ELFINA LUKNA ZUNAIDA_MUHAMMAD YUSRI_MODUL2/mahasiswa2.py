class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not self.validasi_nim(nim):
            raise ValueError("NIM tidak valid")
        
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.daftar_matkul = []
        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        if len(self.daftar_matkul) >= 4:
            print("Mahasiswa sudah mengambil maksimal 4 mata kuliah")
        else:
            self.daftar_matkul.append(matkul)

    def tampilkan_info(self):
        print(f"\nNama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah:")
        for matkul in self.daftar_matkul:
            print(f"- {matkul.nama} ({matkul.kode}), SKS: {matkul.sks}")

    @classmethod
    def get_total_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return isinstance(nim, str) and nim.startswith("23") and len(nim) == 10 and nim.isdigit()

class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not self.validasi_sks(sks):
            raise ValueError("SKS tidak valid")
        
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]

class Kampus:
    def __init__(self, nama, alamat):
        if not self.validasi_nama(nama):
            raise ValueError("Nama kampus tidak valid")
        
        self.nama = nama
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"\nNama Kampus: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Total Mahasiswa: {Mahasiswa.get_total_mahasiswa()}")
        print(f"Nama Valid: {'Ya' if self.validasi_nama(self.nama) else 'Tidak'}")

    @staticmethod
    def validasi_nama(nama):
        return isinstance(nama, str) and len(nama) > 0 and not any(c.isdigit() for c in nama)

kampus = Kampus("Universitas Bina Bangsa Jaya", "Jl. Manggis No. 1")

matkul = [
    MataKuliah("MK001", "APB", 3),
    MataKuliah("MK002", "PAI", 3),
    MataKuliah("MK003", "Bahasa Inggris", 3),
    MataKuliah("MK004", "Basis Data", 3),
    MataKuliah("MK005", "Bahasa Inddonesia", 2),
    MataKuliah("MK006", "PBO", 2),
    MataKuliah("MK007", "PBW", 2),
    MataKuliah("MK008", "Statistika", 2)
]

mhss = [
    Mahasiswa("Fina", "2312345678", "Informatika"),
    Mahasiswa("Finfin", "2312345678", "Sistem Informasi"),
    Mahasiswa("Clara", "2312345678", "Teknik Komputer"),
    Mahasiswa("Dewa", "2312345678", "Ilmu Komputer"),
    Mahasiswa("Cici", "2312345678", "Teknik Elektro"),
    Mahasiswa("Fani", "2312345678", "Sistem Informasi")
]

for i, mhs in enumerate(mhss):
    start = i % 4
    for j in range(4):
        mhs.tambah_matkul(matkul[start + j])

print("=== INFO MAHASISWA ===")
for mhs in mhss:
    mhs.tampilkan_info()

print("\n=== INFO KAMPUS ===")
kampus.tampilkan_info()




