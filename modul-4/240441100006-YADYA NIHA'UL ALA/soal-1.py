class RekeningBank:
    def __init__(self, nomor_rek, nama_pemilik, saldo):
        self.__nomor_rek = nomor_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    def get_nomor_rek(self):
        return self.__nomor_rek

    def get_nama_pemilik(self):
        return self.__nama_pemilik

    def get_saldo(self):
        return self.__saldo

    def deposit(self, amount):
        if amount > 0:
            self.__saldo += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.__saldo >= amount:
            self.__saldo -= amount
            return True
        else:
            return False

class Bank:
    def __init__(self):
        self.__daftar_rekening = []

    def tambah_rekening(self, rekening):
        for rek in self.__daftar_rekening:
            if rek.get_nomor_rek() == rekening.get_nomor_rek():
                print(f"Nomor rekening '{rekening.get_nomor_rek()}' sudah terdaftar, tidak bisa menambahkan.")
                return False
        self.__daftar_rekening.append(rekening)
        return True

    def setor(self, nomor_rek, amount):
        rekening = self.__cari_rekening(nomor_rek)
        if rekening:
            if rekening.deposit(amount):
                print(f"Setoran sebesar {amount} ke rekening {nomor_rek} berhasil.")
            else:
                print("Jumlah setoran harus positif.")
        else:
            print(f"Rekening dengan nomor {nomor_rek} tidak ditemukan.")

    def tarik(self, nomor_rek, amount):
        rekening = self.__cari_rekening(nomor_rek)
        if rekening:
            if rekening.withdraw(amount):
                print(f"Penarikan sebesar {amount} dari rekening {nomor_rek} berhasil.")
            else:
                # print(f"Saldo tidak cukup untuk penarikkan pada rekening {nomor_rek}.")
                print(f"Penarikkan pada rekening {nomor_rek} gagal. Saldo tidak cukup.")
        else:
            print(f"Rekening dengan nomor {nomor_rek} tidak ditemukan.")

    def __cari_rekening(self, nomor_rek):
        for rek in self.__daftar_rekening:
            if rek.get_nomor_rek() == nomor_rek:
                return rek
        return None

    def tampilkan_semua_rekening(self):
        if len(self.__daftar_rekening) == 0:
            print("Belum ada rekening yang terdaftar.")
            return
        print("Daftar Rekening Nasabah:")
        print("-" * 40)
        for rek in self.__daftar_rekening:
            print(f"Nomor Rekening : {rek.get_nomor_rek()}")
            print(f"Nama Pemilik   : {rek.get_nama_pemilik()}")
            print(f"Saldo          : Rp {rek.get_saldo():,.2f}")
            print("-" * 40)


def main():
    bank = Bank()

    bank.tambah_rekening(RekeningBank("123456789", "Kaedehara Kazuha", 1000000))
    bank.tambah_rekening(RekeningBank("987654321", "Kamisato Ayato", 200000000))
    bank.tambah_rekening(RekeningBank("112233445", "Iudex Neuvilette", 910500000))

    bank.tampilkan_semua_rekening()

    bank.setor("123456789", 500000)
    bank.setor("987654321", 30000000)

    print("+ + + + +")
    bank.tarik("112233445", 4000000) # minus
    bank.tarik("123456789", 2000000)  

    print("=" * 40)

    bank.tampilkan_semua_rekening()

if __name__ == "__main__":
    main()

