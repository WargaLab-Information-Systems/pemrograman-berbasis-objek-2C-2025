class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi, kampus):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.kampus = kampus
        self.daftar_matkul = []
        Mahasiswa.jumlah_mahasiswa += 1
        kampus.tambah_mahasiswa()

    def tambah_matkul(self, matkul):
        if len(self.daftar_matkul) >= 4:
            print(f"Peringatan: {self.nama} sudah mengambil 4 mata kuliah. Mata kuliah {matkul.nama} tetap ditambahkan.")
        self.daftar_matkul.append(matkul)

    def tampilkan_biodata(self):
        print(f"\nBiodata Mahasiswa:")
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print(f"Mata Kuliah yang diambil:")
        for i, matkul in enumerate(self.daftar_matkul, 1):
            print(f"{i}. {matkul.info_matkul()}")

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10 and nim.isdigit()


class MataKuliah:
    def __init__(self, kodeMT, nama, sks):
        if not MataKuliah.validasi_sks(sks):
            print(f"SKS untuk mata kuliah {nama} tidak valid. SKS harus 2 atau 3.")
            self.valid = False
            return
        self.kodeMT = kodeMT
        self.nama = nama
        self.sks = sks
        self.valid = True

    def info_matkul(self):
        return f"{self.kodeMT} - {self.nama} - ({self.sks} SKS)"

    @staticmethod
    def validasi_sks(sks):
        return sks in [2, 3]


class Kampus:
    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            print("Nama kampus tidak boleh mengandung angka.")
            self.valid = False
            return
        self.nama = nama
        self.alamat = alamat
        self.jumlah_mahasiswa = 0
        self.valid = True

    def tambah_mahasiswa(self):
        self.jumlah_mahasiswa += 1

    def tampilkan_info_kampus(self):
        print(f"\nInfo Kampus:")
        print(f"Nama Kampus: {self.nama}")
        print(f"Alamat Kampus: {self.alamat}")
        print(f"Total Mahasiswa: {self.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)


while True:
    nama_kampus = input("Masukkan nama kampus: ")
    alamat_kampus = input("Masukkan alamat kampus: ")
    kampus = Kampus(nama_kampus, alamat_kampus)
    if kampus.valid:
        break

matkul_list = [
    MataKuliah("MT001", "Pemrograman Berbasis Objek", 3),
    MataKuliah("MT002", "Pemrograman Berbasis Web", 3),
    MataKuliah("MT003", "Pengantar Basis Data", 3),
    MataKuliah("MT004", "Desain Manajemen Jaringan", 3),
    MataKuliah("MT005", "E-Business dan E-Commerce", 2),
    MataKuliah("MT006", "Analisa Proses Bisnis", 2),
]

matkul_list = [m for m in matkul_list if m.valid]

jumlah_mhs = input("Masukkan jumlah mahasiswa: ")
while not jumlah_mhs.isdigit():
    print("Masukkan angka.")
    jumlah_mhs = input("Masukkan jumlah mahasiswa: ")
jumlah_mhs = int(jumlah_mhs)

mahasiswa_list = []

for i in range(jumlah_mhs):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama: ")

    while True:
        nim = input("NIM (10 digit, mulai dengan '23'): ")
        if Mahasiswa.validasi_nim(nim):
            break
        print("NIM tidak valid. Harus 10 digit dan mulai dengan '23'.")

    prodi = input("Prodi: ")
    mhs = Mahasiswa(nama, nim, prodi, kampus)

    print("Pilih mata kuliah yang diambil (maks 4):")
    for j, matkul in enumerate(matkul_list, 1):
        print(f"{j}. {matkul.info_matkul()}")

    while True:
        jumlah_matkul = input("Berapa mata kuliah yang ingin diambil? (1-4): ")
        if jumlah_matkul.isdigit() and 1 <= int(jumlah_matkul) <= 4:
            jumlah_matkul = int(jumlah_matkul)
            break
        else:
            print("Jumlah mata kuliah harus antara 1-4.")

    for _ in range(jumlah_matkul):
        while True:
            pilihan = input("Pilih no mata kuliah: ")
            if pilihan.isdigit():
                pilihan = int(pilihan)
                if 1 <= pilihan <= len(matkul_list):
                    mhs.tambah_matkul(matkul_list[pilihan-1])
                    break
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Masukkan angka.")

    mahasiswa_list.append(mhs)

print("\n--- INFORMASI MAHASISWA ---")
for mhs in mahasiswa_list:
    mhs.tampilkan_biodata()

kampus.tampilkan_info_kampus()