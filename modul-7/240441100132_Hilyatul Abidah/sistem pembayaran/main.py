from tunai import Tunai
from kartu_kredit import KartuKredit
from dompet_digital import DompetDigital

def input_jumlah_pembayaran():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah pembayaran (Rp): "))
            if jumlah > 0:
                return jumlah
            else:
                print("Jumlah harus lebih dari 0. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Harus berupa angka bulat.")

def pilih_metode_pembayaran():
    while True:
        print("\n=== Pilih Metode Pembayaran ===")
        print("1. Tunai")
        print("2. Kartu Kredit")
        print("3. Dompet Digital")
        pilihan = int(input("Masukkan pilihan (1/2/3): "))
        
        if pilihan == 1:
            return Tunai()
        elif pilihan == 2:
            return KartuKredit()
        elif pilihan == 3:
            return DompetDigital()
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

def main():
    while True:
        print("\n=== Sistem Pembayaran ===")
        jumlah = input_jumlah_pembayaran()
        metode = pilih_metode_pembayaran()
        total_bayar = metode.proses_pembayaran(jumlah)
        
        print(f"\nTotal yang harus dibayar: Rp{total_bayar}")

        ulang = input("\nIngin melakukan pembayaran lagi? (y/n): ").lower()
        if ulang != 'y':
            print("Terima kasih! Program selesai.")
            break

if __name__ == "__main__":
    main()
