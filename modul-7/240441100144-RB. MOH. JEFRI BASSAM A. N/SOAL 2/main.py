from kendaraan.mobil import Mobil
from kendaraan.motor import Motor
from kendaraan.sepeda import Sepeda

while True:
    print("\n==== SISTEM PEMESANAN KENDARAAN UJEE ====")
    nama = input("Masukkan nama : ")

    print("---Pilih jenis kendaraan ---")
    print("1. Mobil")
    print("2. Motor")
    print("3. Sepeda")
    pilihan = int(input("Pilihan (1/2/3) : "))

    if pilihan == 1:
        kendaraan = Mobil()
    elif pilihan == 2:
        kendaraan = Motor()
    elif pilihan == 3:
        kendaraan = Sepeda()
    else:
        print("\n-- Pilihan tidak valid --")
        continue

    usia = int(input("Masukkan usia   : "))
    berhasil = kendaraan.proses_booking(nama, usia)

    if berhasil:
        biaya = kendaraan.hitung_biaya()
        asuransi = kendaraan.biaya_asuransi()
        total = biaya + asuransi
        
        print(f"\nBiaya sewa              : Rp{biaya}")
        print(f"Biaya asuransi          : Rp{asuransi}")
        print(f"Total yang harus dibayar: Rp{total}")
    else:
        print("\n-- Booking dibatalkan karena tidak memenuhi syarat --")

    ulang = input("\nMau ngulang? (y/n): ")
    if ulang != 'y':
        print("\n--Program selesai --")
        print()
        break
