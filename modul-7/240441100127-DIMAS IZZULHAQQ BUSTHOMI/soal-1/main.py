from tunai import Tunai
from kartuKredit import KartuKredit
from dompetDigital import DompetDigital

def main():
    while True:
        print("1. Tunai")
        print("2. Dompet Digital")
        print("3. Kartu Kredit")
        print("4. Selesai")
        pilihan = int(input("Pilih menu: "))
        jumlah = int(input("Masukkan Jumlah: "))

        if pilihan == 1:
            metode = Tunai()
        elif pilihan == 2:
            metode = DompetDigital()
        elif pilihan == 3:
            metode = KartuKredit()
        elif pilihan == 4:
            break
        else:
            print("Pilih yang ada di menu!")

        total = metode.prosesPembayaran(jumlah)
        print(f"Total yang dibayar setelah terhitung : {total}")

main()