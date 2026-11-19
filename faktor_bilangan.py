# ============================================
# PROGRAM FAKTOR BILANGAN
# ============================================

def cari_faktor(n):
    """
    Fungsi untuk mencari semua faktor dari bilangan n.
    Faktor adalah bilangan yang dapat membagi n habis (sisa bagi = 0).
    """
    faktor = []
    for i in range(1, n + 1):
        if n % i == 0:
            faktor.append(i)
    return faktor


# ---- Program Utama ----
print("=" * 50)
print("        PROGRAM FAKTOR BILANGAN")
print("=" * 50)

# Contoh dengan n = 100
n = 100
hasil = cari_faktor(n)
print(f"\nInput  : n = {n}")
print(f"Faktor : {set(hasil)}")
print(f"\nFaktor bilangan {n} adalah:")
print("{" + ", ".join(str(f) for f in hasil) + "}")
print(f"\nJumlah faktor: {len(hasil)} buah")

print("\n" + "-" * 50)

# Input dari pengguna
print("\nCoba masukkan bilangan lain:")
try:
    angka = int(input("Masukkan bilangan bulat positif: "))
    if angka <= 0:
        print("Error: Masukkan bilangan bulat positif!")
    else:
        result = cari_faktor(angka)
        print(f"Faktor bilangan {angka} adalah:")
        print("{" + ", ".join(str(f) for f in result) + "}")
        print(f"Jumlah faktor: {len(result)} buah")
except ValueError:
    print("Error: Masukkan bilangan bulat yang valid!")

print("\n" + "=" * 50)
