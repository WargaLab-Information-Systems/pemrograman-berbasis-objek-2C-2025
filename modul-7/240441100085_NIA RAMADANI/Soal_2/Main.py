from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def main():
    print("\n==== Aplikasi Pemesanan Kendaraan ====\n")
    nama = input("Nama Anda: ")
    usia = int(input("Usia Anda: "))

    print("\nPilih kendaraan untuk dipesan:")
    print("1. Mobil")
    print("2. Motor")
    print("3. Sepeda")
    pilihan = input("Pilihan (1/2/3): ")

    kendaraan = None

    try:
        if pilihan == '1':
            kendaraan = Mobil(nama, usia)
        elif pilihan == '2':
            kendaraan = Motor(nama, usia)
        elif pilihan == '3':
            kendaraan = Sepeda(nama, usia)
        else:
            print("Pilihan tidak valid.")
            return

        kendaraan.proses_pemesanan()
        total = kendaraan.hitung_biaya() + kendaraan.hitung_asuransi()
        print(f"\nTotal yang harus dibayar: Rp{total:,}")

    except ValueError as e:
        print(f"\nGagal memesan: {e}")

if __name__ == "__main__":
    main()
