class Mahasiswa:
    jumlah_mahasiswa = 0 

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, kode_mk, nama_matkul, sks):
        self.matkul.append({'kode': kode_mk, 'nama': nama_matkul, 'sks': sks})

    def tampilkan_biodata(self):
        print(f"\nNama : {self.nama}")
        print(f"NIM  : {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata kuliah:")
        total_sks = 0
        for mk in self.matkul:
            print(f"- {mk['kode']} {mk['nama']} ({mk['sks']} SKS)")
            total_sks += mk['sks']
        print(f"Total SKS: {total_sks}")

    @classmethod
    def total_mahasiswa(cls):
        print(f"\nTotal Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        # NIM harus terdiri dari 10 digit
        if len(nim) != 10:
            return False
        # Memeriksa apakah dua digit pertama adalah '2' dan '3'
        if nim[0] != '2' or nim[1] != '3':
            return False
        # Memeriksa apakah setiap karakter NIM adalah angka
        for char in nim:
            if char < '0' or char > '9':
                return False
        return True

class Kampus:
    def __init__(self, nama, alamat, daftar_matkul):
        self.nama = nama
        self.alamat = alamat
        self.daftar_mahasiswa = []
        self.daftar_matkul = daftar_matkul 

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_semua(self):
        print(f"\n== Daftar Mahasiswa di {self.nama} ==")
        print(f"Alamat: {self.alamat}")
        for mhs in self.daftar_mahasiswa:
            mhs.tampilkan_biodata()
        Mahasiswa.total_mahasiswa()

    def tampilkan_daftar_matkul(self):
        print("\nDaftar Mata Kuliah yang Tersedia:")
        for mk in self.daftar_matkul:
            print(f"- {mk['kode']} {mk['nama']} ({mk['sks']} SKS)")

# ====================== Input Data ======================
# Daftar Mata Kuliah yang Tersedia di Kampus
daftar_matkul = [
    {'kode': 'IF101', 'nama': 'Pemrograman', 'sks': 3},
    {'kode': 'IF102', 'nama': 'Struktur Data', 'sks': 2},
    {'kode': 'IF103', 'nama': 'Matematika Diskrit', 'sks': 3},
    {'kode': 'IF104', 'nama': 'Basis Data', 'sks': 2},
    {'kode': 'IF105', 'nama': 'Jaringan Komputer', 'sks': 3},
    {'kode': 'IF106', 'nama': 'Sistem Operasi', 'sks': 2}
]

nama_kampus = input("Masukkan nama kampus: ")
alamat_kampus = input("Masukkan alamat kampus: ")
kampus = Kampus(nama_kampus, alamat_kampus, daftar_matkul)

kampus.tampilkan_daftar_matkul()  # Menampilkan daftar mata kuliah yang tersedia

jumlah_mhs = int(input("Masukkan jumlah mahasiswa: "))
for i in range(jumlah_mhs):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama: ")

    while True:
        nim = input("NIM : ")
        if Mahasiswa.validasi_nim(nim):
            break
        else:
            print("NIM tidak valid! Harus 10 digit dan diawali '23'. Coba lagi.")

    prodi = input("Prodi: ")
    mhs = Mahasiswa(nama, nim, prodi)

    jml_matkul = int(input("Jumlah mata kuliah diambil (min 4): "))
    while jml_matkul < 4:
        print("Minimal 4 mata kuliah!")
        jml_matkul = int(input("Masukkan ulang jumlah mata kuliah: "))

    for j in range(jml_matkul):
        while True:
            kode_mk = input(f"  Masukkan Kode Mata Kuliah ke-{j+1}: ")
            # Memeriksa apakah kode mata kuliah ada di daftar yang tersedia
            matkul_tersedia = next((mk for mk in daftar_matkul if mk['kode'] == kode_mk), None)
            if matkul_tersedia:
                nama_mk = matkul_tersedia['nama']
                sks = matkul_tersedia['sks']
                break
            else:
                print("Kode mata kuliah tidak valid, coba lagi!")

        mhs.tambah_matkul(kode_mk, nama_mk, sks)

    kampus.tambah_mahasiswa(mhs)

# ====================== Output ======================
kampus.tampilkan_semua()

print("\n== Validasi NIM ==")
for mhs in kampus.daftar_mahasiswa:
    status = "Valid" if Mahasiswa.validasi_nim(mhs.nim) else "Tidak Valid"
    print(f"{mhs.nama} ({mhs.nim}): {status}")