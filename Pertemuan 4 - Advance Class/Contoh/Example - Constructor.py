# ==============================
# Membuat Kelas dengan Constructor
# ==============================

class Gedung :
    def __init__(self, nama, tinggi) :
        # Atribut Kelas
        self.nama = nama
        self.tinggi = tinggi

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
# Mengubah Atribut Object gedung_a
# ==============================
gedung_a.nama = "Yoenidar Karim"
print(gedung_a.nama)