class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError("NIM harus dimulai dengan '23' dan terdiri dari 10 digit.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.mata_kuliah = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_mata_kuliah(self, mata_kuliah):
        if len(self.mata_kuliah) >= 4:
            print("Mahasiswa sudah mengambil 4 mata kuliah.")
        else:
            self.mata_kuliah.append(mata_kuliah)

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah:")
        for matkul in self.mata_kuliah:
            print(f"  - {matkul}")

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"Jumlah Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        return nim.isdigit() and nim.startswith("23") and len(nim) == 10


class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.validasi_sks(sks):
            raise ValueError("SKS harus 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"{self.kode} - {self.nama} ({self.sks} SKS)"

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]


class Kampus:
    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            raise ValueError("Nama kampus tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampilkan_info_kampus(cls, kampus):
        print(f"Nama Kampus: {kampus.nama}")
        print(f"Alamat Kampus: {kampus.alamat}")
        print(f"Total Mahasiswa: {Mahasiswa.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)



daftar_mahasiswa = []
for i in range(6):
    print(f"\n=== Input Mahasiswa {i+1} ===")
    while True:
        nama = input("Nama: ")
        nim = input("NIM: ")
        prodi = input("Prodi: ")
        if Mahasiswa.validasi_nim(nim):
            mahasiswa = Mahasiswa(nama, nim, prodi)
            daftar_mahasiswa.append(mahasiswa)
            break
        else:
            print("NIM tidak valid. Harus diawali dengan '23' dan 10 digit.")

daftar_matkul = []
for i in range(8):
    print(f"\n=== Input Mata Kuliah {i+1} ===")
    while True:
        kode = input("Kode: ")
        nama = input("Nama: ")
        sks_input = input("SKS (2 atau 3): ")
        if sks_input.isdigit():
            sks = int(sks_input)
            if MataKuliah.validasi_sks(sks):
                matkul = MataKuliah(kode, nama, sks)
                daftar_matkul.append(matkul)
                break
            else:
                print("SKS harus 2 atau 3.")
        else:
            print("SKS harus berupa angka.")


for mahasiswa in daftar_mahasiswa:
    print(f"\n=== Pilih Mata Kuliah untuk {mahasiswa.nama} ===")
    for i in range(4):
        print("\nDaftar Mata Kuliah:")
        for j, matkul in enumerate(daftar_matkul):
            print(f"{j+1}. {matkul}")
        while True:
            pilihan_input = input(f"Pilih mata kuliah {i+1} (1-{len(daftar_matkul)}): ")
            if pilihan_input.isdigit():
                pilihan = int(pilihan_input)
                if 1 <= pilihan <= len(daftar_matkul):
                    mahasiswa.tambah_mata_kuliah(daftar_matkul[pilihan - 1])
                    break
            print("Pilihan tidak valid. Ulangi.")


print("\n=== Input Data Kampus ===")
while True:
    nama_kampus = input("Nama Kampus: ")
    alamat_kampus = input("Alamat Kampus: ")
    if Kampus.validasi_nama_kampus(nama_kampus):
        kampus = Kampus(nama_kampus, alamat_kampus)
        break
    else:
        print("Nama kampus tidak boleh mengandung angka.")

print("\n=== Informasi Mahasiswa ===")
print("==============================")
for mhs in daftar_mahasiswa:
    mhs.tampilkan_biodata()
    print("------------------------------")

print("\n=== Informasi Kampus ===")
print("==============================")
Kampus.tampilkan_info_kampus(kampus)
