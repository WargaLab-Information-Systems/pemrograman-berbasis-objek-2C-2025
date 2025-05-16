class RekeningBank:
    def __init__(self, norek, nama, saldo):
        self.nama = nama
        self._norek = norek
        self.__saldo = saldo
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        if saldo >= 0: 
            self.__saldo = saldo
        else:
            print("Saldo tidak valid.")
    def tampilkan_info(self):
        return f"Nomor Rekening: {self._norek}, Nama Pemilik: {self.nama}, Saldo: {self.__saldo}"
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setoran tidak valid.")
    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Jumlah penarikan tidak valid atau saldo tidak cukup.")

class Bank:
    def __init__(self):
        self.list_rekening = []
    def tambah_rekening(self, norek, nama, saldo):
        rekening_baru = RekeningBank(norek, nama, saldo)
        self.list_rekening.append(rekening_baru)
    def cari_rekening(self, norek):
        for rekening in self.list_rekening:
            if rekening._norek == norek:
                return rekening
    def tampilkan_semua_rekening(self):
        if not self.list_rekening:
            print("Tidak ada rekening.")

        for rekening in self.list_rekening:
            print(rekening.tampilkan_info())

def main():
    bank = Bank()
    while True:
        print("\nMenu Bank")
        print("1. Tambah Rekening")
        print("2. Setoran")
        print("3. Tarik Tunai")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")        
        pilihan = int(input("Pilih menu: "))
        if pilihan == 1:
            norek = int(input("Masukkan nomor rekening: "))
            nama = input("Masukkan nama pemilik: ")
            saldo = int(input("Masukkan saldo awal: "))
            bank.tambah_rekening(norek, nama, saldo)
            print("Rekening berhasil ditambahkan.")
        elif pilihan == 2:
            norek = int(input("Masukkan nomor rekening tujuan setoran: "))
            jumlah = int(input("Masukkan jumlah setoran: "))
            rekening = bank.cari_rekening(norek)
            if rekening:
                rekening.setor(jumlah)
                print("Setoran berhasil.")
            else:
                print("Rekening tidak ditemukan.")
        elif pilihan == 3:
            norek = int(input("Masukkan nomor rekening: "))
            jumlah = int(input("Masukkan jumlah penarikan: "))
            rekening = bank.cari_rekening(norek)
            if rekening:
                rekening.tarik(jumlah)
                print("Penarikan berhasil.")
            else:
                print("Rekening tidak ditemukan.")
        elif pilihan == 4:
            bank.tampilkan_semua_rekening()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan layanan bank.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
main()
