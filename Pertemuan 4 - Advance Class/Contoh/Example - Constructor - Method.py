# ==============================
# Membuat Kelas dengan Constructor
# ==============================

class Gedung :
    def __init__(self, nama, tinggi) :
        # Atribut Kelas
        self.nama = nama
        self.tinggi = tinggi
    
    def renovasi (self):
        print(f"Merenovasi Gedung {self.nama} .....")

    def mengecat_gedung(self, cat):
        print(f"Mengecat Gedung {self.nama} dengan warna {cat}.....")

# ==============================
# Instanisasi Object dari Class
# ==============================

gedung_a = Gedung("Alfian Husin", "2 Lantai")

# ==============================
# Memanggil Atribut Object gedung_a
# ==============================

print(gedung_a.nama)
print(gedung_a.tinggi)

# ==============================
# Memanggil method renovasi()
# ==============================
gedung_a.renovasi()
gedung_a.mengecat_gedung("Merah")