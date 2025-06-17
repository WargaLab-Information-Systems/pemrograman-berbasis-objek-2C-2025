from metode_tunai import Tunai
from metode_kartu import KartuKredit
from metode_dompet import DompetDigital

def tampilkan_menu():
    print("\n=== Sistem Pembayaran ===")
    print("1. Tunai (Diskon 5%)")
    print("2. Kartu Kredit (Biaya Admin Rp3.000)")
    print("3. Dompet Digital (Potongan Rp10.000 jika ≥ Rp100.000)")
    print("0. Keluar")
    return int(input("Pilih metode pembayaran (0-3): "))

def pilih_metode(pilihan):
    if pilihan == 1:
        return Tunai()
    elif pilihan == 2:
        return KartuKredit()
    elif pilihan == 3:
        return DompetDigital()
    else:
        return 

def main():
    while True:
        pilihan = tampilkan_menu()

        if pilihan == 0:
            print("Terima kasih telah menggunakan sistem pembayaran.")
            break

        metode = pilih_metode(pilihan)
        if metode is None:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        try:
            jumlah = float(input("Masukkan total belanja (Rp): "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari nol.")
                continue
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")
            continue

        metode.proses_pembayaran(jumlah)

main()
