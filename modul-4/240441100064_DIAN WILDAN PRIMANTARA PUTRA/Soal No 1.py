class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo):
        self.__no_rek = no_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    @property
    def no_rek(self):
        return self.__no_rek

    @property 
    def nama_pemilik(self):
        return self.__nama_pemilik

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value


class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, no_rek, nama, saldo_awal):
        rekening = RekeningBank(no_rek, nama, saldo_awal)
        self.rekening_list.append(rekening)

    def setor(self, no_rek, jumlah):
        for rekening in self.rekening_list:
            if rekening.no_rek == no_rek:
                rekening.saldo += jumlah

    def tarik(self, no_rek, jumlah):
        for rekening in self.rekening_list:
            if rekening.no_rek == no_rek and rekening.saldo >= jumlah:
                rekening.saldo -= jumlah

    def tampilkan_semua_rekening(self):
        print("=== Daftar Rekening ===")
        for r in self.rekening_list:
            print(f"Rek: {r.no_rek}, Nama: {r.nama_pemilik}, Saldo: {r.saldo}")

bank = Bank()
bank.tambah_rekening("001", "Dian", 100000)
bank.tambah_rekening("002", "Ferdi", 150000)
bank.setor("001", 50000)
bank.tarik("002", 30000)
bank.tampilkan_semua_rekening()