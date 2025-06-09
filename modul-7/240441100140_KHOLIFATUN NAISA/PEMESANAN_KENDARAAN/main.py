from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

while True:
    print("\nSELAMAT DATANG DI RENTAL KENDARAAN")
    print("1. Mobil")
    print("2. Motor")
    print("3. Sepeda")
    print("4. Keluar")
    jawab = int(input("masukkan nomor jenis kendaraan yang ingin anda rental: "))
    if jawab == 1:
        rental = Mobil()
    elif jawab == 2:
        rental = Motor()
    elif jawab == 3:
        rental = Sepeda()
    elif jawab == 4:
        print("Terimakasih sudah berkunjung")
        break
    else:
        print("inputan tidak valid")

    rental.booking()
    rental.biaya()
    rental.asuransi()
