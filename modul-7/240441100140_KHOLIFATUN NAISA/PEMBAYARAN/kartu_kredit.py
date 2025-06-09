from pembayaran import Pembayaran

class Kartu_Kredit(Pembayaran):
    def bayar(self):
        jumlah = int(input("masukkan jumlah pembayaran: "))
        admin = jumlah * 0.02
        total = jumlah + admin
        if jumlah >= 50000:
            print("selamat anda mendapatkan biaya tambahan sebesar 2%")
            print(f"maka total yang harus anda bayar adalah sebesar {total}")
        elif jumlah < 50000:
            print("anda tidak mendapatkan biaya tambahan")
        else:
            print("inputan tidak valid")