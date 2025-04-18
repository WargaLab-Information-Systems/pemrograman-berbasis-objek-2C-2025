class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.mata_kuliah = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tmb_matkul(self, matkul):
        self.mata_kuliah.append(matkul)

    def biodata(self):
        print("Nama         : ", self.nama)
        print("NIM          : ", self.nim)
        print("Prodi        : ", self.prodi)
        print("Validasi NIM : ", Mahasiswa.validasi_nim(self.nim))
        print("Mata Kuliah  :")
        for i in self.mata_kuliah:
            print(f"- {i.nama} ({i.sks} SKS) --> {Matakuliah.validasi_sks(i.sks)}")

    @classmethod
    def total(cls):
        return f"Jumlah Mahasiswa adalah {cls.jumlah_mahasiswa} mahasiswa"

    @staticmethod
    def validasi_nim(nim):
        if nim.startswith("23") and len(nim) == 10:
            return "NIM lolos pengecekan validasi!"
        else:
            return "NIM tidak valid"


class Matakuliah:
    def __init__(self, kode_matkul, nama, sks):
        self.kode_matkul = kode_matkul
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        if sks == 2 or sks == 3:
            return "Jumlah SKS valid!"
        else:
            return "Jumlah SKS tidak valid!"


class Kampus:
    def __init__(self, nama_kampus, alamat_kampus):
        self.nama_kampus = nama_kampus
        self.alamat_kampus = alamat_kampus

    @staticmethod
    def validasi_kampus(nama_kampus):
        for i in nama_kampus:
            if i.isdigit():
                return "Nama Kampus tidak valid!"
        return "Nama Kampus lolos pengecekan validasi!"

    def tampilkan_kampus(self):
        print(f"Nama Kampus   : {self.nama_kampus}")
        print(f"Alamat Kampus : {self.alamat_kampus}")
        print(f"Validasi      : {Kampus.validasi_kampus(self.nama_kampus)}")



matkul1 = Matakuliah("AB1", "Desain Manajemen Jaringan", 2)
matkul2 = Matakuliah("AB2", "Pengantar Basis Data", 2)
matkul3 = Matakuliah("AB3", "Algoritma Pemrograman", 3)
matkul4 = Matakuliah("AB4", "Keterampilan Interpersonal", 3)
matkul5 = Matakuliah("AB5", "Pemrograman Berbasis Objek", 3)
matkul6 = Matakuliah("AB6", "Pemrograman Berbasis Web", 4)
matkul7 = Matakuliah("AB7", "Pancasila", 2)
matkul8 = Matakuliah("AB8", "Bahasa Inggris", 2)

mhs1 = Mahasiswa("Nur Cahyo", "2344110001", "Sistem Informasi")
mhs1.tmb_matkul(matkul1)
mhs1.tmb_matkul(matkul2)
mhs1.tmb_matkul(matkul3)
mhs1.tmb_matkul(matkul8)

mhs2 = Mahasiswa("Gerald", "2344110002", "Sistem Informasi")
mhs2.tmb_matkul(matkul3)
mhs2.tmb_matkul(matkul4)
mhs2.tmb_matkul(matkul7)
mhs2.tmb_matkul(matkul5)

mhs3 = Mahasiswa("Arif Brata", "2344110003", "Sistem Informasi")
mhs3.tmb_matkul(matkul1)
mhs3.tmb_matkul(matkul2)
mhs3.tmb_matkul(matkul8)
mhs3.tmb_matkul(matkul7)

mhs4 = Mahasiswa("Pras Teguh", "2344110004", "Sistem Informasi")
mhs4.tmb_matkul(matkul3)
mhs4.tmb_matkul(matkul2)
mhs4.tmb_matkul(matkul5)
mhs4.tmb_matkul(matkul6)

mhs5 = Mahasiswa("Arafah Rianti", "2344110005", "Sistem Informasi")
mhs5.tmb_matkul(matkul4)
mhs5.tmb_matkul(matkul5)
mhs5.tmb_matkul(matkul7)
mhs5.tmb_matkul(matkul8)

mhs6 = Mahasiswa("Gustiwiw", "234411006", "Sistem Informasi")
mhs6.tmb_matkul(matkul5)
mhs6.tmb_matkul(matkul2)
mhs6.tmb_matkul(matkul7)
mhs6.tmb_matkul(matkul8)

daftar_mahasiswa = [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]

print("\n=== Data Setiap Mahasiswa ===")
print()
for mhs in daftar_mahasiswa:
    mhs.biodata()
    print()

print(Mahasiswa.total())

kampus1 = Kampus("Universitas3 Trunojoyo Madura", "Madura")
print("\n=== Data Kampus ===")
kampus1.tampilkan_kampus()
