class Kucing():
    def __init__(self,nama,warna,suara):
        self.nama = nama
        self.warna = warna
        self.suara = suara

    def display(self):
        return f"=== KUCING ===\nKucing yang memiliki nama {self.nama} ini berwarna {self.warna} yang bersuara {self.suara}.\n"

class Bebek():
    def __init__(self,nama,warna,suara):
        self.nama = nama
        self.warna = warna
        self.suara = suara

    def display(self):
        return f"=== BEBEK ===\nBebek yang memiliki nama {self.nama} ini berwarna {self.warna} yang bersuara {self.suara}.\n"

class Kelinci():
    def __init__(self,nama,warna,suara):
        self.nama = nama
        self.warna = warna
        self.suara = suara

    def display(self):
        return f"=== KELINCI ===\nKelinci yang memiliki nama {self.nama} ini berwarna {self.warna} yang bersuara {self.suara}.\n"

hewan_list = [
    Kucing("Jaer","abu-abu","miaw miaw"),
    Bebek("Cecep","putih","wek wek wek"),
    Kelinci("Beni","coklat","cit cit cit")
]

for hewan in hewan_list:
    print(hewan.display())

