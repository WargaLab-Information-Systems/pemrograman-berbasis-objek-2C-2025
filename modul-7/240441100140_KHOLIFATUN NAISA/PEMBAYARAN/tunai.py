from pembayaran import Pembayaran

class Tunai(Pembayaran):
    def bayar(self):
        jumlah = int(input("masukkan jumlah pembayaran: "))
        potongan = jumlah * 0.05
        total = jumlah - potongan
        if jumlah >= 50000:
            print("selamat anda mendapatkan potongan sebesar 5%")
            print(f"maka total yang harus anda bayar adalah sebesar {total}")
        elif jumlah < 50000:
            print("anda tidak mendapatkan potongan")
        else:
            print("inputan tidak valid")