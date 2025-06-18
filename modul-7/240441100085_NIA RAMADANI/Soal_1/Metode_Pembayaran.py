from abc import ABC, abstractmethod

class MetodePembayaran(ABC):
    def __init__(self, jumlah, saldo_awal):
        self.__jumlah = jumlah
        self.__saldo_awal = saldo_awal

    @property
    def jumlah(self):
        return self.__jumlah

    @property
    def saldo_awal(self):
        return self.__saldo_awal

    @abstractmethod
    def hitung_total(self):
        pass

    @abstractmethod
    def bayar(self):
        pass
