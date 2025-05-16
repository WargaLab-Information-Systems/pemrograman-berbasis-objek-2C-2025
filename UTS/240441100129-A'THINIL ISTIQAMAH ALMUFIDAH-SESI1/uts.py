class Iuran :
    total_warga =0
    def __init__(self, Nama, Metode_pembayaran):
        self.Nama =Nama
        self.Metode_Pembayaran = Metode_pembayaran

    def displayinfo(self):
        print(f"Nama : {self.Nama}, Metode Pembayaran : {self.Metode_Pembayaran}")
        
    @classmethod
    def get_total_warga(cls):
        print(f"total warga yang membayar : {cls.total_warga}")

    @staticmethod
    def validasi_metode (bank):
        return f"{bank}"
    
class IuranTunai(Iuran):
    def __init__(self, Nama, Metode_pembayaran, jumlah):
        super().__init__(Nama, Metode_pembayaran)
        self.jumlah = jumlah

    def displayinfo(self):
        return f"{super().displayinfo()}, Membayar Sebesar Rp. {self.jumlah}"
    
class IuranTransfer (Iuran):
    def __init__(self, Nama, Metode_pembayaran, jumlah, bank):
        super().__init__(Nama, Metode_pembayaran)
        self.jumlah=jumlah
        self.bank=bank

    def displayinfo(self):
        print (f"Transfer : {self.Nama}")
        print(f"Membayar sebesar :{self.jumlah}")
        print(f"Via : {self.bank}")


def main():
    daftar_iuran = 0
    daftar_iuran.append(Iuran)
    for i in range():
        if IuranTransfer :
            print(f"Bank :")
        else :
            print(f"tunai")
tunai1= Iuran 







        


        


        

    