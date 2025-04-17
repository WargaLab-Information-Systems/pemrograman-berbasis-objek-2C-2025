class Mahasiswa:
    jumlah_mahasiswa = 0
    def __init__(self,nama,nim,prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matakuliah = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matakuliah(self, matakuliah):
        if matakuliah not in self.matakuliah:
            self.matakuliah.append(matakuliah)
        else:
            print("Mata kuliah telah diambil")
    def biodata(self):
        print(f"Nama saya:{self.nama}")
        print(f"NIM:{self.nim}")
        print(f"Prodi:{self.prodi}")
        for matkul in self.matakuliah:
            print(f"Matkul:{matkul.nama},Kode:{matkul.kode},sks:{matkul.sks}")
    @classmethod
    def jumlah(cls):
        return cls.jumlah_mahasiswa 
    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10
            
class Matakuliah:
    def __init__(self,kode,nama,sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def info(self):
        return f"kode:{self.kode}, nama:{self.nama}, sks:{self.sks}"
    @staticmethod
    def validasi_sks(sks):
        return sks == 2 or sks == 3

class Kampus:
    jumlah_mahasiswa = 0 
    def __init__(self, nama_kampus, alamat):
        self.nama_kampus = nama_kampus
        self.alamat = alamat
    @classmethod
    def jumlah(cls):
        return f"Jumlah Mahasiswa: {cls.jumlah_mahasiswa}"
    @staticmethod
    def validasi_angka(nama_kampus):
        if nama_kampus.isalpha:
            return nama_kampus
    def info(self):
        return f"Nama Kampus: {self.nama_kampus}, Alamat: {self.alamat}"
    def tambah_mahasiswa(self):
        Kampus.jumlah_mahasiswa += 1

Nama_kampus = input("Masukkan Nama Kampus: ")
Alamat_kampus = input("Alamat Kampus: ")
kampus = Kampus(Nama_kampus, Alamat_kampus)

matkul_list = []
print("\nMasukkan 8 Mata Kuliah:")
i = 1
while i <= 2:
    print(f"\n Mata Kuliah ke-{i}")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks_input = input("SKS (2 atau 3): ")
    if sks_input.isdigit():
        sks = int(sks_input)
        if Matakuliah.validasi_sks(sks):
            matkul_list.append(Matakuliah(kode, nama, sks))
            i += 1
        else:
            print("SKS harus 2 atau 3.")
    else:
        print("Masukkan angka")

mhs_list = []
print("\nMasukkan 1 Mahasiswa:")
a = 1
while a <= 1:
    print(f"\nMahasiswa ke-{a}")
    nama = input("Nama: ")
    while True:
        nim_input = input("NIM: ")
        if nim_input.isdigit():
            if Mahasiswa.validasi_nim(nim_input):  
                nim = nim_input
                break
            else:
                print("Masukkan NIM dengan awalan 23 dan 10 digit")
        else:
            print("Masukkan NIM berupa angka")

    prodi = input("Prodi: ")
    mhs = Mahasiswa(nama, nim_input, prodi)

    print("Pilih 4 mata kuliah dari daftar:")
    for j in range(len(matkul_list)):
        mk = matkul_list[j]
        print(f"{j+1}. {mk.nama} ({mk.kode}) - {mk.sks} SKS")

    pilih = 1
    while pilih <= 2:
        pilihan = input(f"Matkul ke-{pilih} (1-{len(matkul_list)}): ")
        if pilihan:
            idx = int(pilihan)
            if 1 <= idx <= len(matkul_list):
                mhs.tambah_matakuliah(matkul_list[idx - 1])
                pilih += 1
            else:
                print("Nomor tidak sesuai")
        else:
            print("Masukkan angka")
    mhs_list.append(mhs)
    a += 1

print("\n DATA MAHASISWA ")
for mhs in mhs_list:
    mhs.biodata()

print("\n DATA KAMPUS ")
kampus.info()
if Kampus.validasi_angka(Nama_kampus):
    print("Nama kampus valid")
else:
    print("Nama kampus tidak valid")