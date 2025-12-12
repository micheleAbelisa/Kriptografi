#!/usr/bin/env python3
"""
Latihan 2 - RSA (p,q,e acak dalam rentang prima 50-200)
Menampilkan seluruh proses perhitungan (debug) sesuai format PPT.
"""

import random
import math

# -----------------------------
# Utility: primality & prime list
# -----------------------------
def is_prime(n: int) -> bool:
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    r = int(n**0.5)
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

def primes_in_range(low: int, high: int):
    return [x for x in range(low, high+1) if is_prime(x)]

# -----------------------------
# GCD by repeated division (print steps)
# -----------------------------
def gcd_steps(a: int, b: int):
    print("=== Perhitungan GCD (pembagian berulang) ===")
    A, B = a, b
    while B != 0:
        q = A // B
        r = A % B
        print(f"{A} = {q} × {B} + {r}")
        A, B = B, r
    print(f"GCD = {A}\n")
    return A

# -----------------------------
# Extended Euclidean with trace (for back-substitution)
# returns (g, x, y) where a*x + b*y = g
# also prints the table of (r, q) and the back-substitution steps
# -----------------------------
def extended_euclid_trace(a: int, b: int):
    print("=== Extended Euclidean (algoritma Euclid) - forward steps ===")
    r0, r1 = a, b
    quotients = []
    remainders = [r0, r1]
    while r1 != 0:
        q = r0 // r1
        r2 = r0 - q * r1
        quotients.append(q)
        remainders.append(r2)
        print(f"{r0} = {q} × {r1} + {r2}")
        r0, r1 = r1, r2

    g = r0
    print(f"GCD = {g}\n")

    # Back substitution to find x,y
    # Use arrays for s and t (Bezout coefficients)
    print("=== Back-substitution untuk menemukan koefisien x,y ===")
    # initialize
    s = [1, 0]
    t = [0, 1]
    r = remainders[:]  # list of remainders including final 0 maybe
    # Build full lists consistent with quotients length
    # We'll re-run process computing s,t in same order as Euclid:
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    idx = 0
    print(f"mulai: r0={r0}, r1={r1}, s0={s0}, s1={s1}, t0={t0}, t1={t1}")
    while r1 != 0:
        q = r0 // r1
        r2 = r0 - q * r1
        s2 = s0 - q * s1
        t2 = t0 - q * t1
        print(f"q = {q} => r2 = {r0} - {q}*{r1} = {r2}; s2 = {s0} - {q}*{s1} = {s2}; t2 = {t0} - {q}*{t1} = {t2}")
        r0, r1 = r1, r2
        s0, s1 = s1, s2
        t0, t1 = t1, t2
        idx += 1

    # now r0 is gcd, and s0,t0 are Bezout coefficients
    x, y = s0, t0
    print(f"\nHasil: {a}*({x}) + {b}*({y}) = {g}\n")
    return g, x, y

# -----------------------------
# Modular inverse using extended Euclid (with trace)
# -----------------------------
def modinv_with_trace(e: int, phi: int):
    g, x, y = extended_euclid_trace(e, phi)
    if g != 1:
        raise ValueError(f"Tidak ada inverse modular karena gcd({e},{phi}) = {g}")
    # x mungkin negatif; adjust ke range 0..phi-1
    d = x % phi
    print(f"Inverse modular (d) dari e mod phi = {d}  (karena {e}*{x} + {phi}*{y} = 1 -> d ≡ {x} (mod {phi}))\n")
    return d

# -----------------------------
# Diophantine (metode k) mencari d: cari k such that (1 + k*phi) % e == 0
# Print steps mirip PPT
# -----------------------------
def diophantine_find_d(e: int, phi: int, max_k=10000):
    print("=== Mencari d dengan METODE DIOPHANTINE (metode k) ===")
    print(f"Persamaan: {e} * d - {phi} * k = 1  ->  {e}d = 1 + {phi}k")
    k = 1
    while k <= max_k:
        val = 1 + k * phi
        if val % e == 0:
            d = val // e
            print(f"Ditemukan k = {k}")
            print(f"{e}d = {val}  ->  d = {val} / {e} = {d}\n")
            return d, k
        # (optional) print some first attempts to show process (but avoid huge output)
        if k <= 10 or k % 500 == 0:
            print(f"coba k={k} -> 1+{k}*{phi} = {val}  (mod {e} -> rem {val % e})")
        k += 1
    raise ValueError(f"Tidak ditemukan k sampai {max_k}")

# -----------------------------
# Encryption & Decryption (per ASCII character) with debug
# -----------------------------
def encrypt_ascii_per_char(plaintext: str, e: int, n: int):
    print("=== ENKRIPSI (per karakter ASCII) ===")
    table = []
    ciphertext = []
    for ch in plaintext:
        m = ord(ch)
        if m >= n:
            raise ValueError(f"Nilai ASCII {m} dari karakter '{ch}' >= n ({n}). Tidak bisa enkripsi per-char dengan n ini.")
        c = pow(m, e, n)
        table.append((ch, m, c))
        ciphertext.append(c)
        print(f"'{ch}' -> ASCII {m} -> c = {m}^{e} mod {n} = {c}")
    print()
    return ciphertext, table

def decrypt_ascii_per_char(ciphertext, d: int, n: int):
    print("=== DEKRIPSI (per karakter) ===")
    recovered = ""
    for c in ciphertext:
        m = pow(c, d, n)
        recovered += chr(m)
        print(f"{c} -> m = {c}^{d} mod {n} = {m} -> '{chr(m)}'")
    print()
    return recovered

# -----------------------------
# Main routine for latihan 2
# -----------------------------
def rsa_latihan2_interactive():
    print("========================================")
    print("  LATIHAN 2 - RSA (p,q,e acak; prima 50-200)")
    print("========================================\n")

    # 1) pilih p dan q random (prima, distinct)
    primes = primes_in_range(50, 200)
    if len(primes) < 2:
        raise RuntimeError("Tidak ada cukup bilangan prima dalam rentang yang diberikan.")

    p = random.choice(primes)
    q = random.choice(primes)
    # pastikan berbeda
    while q == p:
        q = random.choice(primes)

    print(f"Terpilih secara acak: p = {p}, q = {q}\n")

    # 2) hitung n dan phi
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"n = p × q = {p} × {q} = {n}")
    print(f"φ(n) = (p-1)(q-1) = ({p}-1)×({q}-1) = {phi}\n")

    # 3) pilih e random sehingga 1 < e < phi dan gcd(e,phi)=1
    # tampilkan proses pemilihan hingga ditemukan
    print("=== Memilih e (1 < e < φ(n), GCD(e, φ(n)) = 1) ===")
    attempts = 0
    while True:
        attempts += 1
        e = random.randint(2, phi-1)
        g = math.gcd(e, phi)
        print(f"Coba e = {e} -> GCD({e},{phi}) = {g}")
        if g == 1:
            print(f"Terpilih e = {e} (coprime dengan φ(n))\n")
            break
        if attempts >= 50 and attempts % 50 == 0:
            # avoid infinite loop; but this is very unlikely
            print("Masih mencoba mencari e yang coprime...\n")

    # 4) Tunjukkan langkah GCD e & phi dengan pembagian berulang (seperti di PPT)
    gcd_steps(e, phi)

    # 5) Cari d dengan 2 cara: (A) Diophantine / metode k, (B) Extended Euclid + back-substitution
    # (A)
    d_k, k_found = diophantine_find_d(e, phi, max_k=20000)

    # (B)
    d_ext = modinv_with_trace(e, phi)

    # padankan hasil
    if d_k % phi != d_ext % phi:
        print("PERINGATAN: Hasil metode k dan Extended Euclid berbeda modulo φ(n). Menampilkan keduanya:")
        print(f"d (metode k)  = {d_k}")
        print(f"d (ext euclid)= {d_ext}")
    else:
        # prefer canonical in range 0..phi-1
        d_canonical = d_ext % phi
        print(f"Kedua metode menghasilkan d ≡ {d_canonical} (mod {phi}). Menggunakan d = {d_canonical} sebagai eksponen privat.\n")
        d_k = d_canonical
        d_ext = d_canonical

    # 6) tampilkan kunci
    print(f"Kunci Publik  : (e={e}, n={n})")
    print(f"Kunci Privat  : (d={d_canonical}, n={n})\n")

    # 7) input plaintext dan lakukan enkripsi-dekripsi
    plaintext = input("Masukkan plaintext (disarankan ASCII/basic chars): ")
    print()
    ciphertext, table = encrypt_ascii_per_char(plaintext, e, n)

    print("TABEL ENKRIPSI (ringkasan):")
    print("Char | ASCII | Ciphertext")
    for ch, m, c in table:
        print(f" '{ch}'  |  {m}   |  {c}")
    print()

    recovered = decrypt_ascii_per_char(ciphertext, d_canonical, n)

    print("=== Ringkasan akhir ===")
    print(f"Plaintext asli : {plaintext}")
    print(f"Ciphertext (list angka): {ciphertext}")
    print(f"Plaintext hasil dekripsi : {recovered}")
    print("========================================\n")

    return {
        "p": p, "q": q, "e": e, "d": d_canonical, "n": n,
        "phi": phi, "ciphertext": ciphertext, "recovered": recovered
    }

# -----------------------------
# Run interactive routine if script
# -----------------------------
if __name__ == "__main__":
    rsa_latihan2_interactive()
