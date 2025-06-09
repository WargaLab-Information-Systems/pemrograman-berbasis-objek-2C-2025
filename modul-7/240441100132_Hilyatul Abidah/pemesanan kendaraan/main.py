from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def pilih_kendaraan():
    while True:
        print("\n=== Pilih Kendaraan ===")
        print("1. Mobil")
        print("2. Motor")
        print("3. Sepeda")
        pilihan = int(input("Masukkan pilihan (1/2/3): "))

        if pilihan == 1:
            return Mobil()
        elif pilihan == 2:
            return Motor()
        elif pilihan == 3:
            return Sepeda()
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

def input_usia():
    while True:
        try:
            usia = int(input("Masukkan usia Anda: "))
            if usia > 0:
                return usia
            else:
                print("Usia harus lebih dari 0.")
        except ValueError:
            print("Masukkan angka yang valid.")

def main():
    while True:
        kendaraan = pilih_kendaraan()
        usia = input_usia()

        if kendaraan.validasi_usia(usia):
            kendaraan.proses_booking()
            biaya = kendaraan.hitung_biaya()
            kendaraan.info_asuransi()
            print(f"Total biaya booking: Rp{biaya}/hari")
        else:
            print("Maaf, usia Anda tidak memenuhi syarat untuk kendaraan ini.")

        ulang = input("\nIngin melakukan booking lagi? (y/n): ")
        if ulang != 'y':
            print("Terima kasih telah menggunakan sistem pemesanan!")
            break

if __name__ == "__main__":
    main()