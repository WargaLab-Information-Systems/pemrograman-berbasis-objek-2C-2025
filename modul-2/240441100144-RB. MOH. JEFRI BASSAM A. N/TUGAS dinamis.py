class mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim 
        self.prodi = prodi 
        self.daftar_matkul = []
        mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul_anyar):
        self.daftar_matkul.append(matkul_anyar)

    def info_bio_matkul(self):
        print(f"nama          : {self.nama}")
        print(f"NIM           : {self.nim}")
        print(f"Program Studi : {self.prodi}")
        print(f"Mata Kuliah yang diambil :")
        if len(self.daftar_matkul) == 0:
            print("--- belum ada data matkul yang  diambil ---\n")
        else:
            for matakul in self.daftar_matkul:
                print(f"- {matakul.nama_matkul} | {matakul.sks} SKS | {matakul.kode_matkul}")
        print()
        
    @classmethod
    def info_jmlh_mhs(cls):
        return f"Jumlah mahasiswa yang terdata : {cls.jumlah_mahasiswa}"
    
    @staticmethod
    def validasi_nim(nim):
        return nim[0:2] == "23" and len(nim) == 10

class matakuliah:
    def __init__(self, kode_matkul, nama_matkul, sks):
        self.kode_matkul = kode_matkul
        self.nama_matkul = nama_matkul
        self.sks = sks
      
    @staticmethod
    def validasi_sks(sks):
        return sks == "2" or sks == "3"
        
class univ:
    def __init__(self, nama_univ, alamat_univ):
        self.nama_univ = nama_univ
        self.alamat_univ = alamat_univ

    def info(self):
        print("---------INFO KAMPUS---------")
        print(f"Nama Universitas   : {self.nama_univ}")
        print(f"Alamat Universitas : {self.alamat_univ}")
        if univ.valid_nama(self.nama_univ):
             print("Validasi Nama Kampus : VALID")
        else:
            print("Validasi Nama Kampus : TIDAK VALID")

    @staticmethod
    def valid_nama(nama_univ):
        for nm_univ in nama_univ:
            if nm_univ.isdigit():
                return False
        return True

    @classmethod
    def info_univ(cls):
        print(f"\ntotal mahasiswa dikampus : {mahasiswa.jumlah_mahasiswa}\n")

# kampus
print("-----DATA UNIVERSITAS-----")
while True:
    nama_univ = input("masukkan nama Universitas : ")
    if univ.valid_nama(nama_univ):
        break
    else:
        print(f"---nama kampus tidak valid! mengandung angka---") 

alamat_univ = input("masukkan alamat Universitas : ")  
kampus = univ(nama_univ, alamat_univ)

# matakuliah
daftar_matkul = []

print("\n-----DATA MATAKULIAH-----")
while True:
    jumlah_matkul = int(input("berapa mata kuliah yang ingin dimasukkan (min 8) ? "))
    if jumlah_matkul >= 2:
        break
    elif jumlah_matkul < 2:
        print("\n---jumlah data matakuliah minimal 8---\n")

i = 0
while i < jumlah_matkul:
    print(f"-----Data mata kuliah ke-{i+1}-----")
    kode_matkul = input("kode mata kuliah : ")
    nama_matkul = input("nama mata kuliah : ")

    while True:
        sks = input("sks matkul (2/3) : ")
        print()
        if matakuliah.validasi_sks(sks):
            break
        else:
            print("---SKS tidak valid, silakan masukkan ulang---\n")
    matakul = matakuliah(kode_matkul,nama_matkul, sks)
    daftar_matkul.append(matakul)
    i += 1

# mahasiswa
mhs_list = []

print("-----DATA MAHASISWA-----")
while True:
    jmlh_mhs = int(input("berapa mahasiswa yang ingin dimasukkan ? "))
    if jmlh_mhs >= 1:
        break
    elif jmlh_mhs < 1:
        print("---jumlah data mahasiswa minimal 6---")

i = 0
while i < jmlh_mhs:
    print(f"-----Data mahasiswa ke-{i+1}-----")
    nama = input("nama          : ")
    nim = input("NIM           : ")
    prodi = input("Program Studi : ")

    if mahasiswa.validasi_nim(nim):
        m = mahasiswa(nama, nim, prodi)
        mhs_list.append(m)
        i += 1
        
        tambah = input("apakah anda ingin nambah mata kuliah untuk mahasiswa ini ? (y/n)")
        print()
        while tambah == "y":
            j = 0
            while j < len(daftar_matkul):
                print(f"{j+1}. {daftar_matkul[j].nama_matkul}")
                j += 1
            
            pilih = int(input("pilih nomor data mata kuliah : ")) - 1
            if 0 <= pilih < len(daftar_matkul):
                m.tambah_matkul(daftar_matkul[pilih])
                tambah = input("tambah lagi ? (y/n)")
                print()
            else:
                print("\n---tidak ada pilihan tersebut---\n")
                tambah = input("coba lagi ? (y/n)")
    else:
        print(f"\n---NIM {nim} tidak valid! harus dimulai dengan 23 dan 10 digit---\n")
        
# tampilkan semua data
print("\n--------BIODATA MAHASISWA --------")
i = 0
while i < len(mhs_list):
    print(f"-----Biodata mahasiswa {i+1}-----")
    mhs_list[i].info_bio_matkul()
    i += 1
print(mahasiswa.info_jmlh_mhs())
 
univ.info_univ()
kampus.info()