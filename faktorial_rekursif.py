# ============================================
# PROGRAM FAKTORIAL MENGGUNAKAN FUNGSI REKURSIF
# ============================================

def faktorial(n):
    """
    Fungsi rekursif untuk menghitung faktorial dari n.
    Faktorial(n) = n * faktorial(n-1)
    Base case: faktorial(0) = 1 dan faktorial(1) = 1
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)


# ---- Program Utama ----
print("=" * 45)
print("   PROGRAM FAKTORIAL (FUNGSI REKURSIF)")
print("=" * 45)

# Contoh dengan n = 5
n = 5
hasil = faktorial(n)
print(f"\nInput  : n = {n}")
print(f"Proses : {n}! = ", end="")

# Tampilkan langkah perkalian
langkah = " × ".join(str(i) for i in range(n, 0, -1))
print(f"{langkah} = {hasil}")
print(f"\nHasil Faktorial {n}! = {hasil}")

print("\n" + "-" * 45)

# Input dari pengguna
print("\nCoba masukkan bilangan lain:")
try:
    angka = int(input("Masukkan bilangan bulat non-negatif: "))
    if angka < 0:
        print("Error: Faktorial tidak terdefinisi untuk bilangan negatif!")
    else:
        print(f"Faktorial {angka}! = {faktorial(angka)}")
except ValueError:
    print("Error: Masukkan bilangan bulat yang valid!")

print("\n" + "=" * 45)
