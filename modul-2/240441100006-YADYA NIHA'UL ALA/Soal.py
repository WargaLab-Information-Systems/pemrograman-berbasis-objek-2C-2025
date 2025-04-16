class Mahasiswa:
    jumlah_mhs = 0

    def __init__(self, nama, nim, prodi):
        try:
            if not Mahasiswa.cek_nim(nim):
                raise ValueError("NIM harus dimulai dengan '23' dan terdiri dari 10 digit angka")
        except Exception as e:
            print(f"[Error] Gagal membuat Mahasiswa: {e}")
            raise

        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_list = []

        Mahasiswa.jumlah_mhs += 1

    @classmethod
    def total_mhs(cls):
        return cls.jumlah_mhs

    @staticmethod
    def cek_nim(nim):
        if not isinstance(nim, str):
            raise TypeError("NIM harus berupa string")
        if not nim.startswith("23"):
            return False
        if len(nim) != 10 or not nim.isdigit():
            return False
        return True

    def tambah_matkul(self, matkul):
        try:
            self.matkul_list.append(matkul)
        except Exception as e:
            print(f"[Error] Gagal menambahkan mata kuliah: {e}")

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Program Studi: {self.prodi}")
        print("Mata Kuliah yang diambil:")
        for matkul in self.matkul_list:
            print(f"- {matkul.nama} ({matkul.sks} SKS)")

class MataKuliah:
    def __init__(self, kode, nama, sks):
        try:
            if not MataKuliah.cek_sks(sks):
                raise ValueError("SKS tidak sesuai, pilih antara 2 atau 3")
        except Exception as e:
            print(f"[Error] Gagal membuat Mata Kuliah: {e}")
            raise

        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def cek_sks(sks):
        return sks in [2, 3]

class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        try:
            if not Kampus.validasi_nama(nama):
                raise ValueError("Nama kampus tidak boleh mengandung angka")
        except Exception as e:
            print(f"[Error] Gagal membuat Kampus: {e}")
            raise

        self.nama = nama
        self.alamat = alamat

    @staticmethod
    def validasi_nama(nama):
        return not any(char.isdigit() for char in nama)

    @classmethod
    def kampus_info(cls, kampus_obj):
        print(f"Nama Kampus: {kampus_obj.nama}")
        print(f"Alamat: {kampus_obj.alamat}")
        print(f"Total Mahasiswa: {Mahasiswa.total_mhs()}")

# --- MATA KULIAH ---
mk_list = []
try:
    mk_list.extend([
        MataKuliah("MK01", "PBO", 3),
        MataKuliah("MK02", "PBW", 3),
        MataKuliah("MK03", "APB", 2),
        MataKuliah("MK04", "PBD", 2),
        MataKuliah("MK05", "DMJ", 2),
        MataKuliah("MK06", "English", 2),
        MataKuliah("MK07", "PAI", 2),
        MataKuliah("MK08", "E-Business", 2),
        MataKuliah("MK09", "Mandarin", 2),
        MataKuliah("MK10", "Matematika", 2),
        MataKuliah("MK11", "Bahasa Indonesia", 2)
    ])
except Exception:
    pass

# --- MAHASISWA ---
daftar_mhs = []
try:
    daftar_mhs.extend([
        Mahasiswa("Yadya Niha'ul Ala", "2304411006", "SI"),
        Mahasiswa("Cayden Arseus Valentine", "2304411106", "SI"),
        Mahasiswa("Lucius Ainsworth Dragunov", "2304011002", "Hukum"),
        Mahasiswa("Asher Alterga Von de Charles", "2304411016", "SI"),
        Mahasiswa("Li Zayne", "2300411006", "Kedokteran Forensik dan Medikolegal"),
        Mahasiswa("Velipe Elerise de Blair", "2301411012", "SI")
    ])
except Exception:
    pass

# --- KAMPUS ---
kampus1 = None
try:
    kampus1 = Kampus("Universitas Trunojoyo Madura", "Jl. Raya Telang, Perumahan Telang Inda, Telang, Kec. Kamal, Kabupaten Bangkalan, Jawa Timur 69162")
except Exception:
    pass

# --- DAFTAR PENGAMBILAN MATA KULIAH ---
try:
    daftar_mhs[0].tambah_matkul(mk_list[0])
    daftar_mhs[0].tambah_matkul(mk_list[1])
    daftar_mhs[0].tambah_matkul(mk_list[2])
    daftar_mhs[0].tambah_matkul(mk_list[4])
    daftar_mhs[0].tambah_matkul(mk_list[5])
    daftar_mhs[0].tambah_matkul(mk_list[7])

    daftar_mhs[1].tambah_matkul(mk_list[0])
    daftar_mhs[1].tambah_matkul(mk_list[1])
    daftar_mhs[1].tambah_matkul(mk_list[3])
    daftar_mhs[1].tambah_matkul(mk_list[6])

    daftar_mhs[2].tambah_matkul(mk_list[5])
    daftar_mhs[2].tambah_matkul(mk_list[6])
    daftar_mhs[2].tambah_matkul(mk_list[9])
    daftar_mhs[2].tambah_matkul(mk_list[10])

    daftar_mhs[3].tambah_matkul(mk_list[0])
    daftar_mhs[3].tambah_matkul(mk_list[1])
    daftar_mhs[3].tambah_matkul(mk_list[3])
    daftar_mhs[3].tambah_matkul(mk_list[2])
    daftar_mhs[3].tambah_matkul(mk_list[7])

    daftar_mhs[4].tambah_matkul(mk_list[5])
    daftar_mhs[4].tambah_matkul(mk_list[8])
    daftar_mhs[4].tambah_matkul(mk_list[9])
    daftar_mhs[4].tambah_matkul(mk_list[10])

    daftar_mhs[5].tambah_matkul(mk_list[0])
    daftar_mhs[5].tambah_matkul(mk_list[1])
    daftar_mhs[5].tambah_matkul(mk_list[2])
    daftar_mhs[5].tambah_matkul(mk_list[3])
    daftar_mhs[5].tambah_matkul(mk_list[5])
except Exception:
    pass

# --- DAFTAR MAHASISWA & MATA KULIAH YANG DIAMBIL ---
print("== Daftar Mahasiswa dan Mata Kuliah yang Diambil ==")
for mhs in daftar_mhs:
    try:
        mhs.tampilkan_biodata()
        print("------------------------")
    except Exception as e:
        print(f"[Error] Gagal menampilkan biodata mahasiswa: {e}")

# --- DAFTAR KAMPUS ---
if kampus1:
    print("\n== Daftar Kampus ==")
    try:
        Kampus.kampus_info(kampus1)
        print("Validasi Nama Kampus:", Kampus.validasi_nama(kampus1.nama))
    except Exception as e:
        print(f"[Error] Gagal menampilkan informasi kampus: {e}")
