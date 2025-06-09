from pembayaran import Pembayaran

class Dompet_Digital(Pembayaran):
    def bayar(self):
        jumlah = int(input("masukkan jumlah pembayaran: "))
        diskon = jumlah * 0.10
        total = jumlah - diskon
        if jumlah >= 50000:
            print("selamat anda mendapatkan diskon sebesar 10%")
            print(f"maka total yang harus anda bayar adalah sebesar {total}")
        elif jumlah < 50000:
            print("anda tidak mendapatkan diskon")
        else:
            print("inputan tidak valid")