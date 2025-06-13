from tunai import Tunai
from kartukredit import KartuKredit
from dompetdigital import DompetDigital

def bayarkan(metode):
    for metode in cara_bayar:
        print(f"Total Akhir: Rp.{metode.bayar()}\n")

cara_bayar = [Tunai(250000), KartuKredit(500000), DompetDigital(400000)]
bayarkan(cara_bayar)