from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def main ():
    while True:
        print("Selamat datang")
        print("1. Mobil")
        print("2. Motor")
        print("3. Sepeda")
        pilihan = int(input("Silahkan pilih: "))

        if pilihan == 1:
            nama = input("Masukkan nama: ")
            umur = int(input("Masukkan Umur: "))
            kendaraan = Mobil()
        elif pilihan == 2:
            nama = input("Masukkan nama: ")
            umur = int(input("Masukkan Umur: "))
            kendaraan = Motor()
        elif pilihan == 3:
            nama = input("Masukkan nama: ")
            umur = int(input("Masukkan Umur: "))
            kendaraan = Sepeda()
        else:
            print("Tidak valid")
            exit()
        
        if kendaraan.proses_booking(nama, umur):
            biaya = kendaraan.hitung_biaya()
            asuransi = kendaraan.informasi_asuransi()
            print(f"Total biaya Rp {biaya} + Asuransi: Rp {asuransi}. Total Akhir Rp {biaya+asuransi}")

        n = input("Apakah ingin booking lagi (y/n): ")
        if n != "y":
            print("Terimakasih")
            break
main()