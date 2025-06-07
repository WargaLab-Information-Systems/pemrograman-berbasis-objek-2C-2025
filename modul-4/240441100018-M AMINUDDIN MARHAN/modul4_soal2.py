class Buku:
    def __init__(self, judul, penulis, halaman):
        if not isinstance(judul, str) or not judul.strip():
            raise ValueError("Judul buku harus berupa string dan tidak boleh kosong")
        if not isinstance(penulis, str) or not penulis.strip() or penulis.isdigit():
            raise ValueError("Penulis buku harus berupa string, tidak boleh kosong dan tidak boleh berupa angka")
        if not isinstance(halaman, int) or halaman <= 0:
            raise ValueError("Halaman buku harus berupa integer dan lebih besar dari 0")
        
        self.__judul = judul
        self.__penulis = penulis
        self.__halaman = halaman

    @property
    def judul(self):
        return self.__judul
    
    @property
    def penulis(self):
        return self.__penulis
    
    @property
    def halaman(self):
        return self.__halaman
    
class Perpustakaan:
    daftar_buku = []

    @classmethod
    def tambah_buku(cls, buku):
        for book in cls.daftar_buku:
            if book.judul == buku.judul:
                print(f"Buku dengan judul '{buku.judul}' sudah ada di perpustakaan")
                return book
        cls.daftar_buku.append(buku)
        print(f"Buku dengan judul '{buku.judul}' berhasil ditambahkan")

    @classmethod
    def display(cls):
        print("\n=====DATA BUKU DI PERPUSTAKAAN=====")
        for buku in cls.daftar_buku:
            print(f"Judul buku    : {buku.judul}")
            print(f"Penulis       : {buku.penulis}")
            print(f"Jumlah halaman: {buku.halaman}")
            print()

def main():
    try:
        buku1 = Buku("Harry Potter", "J.K. Rowling", 500)
        buku2 = Buku("Madilog", "Tan Malaka", 568)
        buku3 = Buku("Lord of the Rings", "J.R.R. Tolkien", 1000)
        buku4 = Buku("Lord of the Rings", "J.R.R. Tolkien", 1000)

        Perpustakaan.tambah_buku(buku1)
        Perpustakaan.tambah_buku(buku2)
        Perpustakaan.tambah_buku(buku3)
        Perpustakaan.tambah_buku(buku4)

        Perpustakaan.display()
    except ValueError as a:
        print(f"Error: {a}")

if __name__ == "__main__":
    main()