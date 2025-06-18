from abc import ABC, abstractmethod

class Booking(ABC):
    def __init__(self, nama, usia):
        self._nama = nama
        self._usia = usia

    @abstractmethod
    def proses_pemesanan(self):
        pass

    @abstractmethod
    def hitung_biaya(self):
        pass

    @abstractmethod
    def hitung_asuransi(self):
        pass

    def cek_usia(self, usia_minimal):
        if self._usia < usia_minimal:
            raise ValueError(f"Usia minimal untuk booking adalah {usia_minimal} tahun.")