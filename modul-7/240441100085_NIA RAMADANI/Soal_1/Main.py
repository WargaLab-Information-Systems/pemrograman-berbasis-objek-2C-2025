from Tunai import Tunai
from Kartu_Kredit import KartuKredit
from Dompet_Digital import DompetDigital

def main():
    print("\n========== SIMULASI PEMBAYARAN ==========")
    jumlah = float(input("Masukkan total belanja Anda (Rp): "))
    saldo = float(input("Masukkan saldo Anda saat ini (Rp): "))

    print("\nPilih metode pembayaran:")
    print("1. Tunai (Diskon 5%)")
    print("2. Kartu Kredit (Biaya 3%)")
    print("3. Dompet Digital (Cashback 2%)")
    pilihan = input("Pilihan Anda (1/2/3): ")

    if pilihan == '1':
        metode = Tunai(jumlah, saldo)
    elif pilihan == '2':
        metode = KartuKredit(jumlah, saldo)
    elif pilihan == '3':
        metode = DompetDigital(jumlah, saldo)
    else:
        print("\n Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
        return

    metode.bayar()  

if __name__ == "__main__":
    main()
