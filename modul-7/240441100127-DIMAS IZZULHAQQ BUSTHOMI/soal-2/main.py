from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def main():
    print("1. Sewa Mobil")
    print("2. Sewa Motor")
    print("3. Sewa Sepeda")
    print("4. Selesai")

    pilihan = int(input("Pilih Kendaraan: "))
    nama = input("Masukkan Nama: ")
    usia = int(input("Masukkan Usia: "))

    if pilihan == 1:
        kendaraan = Mobil()
    elif pilihan == 2:
        kendaraan = Motor()
    elif pilihan == 3:
        kendaraan = Sepeda()
    else:
        print("Pilihan kendaraan tidak tersedia.")
        return
    
    hasil = kendaraan.proses_booking(nama, usia)
    print(hasil)

main()