# ==========================================================
# LATIHAN 1 - RSA FIXED VALUES (p = 17, q = 11, e = 7)
# Format perhitungan mengikuti materi di PPT
# ==========================================================

def gcd_pembagian(a, b):
    print("=== PERHITUNGAN GCD(e, φ(n)) ===")
    while b != 0:
        q = a // b
        r = a % b
        print(f"{a} = {q} × {b} + {r}")
        a, b = b, r
    print(f"GCD = {a}\n")
    return a

def cari_d_dengan_k(e, phi):
    print("=== PERHITUNGAN d (Metode Persamaan Linear / Metode K) ===")
    k = 1
    while True:
        nilai = 1 + k * phi
        if nilai % e == 0:
            d = nilai // e
            print(f"Persamaan: {e}.d - {phi}.k = 1")
            print(f"→ {e}d = 1 + {phi}(k)")
            print(f"→ {e}d = {nilai}  (k = {k})")
            print(f"→ d = {nilai} / {e} = {d}")
            print(f"Nilai d ditemukan = {d}\n")
            return d
        k += 1


def rsa_latihan1(plaintext):
    print("======================================")
    print("     LATIHAN 1: RSA (p=17, q=11, e=7)")
    print("======================================\n")

    # 1. Nilai awal sesuai PPT
    p = 17
    q = 11
    e = 7

    print(f"p = {p}")
    print(f"q = {q}")
    print(f"e = {e}\n")

    # 2. Hitung n
    n = p * q
    print("=== PERHITUNGAN n ===")
    print(f"n = p × q = {p} × {q} = {n}\n")

    # 3. Hitung phi(n)
    phi = (p - 1) * (q - 1)
    print("=== PERHITUNGAN φ(n) ===")
    print(f"φ(n) = (p - 1)(q - 1) = 16 × 10 = {phi}\n")

    # 4. Uji GCD e dan phi
    gcd_pembagian(e, phi)

    # 5. Cari d metode PPT (metode k)
    d = cari_d_dengan_k(e, phi)

    print("=== HASIL KUNCI ===")
    print(f"Kunci Publik  : (e={e}, n={n})")
    print(f"Kunci Privat  : (d={d}, n={n})\n")

    # 6. Enkripsi per karakter ASCII
    print("=== PROSES ENKRIPSI (Per Karakter ASCII) ===")
    encrypted = []
    for ch in plaintext:
        m = ord(ch)
        c = pow(m, e, n)
        encrypted.append(c)
        print(f"'{ch}'  → ASCII {m} → {m}^{e} mod {n} = {c}")

    # 7. Dekripsi
    print("\n=== PROSES DEKRIPSI ===")
    decrypted = ""
    for c in encrypted:
        m = pow(c, d, n)
        decrypted += chr(m)
        print(f"{c} → {c}^{d} mod {n} = {m} → '{chr(m)}'")

    print("\n=== HASIL DEKRIPSI AKHIR ===")
    print("Plaintext hasil dekripsi =", decrypted)
    print("======================================")

    return encrypted, decrypted


# =============================
# JALANKAN DI BAWAH INI
# =============================

plaintext = input("Masukkan plaintext: ")
rsa_latihan1(plaintext)
