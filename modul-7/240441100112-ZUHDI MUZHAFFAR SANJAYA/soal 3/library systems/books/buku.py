class Buku:
    def __init__(self, judul, penulis):
        self._judul = judul
        self._penulis = penulis
        self._status = "tersedia"
        self._dipesan = False

    @property
    def judul(self):
        return self._judul

    @property
    def penulis(self):
        return self._penulis