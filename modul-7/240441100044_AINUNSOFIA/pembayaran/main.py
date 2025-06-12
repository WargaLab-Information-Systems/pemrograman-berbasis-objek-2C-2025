from tunai import Tunai
from kartu_kredit import KartuKredit
from ewallet import DompetDigital

def tampilkan_menu():
    print("\n--- Sistem Pembayaran ---")
    print("1. Tunai (diskon 5%)")
    print("2. Kartu Kredit (biaya admin Rp2500)")
    print("3. Dompet Digital (cashback 3%)")

def main():
    try:
        tampilkan_menu()
        pilihan = input("Pilih metode pembayaran (1/2/3): ")

        if pilihan == '1':
            metode = Tunai()
        elif pilihan == '2':
            metode = KartuKredit()
        elif pilihan == '3':
            metode = DompetDigital()
        else:
            print("Pilihan tidak valid.")
            return
        jumlah = float(input("Masukkan jumlah pembayaran (Rp): "))
        total = metode.proses_pembayaran(jumlah)

    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")

if __name__ == "__main__":
    main()
