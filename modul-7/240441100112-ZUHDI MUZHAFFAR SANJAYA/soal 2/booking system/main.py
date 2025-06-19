from vehicles.mobil import Mobil
from vehicles.motor import Motor
from vehicles.sepeda import Sepeda
from user import User

def main():
    nama = input("Masukkan nama Anda: ")
    usia = int(input("Masukkan usia Anda: "))
    user = User(nama, usia)

    while True:
        print("\nPilih kendaraan yang ingin dipesan:")
        print("1. Mobil")
        print("2. Motor")
        print("3. Sepeda")

        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == "1":
            kendaraan = Mobil("Toyota", 500_000)
        elif pilihan == "2":
            kendaraan = Motor("Yamaha", 150_000)
        elif pilihan == "3":
            kendaraan = Sepeda("Polygon", 50_000)
        else:
            print("Pilihan tidak valid.")
            continue

        try:
            print(kendaraan.proses_booking(user))
            print(f"Biaya sewa: Rp {kendaraan.hitung_biaya():,.0f}")
            print(f"Asuransi: Rp {kendaraan.asuransi():,.0f}")
            print(f"Total bayar: Rp {kendaraan.hitung_biaya() + kendaraan.asuransi():,.0f}")
        except ValueError as e:
            print(f"Gagal booking: {e}")

        ulang = input("\nApakah Anda ingin booking kendaraan lain? (y/n): ").lower()
        if ulang != "y":
            print("Terima kasih telah menggunakan sistem booking kendaraan.")
            break

if __name__ == "__main__":
    main()