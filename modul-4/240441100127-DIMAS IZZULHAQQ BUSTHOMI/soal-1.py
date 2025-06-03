class Bank:
    def __init__(self):
        self.list_rekening = []

    def tambah_rekening(self, rekening):
        self.list_rekening.append(rekening)
        print("-----" * 8)

        print(f"Rekening A.n {rekening.get_nama} berhasil ditambhakan.")
        print("-----" * 8)
        
    def setor(self, no_rek, jumlah):
        for rekening in self.list_rekening:
            if rekening.get_no_rek == no_rek:
                if jumlah > 0 :
                    rekening.set_saldo = rekening.get_saldo + jumlah
                    print("-----" * 8)
                    print(f"Setoran sebesar {jumlah} berhasil pada rekening {rekening.get_nama}.")
                    print("-----" * 8)
                    
                else:
                    print("Setoran Gagal.")

            else:
                print("Nomer Rekening Tidak Ditemukan.")

    def tarik(self, no_rek, jumlah):
        for rekening in self.list_rekening:
            if rekening.get_no_rek == no_rek:
                if rekening.get_saldo >= jumlah:
                    if jumlah > 0:
                        rekening.set_saldo = rekening.get_saldo - jumlah
                        print("-----" * 8)
                        print(f"Penarikan sebesar {jumlah} berhasil pada rekening {rekening.get_nama}.")
                        print("-----" * 8)

                else:
                    print("Penarikan Gagal.")

            else:
                print("Nomer Rekening Tidak Ditemukan.")

    def cari(self, urut):
        no_rek = urut
        for rekening in self.list_rekening:
            if rekening.get_no_rek == no_rek:
                rekening.tampilkan_info()
        
    def tampilkan_semua_rekening(self):
        print("\n=== Daftar Semua Rekening ===")
        for rekening in self.list_rekening:
            rekening.tampilkan_info()

class RekeningBank:
    def __init__(self, no_rek, nama, saldo):
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo

    @property
    def get_no_rek(self):
        return self.__no_rek
    
    @property
    def get_nama(self):
        return self.__nama
    
    @property
    def get_saldo(self):
        return self.__saldo
    
    @get_saldo.setter
    def set_saldo(self, saldo):
        self.__saldo = saldo


    def tampilkan_info(self):
        print(f"No Rekening : {self.get_no_rek}")
        print(f"Nama Pemilik: {self.get_nama}")
        print(f"Saldo       : {self.get_saldo}")
        print("-------------------------------")


class main():
    bank = Bank()
    
    while True:
        print("=== BANK JAWAKARTA ===")
        print("1. Tambah Rekening")
        print("2. Setor Saldo")
        print("3. Tarik Saldo")
        print("4. Tampilkan Semua Rekening")
        print("5. Cari")
        print("6. Keluar")
        print("-----" * 8)

        menu = input("Pilih menu : ")
        if menu == "1":
            no_rek = input("Masukkan NO REK : ")
            for rekening in bank.list_rekening:
                if rekening.get_no_rek == no_rek:
                    print("NO REK TELAH ADA.")
                    break
            else:
                nama = input("Masukkan Nama : ")
                saldo = int(input("Masukkan Saldo Awal : "))
                if saldo < 0:
                    print("Saldo awal tidak boleh negatif.")
                else:
                    nasabah_baru = RekeningBank(no_rek, nama, saldo)
                    bank.tambah_rekening(nasabah_baru)

        elif menu == "2":
            print("=== SETOR SALDO ===")
            no_rek = input("Masukkan NO REK : ")
            saldo = int(input("Masukkan jumlah setor : "))

            bank.setor(no_rek, saldo)

        elif menu == "3":
            print("=== TARIK SALDO ===")
            no_rek = input("Masukkan NO REK : ")
            saldo = int(input("Masukkan jumlah penarikan : "))

            bank.tarik(no_rek, saldo)

        elif menu == "4":
            bank.tampilkan_semua_rekening()
            
        elif menu == "5":
            print("----- Cari Rekening -----")
            urut = input("Masukkan rekening :")
            bank.cari(urut)

        elif menu == "6":
            print("=== TERIMAKASIH ===")
            break

