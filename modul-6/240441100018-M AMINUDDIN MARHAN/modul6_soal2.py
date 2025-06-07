from abc import ABC, abstractmethod

class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanTetap(Karyawan):
    def hitung_gaji(self):
        return "Gaji karyawan tetap adalah Rp. 5.000.000 per bulan"
    
class KaryawanKontrak(Karyawan):
    def hitung_gaji(self):
        return "Gaji karyawan kontrak adalah Rp. 4.000.000 per bulan"

def cetak_gaji(karyawan):
    print(karyawan.hitung_gaji())

karyawan1 = KaryawanTetap()
karyawan2 = KaryawanKontrak()

cetak_gaji(karyawan1)
cetak_gaji(karyawan2)