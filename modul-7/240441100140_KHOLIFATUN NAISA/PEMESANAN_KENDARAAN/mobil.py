from kendaraan import Kendaraan

class Mobil(Kendaraan):
    def __init__(self):
        self.hari = 0
        self.usia = 0

    def booking(self):
        self.usia = int(input("Masukkan usia anda: "))
        if self.usia >= 20:
            self.hari = int(input("Masukkan berapa hari anda akan booking mobil ini: "))
            print(f"Anda akan booking mobil selama {self.hari} hari")
        elif self.usia < 20:
            print("Mohon maaf anda belum cukup umur")
        else:
            print("Inputan invalid")

    def biaya(self):
        if self.hari > 0:
            jumlah = self.hari * 50000  
            print( f"Total biaya yang harus anda bayar adalah sebesar Rp{jumlah}")
        else:
            print( "Silakan lakukan booking terlebih dahulu.")

    def asuransi(self):
        if self.hari > 0:
            biaya_asuransi = 20000  
            print(f"Asuransi tambahan sebesar Rp{biaya_asuransi} telah ditambahkan.")
            total = (self.hari * 50000) + biaya_asuransi
            print( f"Total biaya dengan asuransi: Rp{total}")
        else:
            print( "Asuransi tidak bisa dihitung karena belum booking.")
        


