from abc import ABC, abstractmethod

class Karyawan(ABC):
    @abstractmethod
    def hitung_gaji(self):
        pass

class KaryawanKontrak(Karyawan):
    def hitung_gaji(self): 
        nama = input("masukkan nama karyawan: ")
        departemen = input("masukkan departemen karyawan: ")
        jam_kerja = int(input("masukkan jam kerja karyawan: "))
        gaji_perjam = int(input("masukkan gaji harian karyawan: "))
        gaji_harian = jam_kerja*gaji_perjam
        return(f"- {nama} dari departemen {departemen} bekerja {jam_kerja} jam dengan upah {gaji_perjam}/jam. Total gaji: {gaji_harian}")

class KaryawanTetap(Karyawan):
    def hitung_gaji(self):
        nama = input("masukkan nama karyawan: ")
        departemen = input("masukkan departemen karyawan: ")
        tunjangan = int(input("masukkan tunjangan karyawan: "))
        gaji = int(input("masukkan gaji karyawan tetap: "))
        total_gaji = gaji + (tunjangan * 50000) 
        return(f"- {nama} Karyawan tetap dari departemen {departemen} mempunyai tunjangan {tunjangan} dan gaji tetap {gaji} total gaji yang didapat adalah {total_gaji}")

datakaryawan = []

def jawaban(hasil):
    hasil_gaji = hasil.hitung_gaji()
    print(hasil_gaji)
    datakaryawan.append(hasil_gaji)

while True:
    print("\nSELAMAT DATANG")
    print ("1. Karyawan Tetap")
    print ("2. Karyawan Kontrak")
    print ("3. tampilkan info")
    print ("4. keluar")

    jawab = int(input("Masukkan nomor yang tertera: "))
    if jawab == 1:
        karyawantetap = KaryawanTetap()
        jawaban(karyawantetap)
    elif jawab == 2:
        karyawankontrak = KaryawanKontrak()
        jawaban(karyawankontrak)
    elif jawab == 3:
        if datakaryawan:
            print("\nData yang sudah dihitung:")
            for data in (datakaryawan) :
                print(data)
        else:
            print("Belum ada data yang disimpan.")
    elif jawab == 4:
        print("Terima kasih telah menggunakan layanan hitung menghitung.")
        break
    else:
        print("nomor yang anda inputkan tidak valid")
    