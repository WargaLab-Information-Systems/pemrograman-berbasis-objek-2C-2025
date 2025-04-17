class hewan:
    def __init__(self, nama, kaki, makan):
        self.nama = nama
        self.kaki = kaki
        self.makan = makan

    def pemakan(self):
        return f"{self.nama} berkaki {self.kaki} termasuk hewan {self.makan}"
    
hewan_list = [
    hewan("sapi", 4, "herbivora"),
    hewan("ayam", 2, "omnivora"),
    hewan("singa", 4, "karnivora"),
]

for hewan in hewan_list:
    print(hewan.pemakan())