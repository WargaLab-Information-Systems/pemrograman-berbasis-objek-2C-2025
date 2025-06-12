from abc import ABC

class Buku(ABC):
    def __init__(self, judul: str):
        self.judul = judul
