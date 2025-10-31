import itertools

# --- Fungsi Faktorial ---
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

# --- Fungsi Kombinasi (jumlah C(n, r)) ---
def kombinasi(n, r):
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# --- Fungsi Kombinasi dengan daftar objek ---
def kombinasi_objek(objek, r):
    """
    Menghasilkan semua kombinasi r objek dari list objek
    """
    return list(itertools.combinations(objek, r))

# --- Program Utama ---
n = int(input("Masukkan jumlah total objek (n): "))
r = int(input("Masukkan jumlah objek yang dipilih (r): "))

# Buat list inisial huruf A, B, C, ...
objek = [chr(65 + i) for i in range(n)]  # chr(65) = 'A'

# Hitung jumlah kombinasi
jumlah = kombinasi(n, r)
print("\nJumlah kombinasi C({}, {}) adalah: {}".format(n, r, jumlah))

# Tampilkan semua kombinasi
hasil = kombinasi_objek(objek, r)
print("\nDaftar semua kombinasi:")
for h in hasil:
    print(h)
