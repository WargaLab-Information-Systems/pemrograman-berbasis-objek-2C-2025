class RekeningBank:
    def __init__(self,no_rek,nama,saldo):
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo

    def get_no_rek (self):
        return self.__no_rek
    
    def get_nama (self):
        return self.__nama
    
    def get_saldo (self):
        return self.__saldo
    
    def setor(self,jumlah):
        if jumlah > 0 :
            self.__saldo += jumlah
            print(f"setoran anda berhasil. saldo baru: Rp{self.__saldo}")
        else :
            print("jumlah setor tidak valid.")
    
    def tarik(self,jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"penarikan anda berhasil. saldo baru: Rp{self.__saldo}")
        else:
            print("penarikan anda gagal. saldo anda tidak mencukupi atau input tidak valid.")

    def tampilkan_inpo(self):
        print(f"No Rek:{self.__no_rek},nama:{self.__nama}, Saldo:Rp{self.__saldo}")

class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening (self, no_rek,nama,saldo_awal):
        rekening = RekeningBank(no_rek,nama,saldo_awal)
        self.rekening_list.append(rekening)

    def cari_rekening(self,no_rek):
        for rekening in self.rekening_list:
            if rekening.get_no_rek() == no_rek:
                return rekening
        return None
    
    def setor_uang(self,no_rek,jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening :
            rekening.setor(jumlah)
        else:
            print(f"Rekening tidak ditemukan.")
    def tarik_uang(self,no_rek,jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening :
            rekening.tarik(jumlah)
        else:
            print(f"Rekening tidak ditemukan.")
    def tampilkan_semua_rekening(self):
        print("\n === Data Rekening Nasabah ===")
        if not self.rekening_list:
            print("belum ada rekening.")
        for rekening in self.rekening_list:
            rekening.tampilkan_inpo()

def main():
    bank = Bank()
    bank.tambah_rekening("001","Bita",200000)
    bank.tambah_rekening("002","Lia",40000)
    bank.tambah_rekening("003","Angga",300000)
    
    bank.setor_uang("001", 50000)
    bank.setor_uang("002", 40000)
    bank.setor_uang("001", 100000)

    bank.tampilkan_semua_rekening()

if __name__ == "__main__":
    main()