class Mahasiswa:
    jumlah_mahasiswa = 0
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        if not self.cek_nim(nim):
            raise ValueError("NIM tidak valid")
        self.nim = nim
        self.prodi = prodi
        self.daftar_matkul = []
        Mahasiswa.jumlah_mahasiswa += 1
    
    def tambah_matkul(self, matkul):
        for matkul_duplikat in self.daftar_matkul:
            if matkul_duplikat.kode_matkul == matkul.kode_matkul:
                raise ValueError(f"{self.nama} sudah mengambil mata kuliah {matkul.nama_matkul} (Kode: {matkul.kode_matkul})")
        self.daftar_matkul.append(matkul)

    def tampilkan(self):
        print("\n" + "=" * 40)
        if len(self.daftar_matkul) < 4:
            print(f"{self.nama} harus mengambil minimal 4 mata kuliah. Saat ini hanya mengambil {len(self.daftar_matkul)} mata kuliah.")
        elif len(self.daftar_matkul) > 8:
            print(f"{self.nama} hanya boleh mengambil maksimal 8 mata kuliah.")
        else:
            print(f"Nama: {self.nama}")
            print(f"NIM: {self.nim}")
            print(f"Program Studi: {self.prodi}")
            print("Mata kuliah yang diambil:")
            for matkul in self.daftar_matkul:
                print(f" - {matkul.nama_matkul} (Kode: {matkul.kode_matkul}, SKS: {matkul.sks})")
        print("=" * 40)

    @classmethod
    def jumlah_mhs(cls):
        print(f"Jumlah mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def cek_nim(nim):
        if not isinstance(nim, str):
            print("NIM harus bertipe string")
            return False
        if not nim.startswith('23'):
            print("NIM harus dimulai dengan angka 23")
            return False
        if len(nim) == 10 and nim.isdigit():
            return True
        return False

class MataKuliah:
    def __init__(self, kode_matkul, nama_matkul, sks):
        self.kode_matkul = kode_matkul
        self.nama_matkul = nama_matkul
        self.sks = self.cek_sks(sks)
    
    @staticmethod
    def cek_sks(sks):
        if sks in [2, 3]:
            return sks
        raise ValueError("SKS harus 2 atau 3.")

class Kampus:
    daftar_mahasiswa = []
    def __init__(self, nama_kampus, alamat):
        self.nama_kampus = self.cek_nama(nama_kampus)
        self.alamat = alamat
    
    def jumlah_mhs(self):
        print(f"Jumlah mahasiswa di {self.nama_kampus}: {len(self.daftar_mahasiswa)}")

    @classmethod
    def tambah_mahasiswa(cls, mahasiswa):
        cls.daftar_mahasiswa.append(mahasiswa)

    @staticmethod
    def cek_nama(nama_kampus):
        if any(karakter.isdigit() for karakter in nama_kampus):
            raise ValueError("Nama kampus tidak boleh mengandung angka.")
        return nama_kampus

try:
    campus = Kampus("UTM", "Jl. Raya Telang")
    mhs1 = Mahasiswa("Amin", "2304411001", "SI")
    mhs2 = Mahasiswa("Denis", "2304411002", "SI")
    mhs3 = Mahasiswa("Adit", "2304411003", "SI")
    mhs4 = Mahasiswa("Jarwo", "2304411004", "SI")
    mhs5 = Mahasiswa("Sopo", "2304411005", "SI")
    mhs6 = Mahasiswa("Adel", "2304411006", "SI")

    mk1 = MataKuliah("SI001", "Alpro", 3)
    mk2 = MataKuliah("SI002", "Statistik", 3)
    mk3 = MataKuliah("SI003", "MO", 2)
    mk4 = MataKuliah("SI004", "KI", 2)
    mk5 = MataKuliah("SI005", "Pancasila", 2)
    mk6 = MataKuliah("SI006", "LE", 2)
    mk7 = MataKuliah("SI007", "PTIK", 3)
    mk8 = MataKuliah("SI008", "B. Inggris", 2)

    for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
        Kampus.tambah_mahasiswa(mhs)
        
    for matkul in [mk1, mk2, mk3, mk4]:
        mhs1.tambah_matkul(matkul)
    for matkul in [mk1, mk2, mk3, mk4, mk6]:
        mhs2.tambah_matkul(matkul)
    for matkul in [mk5, mk6, mk1, mk2]:
        mhs3.tambah_matkul(matkul)
    for matkul in [mk8, mk3, mk4, mk7, mk1, mk2, mk5, mk6]:
        mhs4.tambah_matkul(matkul)
    for matkul in [mk8, mk7, mk6, mk5, mk4]:
        mhs5.tambah_matkul(matkul)
    for matkul in [mk1, mk2, mk3, mk4, mk6, mk8, mk7]:
        mhs6.tambah_matkul(matkul)

    mhs1.tampilkan()
    mhs2.tampilkan()
    mhs3.tampilkan()
    mhs4.tampilkan()
    mhs5.tampilkan()
    mhs6.tampilkan()
    Mahasiswa.jumlah_mhs()
    campus.jumlah_mhs()
except ValueError as a:
    print(f"Error: {a}")