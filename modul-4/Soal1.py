class RekeningBank:
    def __init__(self, no_rek, nama_pengguna, saldo=0):
        self.__no_rek = no_rek
        self.__nama_pengguna = nama_pengguna
        self.__saldo = saldo

    @property
    def no_rek(self):
        return self.__no_rek

    @no_rek.setter
    def no_rek(self, value):
        self.__no_rek = value

    @property
    def nama_pengguna(self):
        return self.__nama_pengguna

    @nama_pengguna.setter
    def nama_pengguna(self, value):
        self.__nama_pengguna = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if isinstance(value, int) and value >= 0:
            self.__saldo = value
        else:
            print("Saldo tidak valid")

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor berhasil. Saldo saat ini: {self.__saldo}")
        else:
            print("Jumlah tidak valid")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Tarik berhasil. Saldo saat ini: {self.__saldo}")
        else:
            print("Jumlah tidak valid atau saldo tidak mencukupi.")

    def info(self):
        print(f"No Rek : {self.__no_rek}")
        print(f"Nama   : {self.__nama_pengguna}")
        print(f"Saldo  : {self.__saldo}")
        print("-" * 30)

class Bank:
    def __init__(self):
        self.__rekening = {}

    def tambah_rekening(self, no_rek, nama_pemilik, saldo=0):
        if no_rek not in self.__rekening:
            self.__rekening[no_rek] = RekeningBank(no_rek, nama_pemilik, saldo)
            print(f"Rekening {no_rek} berhasil dibuat")
        else:
            print("No rekening sudah ada")

    def setor_tunai(self, no_rek, jumlah):
        rekening = self.__rekening.get(no_rek)
        if rekening:
            rekening.setor(jumlah)
        else:
            print("Rekening tidak ditemukan")

    def tarik_tunai(self, no_rek, jumlah):
        rekening = self.__rekening.get(no_rek)
        if rekening:
            rekening.tarik(jumlah)
        else:
            print("Rekening tidak ditemukan")

    def tampilkan_rekening(self):
        if not self.__rekening:
            print("Tidak ada rekening terdaftar")
        for rekening in self.__rekening.values():
            rekening.info()

class Main:
    @staticmethod
    def run():
        bank = Bank()
        bank.tambah_rekening("201", "Dina", 100000)
        bank.tambah_rekening("202", "unyil", 250000)    
        bank.setor_tunai("201", 75000)
        bank.tarik_tunai("202", 50000)
        print("\nDaftar Rekening:")
        bank.tampilkan_rekening()

if __name__ == "__main__":
    Main.run()