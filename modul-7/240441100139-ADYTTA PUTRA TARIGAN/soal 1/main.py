from tunai import PembayaranTunai
from kredit import PembayaranKartuKredit
from digital import PembayaranDompetDigital

def main():
    try:
        jumlah = int(input("Masukkan total belanja (Rp): "))
    except:
        print("Input harus berupa angka. Program dihentikan.")
        return

    print("\nPilih metode pembayaran:")
    print("1. Tunai")
    print("2. Kartu Kredit")
    print("3. Dompet Digital")

    try:
        pilihan = int(input("Pilihan Anda: "))
    except:
        print("Input tidak valid. Harus berupa angka.")
        return

    try:
        if pilihan == 1:
            metode = PembayaranTunai()
        elif pilihan == 2:
            metode = PembayaranKartuKredit()
        elif pilihan == 3:
            metode = PembayaranDompetDigital()
        else:
            print("Pilihan tidak valid.")
            return

        try:
            dibayar = int(input("Masukkan jumlah yang dibayarkan (Rp): "))
        except:
            print("Input jumlah yang dibayarkan tidak valid.")
            return

        if dibayar < jumlah:
            print("Pembayaran gagal: jumlah yang dibayarkan kurang dari total belanja.")
            return

        metode.bayar(jumlah, dibayar)

    except Exception as e:
        print("Terjadi kesalahan saat memproses pembayaran:", e)

if __name__ == "__main__":
    main()
