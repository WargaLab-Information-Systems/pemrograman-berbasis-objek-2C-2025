class RekeningBank:
    def __init__(self,noRek,nama,saldo):
        self.noRek = noRek
        self._nama = nama
        self.__saldo = saldo

    @property
    def nama(self):
        return self._nama

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        self.__saldo += jumlah

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo anda tidak mencukupi!!")

    def display(self):
        print(f"No Rekening     : {self.noRek}") 
        print(f"Nama            : {self._nama}")
        print(f"Saldo           : Rp{self.__saldo:,}") 
        print()


class Bank:
    list_rekening = []

    @classmethod
    def tambah_rek(cls, rekening):
        cls.list_rekening.append(rekening)
        print(f"Rekening dengan nama {rekening.nama} berhasil di tambahkan")

    @classmethod
    def transaksi_setor(cls, noRek, jumlah):
        for i in cls.list_rekening:
            if i.noRek == noRek:
                i.setor(jumlah)
                return f"Transaksi setor sebesar {jumlah} pada No Rekening {noRek} anda berhasil."
        return "No Rekening anda tidak ditemukan!!"

    @classmethod
    def transaksi_tarik(cls, noRek, jumlah):
        for i in cls.list_rekening:
            if i.noRek == noRek:
                i.tarik(jumlah)
                return f"Transaksi tarik sebesar {jumlah} pada No Rekening {noRek} anda berhasil."
        return "No Rekening anda tidak ditemukan!!"

    @classmethod
    def tampilkan_semua_data(cls):
        print()
        print("=" * 35)
        print(f"{" " * 7}Data Rekening Nasabah")
        print("=" * 35)
        print()
        nomor = 1
        for i in cls.list_rekening:
            print(f"Nasabah ke-{nomor}")
            i.display()
            nomor += 1


class Main:
    def run():
        nsbh1 = RekeningBank("111005", "Oktavia Putri", 10000000)
        nsbh2 = RekeningBank("200313", "Adiyat Iftiar", 15000000)
        nsbh3 = RekeningBank("270805", "Denis", 8450000)
        nsbh4 = RekeningBank("211005", "Sopo", 3210000)
        nsbh5 = RekeningBank("120905", "Jarwo", 7433000)

        Bank.tambah_rek(nsbh1)
        Bank.tambah_rek(nsbh2)
        Bank.tambah_rek(nsbh3)
        Bank.tambah_rek(nsbh4)
        Bank.tambah_rek(nsbh5)

        print()
        print(Bank.transaksi_setor("111005", 3450000))
        print(Bank.transaksi_tarik("200313", 452000))
        print(Bank.transaksi_setor("270805", 523000))
        print(Bank.transaksi_tarik("2110005", 5000000)) 

        Bank.tampilkan_semua_data()


Main.run()
