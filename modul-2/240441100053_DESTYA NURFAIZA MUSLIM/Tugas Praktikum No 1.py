# 1. Mahasiswa
class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.daftar_matkul = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.daftar_matkul.append(matkul)

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah yang Diambil :")
        for idx, mk in enumerate(self.daftar_matkul, 1):
            print(f"  {idx}. {mk.nama_mata_kuliah} ({mk.kode_matkul}, {mk.jumlah_sks} SKS) -> Jumlah SKS valid")
        print()

    @classmethod
    def tampilkan_jumlah(cls):
        print(f"Jumlah Mahasiswa saat ini: {cls.jumlah_mahasiswa}")

    @staticmethod
    def cek_validasi_nim(nim):
        return nim[:2] == '23' and len(nim) == 10 and nim.isdigit()

# 2. Mata Kuliah
class Mata_kuliah:
    def __init__(self, kode_matkul, nama_mata_kuliah, jumlah_sks):
        self.kode_matkul = kode_matkul
        self.nama_mata_kuliah = nama_mata_kuliah
        self.jumlah_sks = jumlah_sks

    @staticmethod
    def cek_validasi_sks(sks):
        return sks in (2, 3)

# 3. Kampus
class Kampus:
    def __init__(self, nama_kampus, alamat_kampus):
        self.nama_kampus = nama_kampus
        self.alamat_kampus = alamat_kampus

    @staticmethod
    def cek_validasi_kampus(nama_kampus):
        return nama_kampus.replace(" ", "").isalpha()

    def tampilkan_info(self, total_mahasiswa):
        print(f"Nama Kampus: {self.nama_kampus}\nAlamat : {self.alamat_kampus}\nTotal Mahasiswa : {total_mahasiswa}")
        print(f"Nama kampus valid: {Kampus.cek_validasi_kampus(self.nama_kampus)} -> Nama Kampus Valid")


#  6 Mahasiswa
data_mhs = [
    ("Bambang", "23044110001", "Teknik Informatika"),
    ("Sutaji", "2344110002", "Sistem Informasi"),
    ("Sriyati", "2444110003", "Sistem Informasi"),
    ("Suhadi", "2344110004", "Teknik Infromatika"),
    ("Wiyoto", "2344110005", "Teknik Informatika"),
    ("Herman", "2344110006", "Sistem Informasi"),
]

# 8 Objek Mata Kuliah
matkul_list = []
data_matkul = [
    ("SI001", "Algoritma dan Pemrograman", 3),
    ("SI002", "Struktur Data", 3),
    ("SI003", "Pengantar Basis Data", 2),
    ("SI004", "Desain Manajemen Komputer", 3),
    ("SI005", "Sistem Operasi", 3),
    ("SI006", "Pemrograman Berbasis Web", 4),
    ("SI007", "Kecerdasan Buatan", 3),
    ("SI008", "Keamanan Siber", 2),
]

# cek sks
for kode, nama_matkul, sks in data_matkul:
    if Mata_kuliah.cek_validasi_sks(sks):
        mk = Mata_kuliah(kode, nama_matkul, sks)
        matkul_list.append(mk)
    else:
        print(f"- Jumlah SKS untuk {nama_matkul} tidak valid. Mata kuliah tidak dibuat.")


# Minimal 4 matkul
mahasiswa_list = []
data_matkul_terpilih = [
    [2, 1, 4, 3],
    [0, 1, 4, 5], 
    [1, 3, 5, 6, 4],  
    [1, 2, 3, 5, 6],  
    [1, 2, 4, 5, 6],  
    [0, 1, 4],  
]

# Membuat objek mahasiswa dan menambahkan mata kuliah yang dipilih
for i in range(len(data_mhs)):
    nama, nim, prodi = data_mhs[i]
    matkul_terpilih_mahasiswa = data_matkul_terpilih[i]
    
    # cek nim
    if Mahasiswa.cek_validasi_nim(nim):
        mhs = Mahasiswa(nama, nim, prodi)
        
        # cek minimal 4 matkul
        if len(matkul_terpilih_mahasiswa) < 4:
            print(f"- Mahasiswa {nama} harus mengambil minimal 4 mata kuliah.")
            continue 
        
        #Menambahkan mata kuliah yang sudah ditentukan
        for idx in matkul_terpilih_mahasiswa:
            if 0 <= idx < len(matkul_list):  
                mhs.tambah_matkul(matkul_list[idx])
            else:
                print(f"- Indeks {idx} untuk mata kuliah tidak valid. Mata kuliah gagal ditambahkan.")

        mahasiswa_list.append(mhs)
    else:
        print(f"- NIM {nim} tidak valid. Mahasiswa {nama} tidak dibuat.")

# 1 Kampus
kmps = Kampus ("Universitas Trunojoyo Madura", "Telang")

if Kampus.cek_validasi_kampus(kmps.nama_kampus):
    kampus_obj = Kampus(kmps.nama_kampus, kmps.alamat_kampus)
else:
    print("Nama kampus tidak valid.")


print("\n ========= DATA MAHASISWA =========")
for mhs in mahasiswa_list:
    mhs.tampilkan_biodata()

print("========= INFO KAMPUS =========\n")
kampus_obj.tampilkan_info(len(mahasiswa_list))
