class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not self.validasi_sks(sks):
            print(f"  SKS {sks} tidak valid! Di-set ke default 2.")
            sks = 2
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks == 2 or sks == 3


class Mahasiswa:
    total_mahasiswa = 0
    daftar_nim = set()

    def __init__(self, nama, nim, prodi):
        while not self.validasi_nim(nim):
            print("NIM tidak valid! Harus 10 digit angka dan diawali dengan '23'.")
            nim = input("Masukkan ulang NIM: ")

        while nim in Mahasiswa.daftar_nim:
            print("NIM sudah terdaftar! Masukkan NIM yang berbeda.")
            nim = input("Masukkan ulang NIM: ")
            while not self.validasi_nim(nim):
                print("NIM tidak valid! Harus 10 digit angka dan diawali dengan '23'.")
                nim = input("Masukkan ulang NIM: ")

        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []

        Mahasiswa.daftar_nim.add(nim)
        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        if matkul in self.matkul_diambil:
            print(f"  Mata kuliah {matkul.nama} sudah diambil sebelumnya.")
        else:
            self.matkul_diambil.append(matkul)

    def tampilkan_biodata(self):
        print(f"\nMahasiswa: {self.nama}, NIM: {self.nim}, Prodi: {self.prodi}")
        print("Mata Kuliah yang diambil:")
        for m in self.matkul_diambil:
            print(f"  > {m.nama} ({m.sks} SKS)")

    @classmethod
    def jumlah_mahasiswa(cls):
        return cls.total_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return nim.isdigit() and nim.startswith(23) and len(nim) == 10


class Kampus:
    total_mahasiswa = 0

    def __init__(self, nama, alamat):
        while not self.validasi_nama(nama):
            print("Nama kampus tidak valid! Tidak boleh mengandung angka atau simbol.")
            nama = input("Masukkan ulang nama kampus: ")
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def set_total_mahasiswa(cls, jumlah):
        cls.total_mahasiswa = jumlah

    @staticmethod
    def validasi_nama(nama):
        return nama.replace(" ", "").isalpha()

matkul_info = {
    "MK001": "Pemrograman",
    "MK002": "Matematika",
    "MK003": "Fisika",
    "MK004": "Kimia",
    "MK005": "Bahasa Inggris",
    "MK006": "Etika Profesi",
    "MK007": "Basis Data",
    "MK008": "Algoritma"
}

print("\n=== DAFTAR MATA KULIAH TERSEDIA ===")
for kode, nama in matkul_info.items():
    print(f"  {kode}: {nama}")

mahasiswa_list = []
while True:
    try:
        jumlah_mhs = int(input("\nMasukkan jumlah mahasiswa (minimal 6): "))
        if jumlah_mhs >= 1:
            break
        else:
            print("Jumlah minimal mahasiswa adalah 6!")
    except ValueError:
        print("Masukkan angka yang valid!")

for i in range(jumlah_mhs):
    print(f"\nMahasiswa ke-{i+1}:")
    nama = input("  Nama: ")
    nim = input("  NIM: ")
    prodi = input("  Prodi: ")

    mhs = Mahasiswa(nama, nim, prodi)

    while True:
        print("Masukkan minimal 4 kode mata kuliah yang diambil (pisahkan dengan koma):")
        kode_input = input("  Kode MK: ").replace(" ", "").upper().split(',')

        if len(kode_input) < 4:
            print("Minimal 4 mata kuliah harus diambil!")
            continue

        semua_kode_valid = all(kode in matkul_info for kode in kode_input)
        if not semua_kode_valid:
            print("Satu atau lebih kode tidak ditemukan. Silakan masukkan ulang.")
            continue

        for kode in kode_input:
            nama_matkul = matkul_info[kode]
            while True:
                sks_input = input(f"Masukkan SKS untuk {nama_matkul} ({kode}) [2/3]: ")
                if sks_input.isdigit():
                    sks = int(sks_input)
                    if MataKuliah.validasi_sks(sks):
                        break
                    else:
                        print("SKS tidak valid! Harus 2 atau 3.")
                else:
                    print("SKS harus berupa angka!")
            matkul = MataKuliah(kode, nama_matkul, sks)
            mhs.tambah_matkul(matkul)
        break

    mahasiswa_list.append(mhs)

print("\n--- Input Data Kampus ---")
nama_kampus = input("Nama kampus: ")
alamat_kampus = input("Alamat kampus: ")
kampus = Kampus(nama_kampus, alamat_kampus)

Kampus.set_total_mahasiswa(Mahasiswa.jumlah_mahasiswa())

print("\n--- INFORMASI MAHASISWA ---")
for mhs in mahasiswa_list:
    mhs.tampilkan_biodata()

print("\n--- INFORMASI KAMPUS ---")
print(f"Nama Kampus: {kampus.nama}")
print(f"Alamat: {kampus.alamat}")
print(f"Nama kampus valid? {'Ya' if Kampus.validasi_nama(kampus.nama) else 'Tidak'}")
print(f"Total Mahasiswa: {Kampus.total_mahasiswa}")