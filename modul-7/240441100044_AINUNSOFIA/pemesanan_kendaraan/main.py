from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def tampilkan_menu():
    print("\n--- Sistem Pemesanan Kendaraan ---")
    print("1. Mobil (Rp250.000 / hari + Asuransi Rp50.000) - Minimal usia 18 tahun")
    print("2. Motor (Rp100.000 / hari + Asuransi Rp20.000) - Minimal usia 17 tahun")
    print("3. Sepeda (Rp50.000 / hari + Asuransi Rp10.000) - Minimal usia 10 tahun")

def main():
    print("=== Selamat datang di Sistem Pemesanan Kendaraan ===")
    nama = input("Masukkan nama Anda: ")
    
    try:
        usia = int(input("Masukkan usia Anda: "))
        tampilkan_menu()
        pilihan = input("Pilih kendaraan (1/2/3): ")

        if pilihan == '1':
            kendaraan = Mobil()
        elif pilihan == '2':
            kendaraan = Motor()
        elif pilihan == '3':
            kendaraan = Sepeda()
        else:
            print("Pilihan tidak valid.")
            return

        # Validasi booking dulu sebelum tanya durasi
        if kendaraan.proses_booking(nama, usia):
            durasi = int(input("Masukkan durasi sewa (hari): "))
            biaya = kendaraan.hitung_biaya(durasi)
            asuransi = kendaraan.hitung_asuransi()
            total = biaya + asuransi
            print(f"\nTotal biaya sewa + asuransi: Rp{total:,}")
        else:
            print("Booking tidak dapat dilanjutkan karena usia tidak memenuhi.")
    
    except ValueError:
        print("Input tidak valid. Harus berupa angka.")

if __name__ == "__main__":
    main()