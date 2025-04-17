class Matkul:
    def __init__(self, kode, nama, sks):
        if not Matkul.validasi_sks(sks):
            raise ValueError("SKS hanya boleh 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]

    def __str__(self):
        return f"{self.nama} ({self.sks} SKS)"

class mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not mahasiswa.validasi_nim(nim):
            raise ValueError("NIM harus dimulai dengan '23' dan total 10 digit.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul = []
        mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul.append(matkul)

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Prodi: {self.prodi}")
        print("Mata Kuliah yang diambil:")
        for m in self.matkul:
            print(f"  - {m}")

    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def validasi_nim(nim):
       return nim.isdigit()and len(nim) == 10 and nim.startswith("23")
    
class Kampus:
    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            raise ValueError("Nama kampus tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"Kampus: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Total Mahasiswa: {mahasiswa.jumlah_mahasiswa()}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)

def input_kampus():
    while True: 
        try:
            nama = input("Masukkan nama kampus: ")
            alamat = input("Masukkan alamat kampus: ")
            return Kampus(nama, alamat)
        except ValueError as e:
            print(f"Error: {e}")

def input_matkul():
    matkul_list = []
    print("\n--- Input Mata Kuliah ---")
    for i in range(8):
        print(f"\nMata Kuliah ke-{i + 1}")
        kode = input("Kode: ").strip()
        nama = input("Nama: ")
        while True:
            try:
                sks = int(input("SKS (2 atau 3): "))
                mk = Matkul(kode, nama, sks)
                matkul_list.append(mk)
                break
            except ValueError as e:
                print(f"Error: {e}")
    return matkul_list

def input_mahasiswa(matkul_list):
    mhs_list = []
    print("\n--- Input Mahasiswa ---")
    for i in range(6):
        print(f"\nMahasiswa ke-{i + 1}")
        nama = input("Nama: ").strip()
        while True:
            try:
                nim = input("NIM (Harus mulai dengan 23 dan 10 digit): ").strip()
                prodi = input("Prodi: ")
                mhs = mahasiswa(nama, nim, prodi)
                break
            except ValueError as e:
                print(f"Error: {e}")
        pilih_matkul_untuk_mahasiswa(mhs, matkul_list)
        mhs_list.append(mhs)
    return mhs_list

def pilih_matkul_untuk_mahasiswa(mhs, matkul_list):
    print("\nPilih minimal 4 mata kuliah (masukkan nomor-nya):")
    for idx, mk in enumerate(matkul_list):
        print(f"{idx + 1}. {mk}")
    while True:
        try:
            pilihan = input("Masukkan nomor matkul (pisahkan dengan koma): ").split(",")
            pilihan = [int(p.strip()) for p in pilihan if p.strip()]
            if len(pilihan) < 4:
                raise ValueError("Minimal 4 mata kuliah!")
            for p in pilihan:
                matkul = matkul_list[p - 1]
                if matkul not in mhs.matkul:
                    mhs.tambah_matkul(matkul)
            break
        except Exception as e:
            print(f"Error: {e}")

kampus = input_kampus()
matkul_list = input_matkul()
mhs_list = input_mahasiswa(matkul_list)

print("=== Data Mahasiswa ===")
for mhs in mhs_list:
    print("-" * 30)
    mhs.tampilkan_info()

print("\n" + "=" * 40)
print("=== Data Kampus ===")
kampus.tampilkan_info()

if Kampus.validasi_nama_kampus(kampus.nama):
    print("Status Nama Kampus: Valid")
else:
    print("Status Nama Kampus: Tidak Valid")