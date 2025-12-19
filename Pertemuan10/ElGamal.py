# ========================
# FUNGSI BANTU
# ========================
def mod_inverse(a, p):
    # Invers modulo menggunakan Teorema Fermat
    return pow(a, p - 2, p)

# ========================
# INPUT PARAMETER
# ========================
print("=== INPUT PARAMETER ELGAMAL ===")
p = int(input("Masukkan bilangan prima (p > 127): "))
g = int(input("Masukkan generator (g): "))
x = int(input("Masukkan private key (x): "))
k = int(input("Masukkan bilangan acak (k): "))
plaintext = input("Masukkan plaintext (teks): ")

# ========================
# VALIDASI p
# ========================
for ch in plaintext:
    if ord(ch) >= p:
        raise ValueError("Nilai p terlalu kecil untuk ASCII plaintext!")

# ========================
# PEMBENTUKAN KUNCI PUBLIK
# ========================
print("\n=== PEMBENTUKAN KUNCI PUBLIK ===")
print("Rumus: y = g^x mod p")
print(f"y = {g}^{x} mod {p}")

y = pow(g, x, p)

print(f"y = {y}")
print("\nPublic Key (p, g, y):", (p, g, y))
print("Private Key x:", x)

# ========================
# ENKRIPSI
# ========================
ciphertext = []

print("\n=== ENKRIPSI ===")
for ch in plaintext:
    m = ord(ch)
    a = pow(g, k, p)
    b = (m * pow(y, k, p)) % p
    ciphertext.append((a, b))
    print(f"'{ch}' (ASCII {m}) -> a = {a}, b = {b}")

# ========================
# DEKRIPSI
# ========================
hasil = ""

print("\n=== DEKRIPSI ===")
for a, b in ciphertext:
    s = pow(a, x, p)
    s_inv = mod_inverse(s, p)
    m = (b * s_inv) % p
    hasil += chr(m)

print("Plaintext hasil dekripsi:", hasil)
