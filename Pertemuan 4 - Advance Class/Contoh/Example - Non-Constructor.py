# ==============================
# Membuat Kelas
# ==============================

class Gedung :
    nama = "Alfian Husin"
    tinggi = "2 Lantai"

# ==============================
# Memanggil Kelas Menjadi Objek
# ==============================
    
gedung_a = Gedung()

# ==============================
# Memanggil Atribut  Objek gedung_a
# ==============================
    
print(gedung_a.nama)
print(gedung_a.tinggi)

# ==============================
# Mengubah Atribut Kelas
# ==============================

Gedung.nama = "Yoenidar Karim"

# Instanisasi kembali
gedung_a = Gedung()

# Memanggil Atribut objek gedung_a
print(gedung_a.nama)