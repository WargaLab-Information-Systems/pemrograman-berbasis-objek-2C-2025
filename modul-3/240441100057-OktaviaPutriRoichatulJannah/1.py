class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : Rp {self.gaji}")
        print(f"Departemen : {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print("  <=== Karyawan Tetap ===>")
        print()
        super().info()
        print(f"Tunjangan  : Rp {self.tunjangan}")
        print()

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print("  <=== Karyawan Harian ===>")
        print()
        super().info()
        print(f"Jam Kerja  : {self.jam_kerja} jam per hari")
        print()


class ManajemenKaryawan:
    daftar_karyawan = [] 

    @classmethod
    def tambah_karyawan(cls, krywn):
        cls.daftar_karyawan.append(krywn)

    @classmethod
    def tampilkan_semua_karyawan(cls):
        print("*" * 35)
        print("      Daftar Semua Karyawan")
        print("*" * 35)
        print()
        for i in cls.daftar_karyawan:
            i.info()


krywn1 = KaryawanTetap("Upin",1200000,"HRD",600000)
krywn2 = KaryawanTetap("Ipin",1400000,"Finance",800000)
krywn3 = KaryawanTetap("Ros",2100000,"IT",1050000)
krywn4 = KaryawanHarian("Mei-mei",750000,"Customer Service",6)
krywn5 = KaryawanHarian("Mail",975000,"Sales",8)
krywn6 = KaryawanHarian("Susanti",690000,"Administrasi",6)

ManajemenKaryawan.tambah_karyawan(krywn1)
ManajemenKaryawan.tambah_karyawan(krywn2)
ManajemenKaryawan.tambah_karyawan(krywn3)
ManajemenKaryawan.tambah_karyawan(krywn4)
ManajemenKaryawan.tambah_karyawan(krywn5)
ManajemenKaryawan.tambah_karyawan(krywn6)

ManajemenKaryawan.tampilkan_semua_karyawan()
