
class Hewan:
    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara

    def bersuara(self):
        return f"{self.nama} bersuara: {self.suara}"

    def info(self):
        return f"Nama: {self.nama}, Jenis: {self.jenis}"


class Kucing(Hewan):
    def __init__(self, nama, warna):
        Hewan.__init__(nama, "Kucing", "Miauw")
        self.warna = warna

    def info(self):
        return f"{super().info()}, Warna: {self.warna}"


class Anjing(Hewan):
    def __init__(self, nama, ras):
        Hewan.__init__(nama, "Anjing", "Guguk")
        self.ras = ras

    def info(self):
        return f"{super().info()}, Ras: {self.ras}"


class Burung(Hewan):
    def __init__(self, nama, jenis_burung):
        Hewan.__init__(nama, "Burung", "Berkicau")
        self.jenis_burung = jenis_burung

    def info(self):
        return f"{super().info()}, Jenis Burung: {self.jenis_burung}"

hewan_list = []

for i in range(2):
    kucing = Kucing(f"Kucing {i+1}", "Coklat cream")
    anjing = Anjing(f"Anjing {i+1}", "Bulldog")
    burung = Burung(f"Burung {i+1}", "Cendrawasih")
    
    hewan_list.append(kucing)
    hewan_list.append(anjing)
    hewan_list.append(burung)

for hewan in hewan_list:
    print(hewan.info())
    print(hewan.bersuara())
