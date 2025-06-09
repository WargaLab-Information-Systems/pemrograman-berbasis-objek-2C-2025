class RekeningBank:
    def __init__(self, no_rek, nama, saldo):
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo

    def get_no_rek(self):
        return self.__no_rek

    def get_nama(self):
        return self.__nama

    def get_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setoran sebesar {jumlah} berhasil untuk {self.__nama}")
        else:
            print("Jumlah setoran harus lebih dari 0")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Penarikan sebesar {jumlah} berhasil untuk {self.__nama}")
        else:
            print("Penarikan gagal. Saldo tidak mencukupi atau jumlah tidak valid")


class Bank:
    def __init__(self):
        self.daftar_rekening = []

    def tambah_rekening(self, rekening):
        self.daftar_rekening.append(rekening)
        print(f"Rekening atas nama {rekening.get_nama()} berhasil ditambahkan.")

    def cari_rekening(self, no_rek):
        for rek in self.daftar_rekening:
            if rek.get_no_rek() == no_rek:
                return rek
        return None

    def setor_uang(self, no_rek, jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            rekening.setor(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    def tarik_uang(self, no_rek, jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            rekening.tarik(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    def tampilkan_semua_rekening(self):
        print("\nDaftar Rekening di Bank:")
        for rek in self.daftar_rekening:
            print(f"No Rekening : {rek.get_no_rek()} | Nama: {rek.get_nama()} | Saldo: {rek.get_saldo()}")


if __name__ == "__main__":
    bank = Bank()

    rekening1 = RekeningBank("001", "Andi", 100000)
    rekening2 = RekeningBank("002", "Budi", 50000)

    bank.tambah_rekening(rekening1)
    bank.tambah_rekening(rekening2)

    bank.setor_uang("001", 50000)
    bank.tarik_uang("002", 30000)
    bank.setor_uang("003", 10000)  

    bank.tampilkan_semua_rekening()