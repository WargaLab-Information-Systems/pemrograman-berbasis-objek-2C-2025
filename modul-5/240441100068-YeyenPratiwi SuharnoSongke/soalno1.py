from abc import ABC, abstractmethod
class Manusia(ABC):
    @abstractmethod
    def berbicara(self):
        pass

    @abstractmethod
    def asal(self):
        pass

    @abstractmethod
    def hobi(self):
        pass

class Joko(Manusia):
    def berbicara(self):
        print("Joko: Saya berbicara soal sejarah.")
    
    def asal(self):
        print("Joko: Saya berasal dari Pekalongan.")
    
    def hobi(self):
        print("Joko: hobi saya Memancing")

class Beni(Manusia):
    def berbicara(self):
        print("Beni: Saya berbicara tentang teknologi.")
    
    def asal(self):
        print("Beni: Saya berasal dari pamekasan.")
    
    def hobi(self):
        print("Beni: hobi saya Membaca.")

class Fani(Manusia):
    def berbicara(self):
        print("Fani: Saya berbicara di depan umum.")
    
    def asal(self):
        print("Fani: Saya berasal dari Bali.")
    
    def hobi(self):
        print("Fani: Saya suka memasak.")

class Jani(Manusia):
    def berbicara(self):
        print("Jani: Saya lebih suka menulis dari pada bicara.")
    
    def asal(self):
        print("Jani: Saya berasal dari jakarta.")
    
    def hobi(self):
        print("Jani: Saya suka menulis novel.")

print("=== Joko ===")
joko = Joko()
joko.berbicara()
joko.asal()
joko.hobi()

print("\n=== Beni ===")
beni = Beni()
beni.berbicara()
beni.asal()
beni.hobi()

print("\n=== Fani ===")
fani = Fani()
fani.berbicara()
fani.asal()
fani.hobi()

print("\n=== Jani ===")
jani = Jani()
jani.berbicara()
jani.asal()
jani.hobi()
