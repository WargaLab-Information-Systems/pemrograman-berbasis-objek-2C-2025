class RekeningBank:
    def __init__(self, no_rek, nama, saldo):
        if not isinstance(no_rek, str):
            raise ValueError("Nomor rekening harus berupa string")
        if not isinstance(nama, str) or not nama.strip() or nama.isdigit():
            raise ValueError("Nama tidak boleh kosong, harus berupa string, dan tidak boleh mengandung angka")
        if not isinstance(saldo, (int, float)) or saldo <= 0:
            raise ValueError("Saldo harus berupa angka dan harus lebih besar dari 0")
        
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo

    @property
    def no_rek(self):
        return self.__no_rek
    
    @property
    def nama(self):
        return self.__nama
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, jumlah):
        if jumlah >= 0:
            self.__saldo = jumlah
        else:
            print("Saldo harus lebih besar dari 0")
    
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Saldo dari nomor rekening '{self.no_rek}' berhasil ditambahkan.")
        else:
            print("Jumlah setor harus lebih besar dari 0.")

    def tarik(self,jumlah):
        if jumlah < self.__saldo:
            self.__saldo -= jumlah
            print(f"Saldo dari nomor rekening '{self.no_rek}' berhasil ditarik.")
        elif jumlah == self.__saldo:
            print("Jumlah penarikan tidak boleh sama dengan saldo saat ini.")
        else:
            print("Jumlah penarikan tidak boleh lebih besar dari saldo saat ini.")

class bank:
    data_rekening = []

    @classmethod
    def tambah_rekening(cls, rekening):
        for rek in cls.data_rekening:
            if rek.no_rek == rekening.no_rek:
                print(f"Nomor rekening '{rekening.no_rek}' sudah terdaftar.")
                return
        cls.data_rekening.append(rekening)
        print(f"Rekening atas nama '{rekening.nama}' berhasil ditambahkan.")

    @classmethod
    def cari_rekening(cls, no_rek):
        for rek in cls.data_rekening:
            if rek.no_rek == no_rek:
                return rek
        return None
    
    def setor(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            rek.setor(jumlah)
        else:
            print(f"Nomor rekening '{no_rek}' tidak ditemukan.")

    def tarik(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            rek.tarik(jumlah)
        else:
            print(f"Nomor rekening '{no_rek}' tidak ditemukan.")

    @classmethod
    def display(cls):
        print("\n=====DATA SELURUH NASABAH BANK=====")
        for rek in cls.data_rekening:
            print(f"Nomor rekening      : {rek.no_rek}")
            print(f"Nama pemilik        : {rek.nama}")
            print(f"Total saldo saat ini: Rp.{rek.saldo}")
            print()

def main():
    b = bank()
    try:
        rekening1 = RekeningBank("0001", "Amin", 3000000)
        rekening2 = RekeningBank("0002", "Bucky", 15000000)
        rekening3 = RekeningBank("0003", "Yelena", 4800000)
        rekening4 = RekeningBank("0003", "Bob", 2500000)

        bank.tambah_rekening(rekening1)
        bank.tambah_rekening(rekening2)
        bank.tambah_rekening(rekening3)
        bank.tambah_rekening(rekening4)

        bank.display()

        b.setor("0001", 1000000)
        b.tarik("0003", 500000)
        rekening2.saldo = -1

        bank.display()
    except ValueError as a:
        print(f"Error: {a}")

if __name__ == "__main__":
    main()