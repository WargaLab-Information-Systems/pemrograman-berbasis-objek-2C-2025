from tunai import Tunai
from kartuKredit import KartuKredit
from ewallet import EWallet

while True:
    print("\n==== SISTEM PEMBAYARAN UJEE ====")
    jumlah = float(input("Masukkan jumlah pembayaran kamu : "))
    
    print("--- Pilih metode pembayaran ---")
    print("1. Tunai")
    print("2. Kartu Kredit")
    print("3. E-Wallet")
    pilihan = int(input("Masukkan pilihan kamu(1/2/3) : "))

    if pilihan == 1:
        metode = Tunai()
    elif pilihan == 2:
        metode = KartuKredit()
    elif pilihan == 3:
        metode = EWallet()
    else:
        print("\n-- Pilihan tidak valid --")
        continue

    total_bayar = metode.proses_pembayaran(jumlah)
    print(f"Total yang harus dibayar sebesar : Rp{total_bayar}")

    ulang = input("\nMau ngulang? (y/n): ")
    if ulang != 'y':
        print("\n--Program selesai --")
        print()
        break
