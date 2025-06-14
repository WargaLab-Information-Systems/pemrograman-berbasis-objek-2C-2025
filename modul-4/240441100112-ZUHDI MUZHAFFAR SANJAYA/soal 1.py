class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo):
        self.__no_rek = no_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    def get_no_rek(self):
        return self.__no_rek

    def get_nama(self):
        return self.__nama_pemilik

    def get_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor berhasil. Saldo baru: {self.__saldo}")
        else:
            print("Jumlah setor harus lebih dari 0.")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Penarikan berhasil. Saldo baru: {self.__saldo}")
        else:
            print("Penarikan gagal. Saldo tidak cukup atau jumlah tidak valid.")


class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, rekening):
        self.rekening_list.append(rekening)

    def cari_rekening(self, no_rek):
        for rek in self.rekening_list:
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
        print("\nDaftar Rekening Nasabah:")
        for rek in self.rekening_list:
            print(f"No Rek: {rek.get_no_rek()}, Nama: {rek.get_nama()}, Saldo: Rp{rek.get_saldo()}")


def main():
    
    bank_utama = Bank()
    
    bank_utama.tambah_rekening(RekeningBank("001", "Agung", 500000))
    bank_utama.tambah_rekening(RekeningBank("002", "Pandu", 300000))
    bank_utama.tambah_rekening(RekeningBank("003", "Salsa", 700000))

    bank_utama.setor_uang("001", 250000)
    bank_utama.tarik_uang("002", 100000)
    bank_utama.setor_uang("003", 50000)
    
    bank_utama.tampilkan_semua_rekening()

if __name__ == "__main__":
    main()