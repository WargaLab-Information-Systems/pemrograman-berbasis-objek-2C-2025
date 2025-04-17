class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul = []
        self.valid = Mahasiswa.cek_valid(nim)

        if self.valid:
            Mahasiswa.jumlah_mahasiswa += 1
            Kampus.total_mahasiswa += 1
        else:
            self.invalid = f"NIM tidak valid : {nim}. Semua harus diawali dari 23."
            
    def tambah_matkul(self, matkul):
        self.matkul.append(matkul)

    def info(self):
        print("-----" * 10)
        print(f"{self.nama}, NIM: {self.nim} - Prodi {self.prodi}")
        print("Matkul diambil:")
        for mk in self.matkul:
            print(f" - {mk.nama} ({mk.sks} SKS)")

    @classmethod
    def total(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def cek_valid(nim):
        if int(nim[:2]) == 23 and len(nim) == 10:
            return nim
        else:
            return
        
class Matakuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode 
        self.nama = nama
        self.sks = sks
        self.valid = Matakuliah.cek_valid(sks)
        
    @staticmethod
    def cek_valid(sks):
        if sks in (2,3):
            return sks

class Kampus:
    total_mahasiswa = 0
    nama_kampus = ""

    def __init__(self, nama, alamat):
        Kampus.nama_kampus = nama
        self.alamat = alamat
    
        if Kampus.cek_valid(Kampus.nama_kampus):
            self.validasi = "Nama Kampus Valid."
        else:
            self.validasi = "Nama Kampus Tidak Valid."

    @classmethod
    def tampilkan(cls):
        print(f"Nama Kampus: {cls.nama_kampus}. Total Mahasiswa: {cls.total_mahasiswa}")

    @staticmethod
    def cek_valid(nama):
        return nama.replace(" ","").isalpha()

list_mahasiswa = []

list_matkul = [
    Matakuliah("MK01", "PBO", 3),
    Matakuliah("MK02", "Struktur Data", 3),
    Matakuliah("MK03", "Basis Data", 2),
    Matakuliah("MK04", "Kalkulus", 2),
    Matakuliah("MK05", "Jaringan", 3),
    Matakuliah("MK06", "Statistika", 2),
    Matakuliah("MK07", "OS", 3),
    Matakuliah("MK08", "Logika", 4)
]

while True:
    jumlah_input = input("Masukkan berapa mahasiswa yang ingin di input: ")
    print("-----" * 10)

    if jumlah_input.isdigit():
        jumlah_input = int(jumlah_input)

        for i in range(jumlah_input):
            print(f"Masukkan data Mahasiswa ke-{i+1}")
            nama = input("Masukkan Nama : ")
            while True:
                nim = input("Masukkan NIM : ")
                if Mahasiswa.cek_valid(nim):
                    prodi = input("Masukkan Prodi : ")

                    mahasiswa = Mahasiswa(nama, nim, prodi)
                    
                    print("-----" * 10)
                    print("DAFTAR MATKUL :")
                    print("-----" * 10)
                    i = 1
                    for mk in list_matkul:
                        print(f"No.{i} : {mk.kode} | {mk.nama} | {mk.sks}")
                        i += 1
                        
                    print("-----" * 10)
                    for i in range(4):
                        while True:
                            pilih_matkul = input(f"Pilih Matakuliah {i+1}: ")
                            pilih_matkul = int(pilih_matkul)
                            mk = list_matkul[pilih_matkul- 1]

                            if Matakuliah.cek_valid(mk.sks):
                                mahasiswa.tambah_matkul(mk)
                                break
                            else:
                                print(f"Matakuliah {mk.nama} tidak valid. karena jumlah SKS {mk.sks} tidak diperbolehkan.")

                    list_mahasiswa.append(mahasiswa)
                    break

                else:
                    print("NIM harus dimulai dari 23 dan total digit 10.")

        break

    else:
        print("Input harus berupa angka.")

print("-----" * 10)
print(f"Total Mahasiswa yang terdaftar : {Mahasiswa.total()}")

for mhs in list_mahasiswa:
    if mhs.valid:
        mhs.info()
    else:
        print("-----" * 10)
        print(mhs.invalid)

data_kampus = []

while True:
    print("-----" * 10)
    nama = input("Masukkan nama kampus: ")
    if Kampus.cek_valid(nama):
        alamat = input("Masukkan alamat : ")

        kampus = Kampus(nama, alamat)
        data_kampus.append(kampus)
        break
    else:
        print("-----" * 10)
        print("Nama kampus tidak valid.")

print("-----" * 10)
kampus.tampilkan()
print("-----" * 10)
print(kampus.validasi)
print("-----" * 10)