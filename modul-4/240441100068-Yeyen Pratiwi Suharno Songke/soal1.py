class RekeningBank:
    def __init__(self, no_rek, nama, saldo_awal=0):
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo_awal

    @property
    def no_rek(self):
        return self.__no_rek

    @property
    def nama(self):
        return self.__nama

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor Rp{jumlah} ke rekening {self.__no_rek} berhasil.")
        else:
            print("Jumlah setor tidak valid!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Tarik Rp{jumlah} dari rekening {self.__no_rek} berhasil.")
        else:
            print("Jumlah penarikan tidak valid atau saldo tidak mencukupi!")


class Bank:
    def __init__(self):
        self.rekening_list = []  

    def tambah_rekening(self, no_rek, nama, saldo_awal=0):
        rekening_baru = RekeningBank(no_rek, nama, saldo_awal)
        self.rekening_list.append(rekening_baru)
        print(f"Rekening atas nama {nama} berhasil ditambahkan.")

    def setor_uang(self, no_rek, jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            rekening.setor(jumlah)
        else:
            print("Rekening tidak ditemukan!")

    def tarik_uang(self, no_rek, jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            rekening.tarik(jumlah)
        else:
            print("Rekening tidak ditemukan!")

    def cari_rekening(self, no_rek):
        for rek in self.rekening_list:
            if rek.no_rek == no_rek:
                return rek
        return None

    def tampilkan_semua_rekening(self):
        if not self.rekening_list:
            print("Tidak ada data rekening.")
        else:
            print("\n=== Daftar Rekening Nasabah ===")
            for rek in self.rekening_list:
                print(f"No Rek: {rek.no_rek} | Nama: {rek.nama} | Saldo: Rp{rek.saldo}")


def main():
    bank = Bank()

    bank.tambah_rekening("001", "Samas", 9100000)
    bank.tambah_rekening("002", "bidiono", 5090000)
    bank.setor_uang("001", 25000)
    bank.tarik_uang("002", 20000)
    
    bank.tampilkan_semua_rekening()


if __name__ == "__main__":
    main()
