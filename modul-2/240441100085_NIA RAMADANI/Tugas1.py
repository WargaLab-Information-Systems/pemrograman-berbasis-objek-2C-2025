class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.Validasi_sks(sks):
            raise ValueError(f"SKS {sks} tidak valid untuk {nama}. Hanya boleh 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def tampil(self):
        return f"{self.kode} - {self.nama} ({self.sks} SKS)"

    @staticmethod
    def Validasi_sks(sks):
        return sks == 2 or sks == 3

class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError(f"NIM {nim} tidak valid! Harus mulai dengan '23' dan terdiri dari 10 digit.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"NIM   : {self.nim}")
        print(f"Prodi : {self.prodi}")
        print("Mata Kuliah yang Diambil:")
        for matkul in self.matkul_diambil:
            print(f" - {matkul.tampil()}")
        print("-" * 40)

    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10 and nim.isdigit()

class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama(nama):
            raise ValueError(f"Nama kampus '{nama}' tidak valid. Tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat
        Kampus.jumlah_mahasiswa = Mahasiswa.jumlah_mahasiswa()

    @classmethod
    def tampilkan_info(cls, kampus_obj):
        print(f"Nama Kampus     : {kampus_obj.nama}")
        print(f"Alamat Kampus   : {kampus_obj.alamat}")
        print(f"Jumlah Mahasiswa: {cls.jumlah_mahasiswa}")
        print(f"Nama kampus valid? {'Ya' if Kampus.validasi_nama(kampus_obj.nama) else 'Tidak'}")

    @staticmethod
    def validasi_nama(nama):
        return not any(char.isdigit() for char in nama)

try:
    matkul1 = MataKuliah("MK001", "Algoritma pemrograman", 3)
    matkul2 = MataKuliah("MK002", "Bahasa Inggris", 2)
    matkul3 = MataKuliah("MK003", "Statistika", 2)
    matkul4 = MataKuliah("MK004", "Agama", 2)
    matkul5 = MataKuliah("MK005", "Pemrograman Basis Web", 3)
    matkul6 = MataKuliah("MK006", "Desain Manajemen Jaringan", 3)
    matkul7 = MataKuliah("MK007", "Pemrograman Basis Objek", 2)
    matkul8 = MataKuliah("MK008", "Kewarganegaraan", 2)

    m1 = Mahasiswa("Reino", "2304411001", "Sistem Informasi")
    m2 = Mahasiswa("Naira", "2304411002", "Sistem Informasi")
    m3 = Mahasiswa("Gio", "2304411003", "Sistem Informasi")
    m4 = Mahasiswa("Winda", "2304411004", "Sistem Informasi")
    m5 = Mahasiswa("Seno", "2304411005", "Sistem informasi")
    m6 = Mahasiswa("Yona", "2304411006", "Sistem Informasi")

    for m in [m1, m2, m3, m4, m5, m6]:
        m.tambah_matkul(matkul1)
        m.tambah_matkul(matkul2)
        m.tambah_matkul(matkul3)
        m.tambah_matkul(matkul4)

    kampus1 = Kampus("Universitas Trunojoyo Madura", "Jl. Raya Telang, Bangkalan")

    print("\n=== DATA MAHASISWA ===")
    for m in [m1, m2, m3, m4, m5, m6]:
        m.tampilkan_info()

    print("=== DATA KAMPUS ===")
    Kampus.tampilkan_info(kampus1)

except ValueError as e:
    print(f"Terjadi kesalahan: {e}")
