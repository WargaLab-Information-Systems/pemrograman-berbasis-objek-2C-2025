class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo_awal):
        self.__no_rek = no_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo_awal

    @property
    def no_rek(self):
        return self.__no_rek

    @property
    def nama_pemilik(self):
        return self.__nama_pemilik

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Penarikan gagal: jumlah saldo tidak mencukupi.")


class Bank:
    def __init__(self):
        self.__daftar_rekening = []

    def tambah_rekening(self, rekening):
        self.__daftar_rekening.append(rekening)

    def cari_rekening(self, no_rek):
        for rek in self.__daftar_rekening:
            if rek.no_rek == no_rek:
                return rek
        return None

    def tampilkan_semua_rekening(self):
        if not self.__daftar_rekening:
            print("Tidak ada rekening yang terdaftar.")
        else:
            print("Daftar Rekening Nasabah:\n")
            for rek in self.__daftar_rekening:
                print(f"No. Rekening  : {rek.no_rek}")
                print(f"Nama Pemilik  : {rek.nama_pemilik}")
                print(f"Saldo         : Rp{rek.saldo}")
                print()

class main():
    bank = Bank()

    rek1 = RekeningBank("1234567890", "Septi", 500000)
    rek2 = RekeningBank("0987654321", "Isti", 1000000)

    bank.tambah_rekening(rek1)
    bank.tambah_rekening(rek2)

    rek = bank.cari_rekening("0987654321")
    if rek:
        rek.setor(250000)
        rek.tarik(100000)
    else:
        print("Nomor rekening tidak terdaftar!")


    print("=====================================")

    bank.tampilkan_semua_rekening()


