class RekeningBank:
    def __init__(self, no_rek, n_pemilik, saldo=0):
        self.__no_rek = no_rek
        self.__n_pemilik = n_pemilik
        self.__saldo = saldo

    def setor(self, jumlah):
        if jumlah > 0: 
            self.__saldo += jumlah
            return True
        return False

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        return False
    @property
    def info(self):
        return {
            "No Rekening": self.__no_rek,
            "Nama Pemilik": self.__n_pemilik,
            "Saldo": self.__saldo
        }
    @property
    def no_rek(self):
        return self.__no_rek

class Bank:
    def __init__(self):
        self.daftar_rekening = []

    def tambah_rekening(self, rekening):
        self.daftar_rekening.append(rekening)

    def setor_uang(self, no_rek, jumlah):
        for rekening in self.daftar_rekening:
            if rekening.no_rek == no_rek:
                return rekening.setor(jumlah)
        return False

    def tarik_uang(self, no_rek, jumlah):
        for rekening in self.daftar_rekening:
            if rekening.no_rek == no_rek:
                return rekening.tarik(jumlah)
        return False

    def tampilkan_semua_rekening(self):
        for rekening in self.daftar_rekening:
            info = rekening.info
            print(f"No Rekening: {info['No Rekening']}, Nama: {info['Nama Pemilik']}, Saldo: Rp{info['Saldo']}")


class main():
    bank = Bank()

    while True:
        norek = input("Masukkan No rek: ")
        n_pemilik = input("Masukkan Nama Pemilik: ")
        saldo = input("Masukkan Saldo: ")

        rekening_baru = RekeningBank(norek, n_pemilik, saldo)
        bank.tambah_rekening(rekening_baru)

        n = input("Tambah Rekening (y/n) : ")
        if n == "n":
            break

    print("Daftar Rekening di Bank:")
    bank.tampilkan_semua_rekening()
main()