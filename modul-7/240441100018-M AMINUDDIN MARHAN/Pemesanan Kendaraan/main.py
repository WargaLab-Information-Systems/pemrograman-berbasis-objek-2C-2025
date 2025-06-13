from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def pesan(k):
    for k in kendaraan:
        k.input()
        print(k.booking())
        k.biaya()
        k.asuransi()
        print()

kendaraan = [Mobil(), Motor(), Sepeda()]
pesan(kendaraan)