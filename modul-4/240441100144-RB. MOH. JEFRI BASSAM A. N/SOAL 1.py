class RekeningBank:
    def __init__(self, no_rekening, nama_pemilik, saldo_awal):
        self._no_rekening = no_rekening
        self._nama_pemilik = nama_pemilik
        self.__saldo = saldo_awal

    @property
    def no_rekening(self):
        return self._no_rekening

    @property
    def nama_pemilik(self):
        return self._nama_pemilik

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo_baru):
        self.__saldo = saldo_baru

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        return False

    def tampilkan_info(self):
        print("No Rekening :", self.no_rekening)
        print("Nama Pemilik:", self.nama_pemilik)
        print("Saldo       : Rp", self.saldo)
        print("-" * 30)

class Bank:
    rekening_list = []

    def tambah_rekening(self, rekening):
        self.rekening_list.append(rekening)

    def cari_rekening(self, no_rekening):
        for rekening in self.rekening_list:
            if rekening.no_rekening == no_rekening:
                return rekening
        return None

    def setor(self, no_rekening, jumlah):
        rekening = self.cari_rekening(no_rekening)
        if rekening:
            rekening.setor(jumlah)
            print("\n --- berhasil disetor tunai --- ")
        else:
            print("\n --- Rekening tidak ditemukan --- ")

    def tarik(self, no_rekening, jumlah):
        rekening = self.cari_rekening(no_rekening)
        if rekening:
            if rekening.tarik(jumlah):
                print("\n --- berhasil ditarik tunai --- ")
            elif not rekening.tarik(jumlah):
                print("\n --- Saldo tidak cukup --- ")
        else:
            print("\n --- Rekening tidak ditemukan --- ")

    def tampilkan_semua_rekening(self):
        if len(self.rekening_list) == 0:
            print("\n --- Belum ada rekening --- ")
        else:
            for rekening in self.rekening_list:
                rekening.tampilkan_info()

    def edit(self):
        print("--- EDIT REKENING BANK ---")
        if len(self.rekening_list) == 0:
            print("\n --- Belum ada rekening --- ")
            return

        no_rek = input("Masukkan no rekening yang ingin diubah datanya: ")
        rekening = self.cari_rekening(no_rek)

        if rekening:
            print("No Rekening :", rekening.no_rekening)
            print("Nama Pemilik:", rekening.nama_pemilik)
            print("Saldo       : Rp", rekening.saldo)

            norek_baru = input("Masukkan no rekening baru    : ")
            nama_baru = input("Masukkan nama pemilik baru   : ")
            saldo_baru = float(input("Masukkan jumlah saldo baru   : "))

            rekening._no_rekening = norek_baru
            rekening._nama_pemilik = nama_baru
            rekening.saldo = saldo_baru

            print("\n --- Data rekening berhasil diubah --- ")
        else:
            print("\n --- No rekening tidak ditemukan --- ")

    def delete(self, no_rekening):
        for i in range(len(self.rekening_list)):
            if self.rekening_list[i].no_rekening == no_rekening:
                del self.rekening_list[i]
                print(f"\n --- Rekening dengan No {no_rekening} berhasil dihapus! --- ")
                return
        print(f"\n --- Rekening dengan No {no_rekening} tidak ditemukan --- ")

        
def main():
    bank = Bank()

    while True:
        print("\n=== MENU BANK MANDIRI ===")
        print("1. Tambah Rekening")
        print("2. Setor")
        print("3. Tarik")
        print("4. Lihat Semua Rekening")
        print("5. edit")
        print("6. delete")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            print("\n --- Tambah Rekening Mandiri --- ")
            no = input("No Rekening     : ")
            nama = input("Nama Pemilik    : ")
            saldo = float(input("Saldo Awal      : "))
            rekening = RekeningBank(no, nama, saldo)
            bank.tambah_rekening(rekening)           
            print("\n --- Rekening berhasil ditambahkan --- ")

        elif pilihan == "2":
            print("\n --- Setor Tunai --- ")
            no = input("Masukkan No Rekening : ")
            jumlah = float(input("Jumlah Setoran       : "))
            bank.setor(no, jumlah)

        elif pilihan == "3":
            print("\n --- Tarik Tunai --- ")            
            no = input("Masukkan No Rekening: ")
            jumlah = float(input("Jumlah Penarikan   : "))
            bank.tarik(no, jumlah)

        elif pilihan == "4":
            print("\n=== DATA SEMUA REKENING NASABAH BANK MANDIRI ===")
            bank.tampilkan_semua_rekening()

        elif pilihan == "5":
            bank.edit()

        elif pilihan == "6":
            print("\n --- Hapus Rekening --- ")
            no = input("masukkan no rekening yang ingin dihapus: ")
            bank.delete(no)

        elif pilihan == "7":
            print("\n  === Terima kasih! === ")
            print(" === Livin By Mandiri === ")
            break

        else:
            print("\n -- Pilihan tidak valid -- ")
main()
