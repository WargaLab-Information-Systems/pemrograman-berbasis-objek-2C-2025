class MataKuliah:
    def __init__(self, kode_mk, nama_mk, jumlah_sks):
        self.kode_mk = kode_mk
        self.nama_mk = nama_mk
        self.jumlah_sks = jumlah_sks
    @staticmethod
    def validasi_sks(sks):
        return sks == 2 or sks == 3

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
        print("\nBIODATA")
        print("Nama:", self.nama)
        print("NIM :", self.nim)
        print("Prodi:", self.prodi)
        print("Mata Kuliah yang Diambil:")
        for mk in self.daftar_matkul:
            print(f"-{mk.kode_mk} -{mk.nama_mk} -{mk.jumlah_sks} SKS")
    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa
    @staticmethod
    def validasi_nim(nim):
        nim = nim  
        return nim[:2] == "23" and len(nim) == 10 and nim.isdigit()

class Kampus:
    def __init__(self, nama_kampus, alamat_kampus):
        self.nama_kampus = nama_kampus
        self.alamat_kampus = alamat_kampus
    @classmethod
    def tampilkan_info(cls, kampus):
        print("\nInformasi Kampus:")
        print("Nama Kampus:", kampus.nama_kampus)
        print("Alamat:", kampus.alamat_kampus)
        print("Total Mahasiswa:", Mahasiswa.total_mahasiswa())
    @staticmethod
    def validasi_nama(nama):
        for i in nama:
            if i.isdigit():
                return False
        return True

while True:
    nama_kampus = input("Masukkan nama kampus: ")
    if not Kampus.validasi_nama(nama_kampus):
        print("Nama kampus tidak boleh mengandung angka!")
        continue
    alamat_kampus = input("Masukkan alamat kampus: ")
    kampus1 = Kampus(nama_kampus, alamat_kampus)
    break

list_matkul = []
jawab_mk = input("\nApakah ingin menginput data mata kuliah? (y/n): ").lower()
if jawab_mk == "y":
    while True:
        kode = input("Kode Mata Kuliah: ")
        nama = input("Nama Mata Kuliah: ")
        sks_input = input("Jumlah SKS (2 atau 3): ")
        if not sks_input.isdigit():
            print("SKS harus berupa angka!")
            continue
        sks = int(sks_input)
        if not MataKuliah.validasi_sks(sks):
            print("SKS hanya boleh 2 atau 3!")
            continue
        mk = MataKuliah(kode, nama, sks)
        list_matkul.append(mk)
        if len(list_matkul) >= 8:
            lanjut = input("Tambah mata kuliah lagi? (y/n): ").lower()
            if lanjut != "y":
                break
        else:
            print(f"Jumlah mata kuliah saat ini: {len(list_matkul)} (Minimal 8)\n")
else:
    print("Lewat bagian input mata kuliah.")

list_mahasiswa = []
jawab_mhs = input("\nApakah ingin menginput data mahasiswa? (y/n): ").lower()
if jawab_mhs == "y":
    while True:
        nama = input("Nama Mahasiswa:")
        nim = input("NIM Mahasiswa:")
        prodi = input("Prodi Mahasiswa:")
        if not Mahasiswa.validasi_nim(nim):
            print("NIM tidak valid! Harus mulai dengan '23', panjang 10 digit angka.")
            continue
        mhs = Mahasiswa(nama, nim, prodi)
        if len(list_matkul) < 4:
            print("Tidak cukup mata kuliah untuk dipilih.")
        else:
            print("Pilih 4 mata kuliah untuk mahasiswa ini:")
            for i in range(len(list_matkul)):
                print(f"{i+1}. {list_matkul[i].nama_mk} ({list_matkul[i].kode_mk})")
            jumlah_dipilih = 0
            while jumlah_dipilih < 4:
                pilih = input(f"Pilih matkul ke-{jumlah_dipilih+1} (nomor): ")
                if not pilih.isdigit():
                    print("Masukkan angka!")
                    continue
                jumlah_matkul = int(pilih) - 1
                if 0 <= jumlah_matkul < len(list_matkul):
                    mhs.tambah_matkul(list_matkul[jumlah_matkul])
                    jumlah_dipilih += 1
                else:
                    print("Nomor tidak tersedia.")
        list_mahasiswa.append(mhs)
        if len(list_mahasiswa) >= 6:
            lanjut = input("Tambah mahasiswa lagi? (y/n): ").lower()
            if lanjut != "y":
                break
        else:
            print(f"Jumlah mahasiswa saat ini: {len(list_mahasiswa)} (Minimal 6)\n")
else:
    print("Lewat bagian input mahasiswa.")

print()
print("DATA MAHASISWA DAN MATA KULIAH")
for mhs in list_mahasiswa:
    mhs.tampilkan_biodata()

Kampus.tampilkan_info(kampus1)
if Kampus.validasi_nama(kampus1.nama_kampus):
    print("Validasi Nama Kampus: VALID")
else:
    print("Validasi Nama Kampus: TIDAK VALID")
