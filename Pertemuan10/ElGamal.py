# ========================
# FUNGSI BANTU
# ========================
def mod_inverse(a, p):
    return pow(a, p - 2, p)

# ========================
# INPUT PARAMETER
# ========================
print("=== INPUT PARAMETER ELGAMAL ===")
p = int(input("Masukkan bilangan prima (p): "))
g = int(input("Masukkan generator (g): "))
x = int(input("Masukkan private key (x): "))
k = int(input("Masukkan bilangan acak (k): "))
plaintext = input("Masukkan plaintext (teks): ")

# ========================
# PEMBENTUKAN KUNCI
# ========================
y = pow(g, x, p)

print("\n=== PEMBENTUKAN KUNCI ===")
print("Public Key (p, g, y):", (p, g, y))
print("Private Key x:", x)

# ========================
# ENKRIPSI
# ========================
ciphertext = []

print("\n=== ENKRIPSI ===")
for ch in plaintext:
    m = ord(ch)           # ubah karakter ke ASCII
    a = pow(g, k, p)
    b = (m * pow(y, k, p)) % p
    ciphertext.append((a, b))
    print(f"'{ch}' -> ({a}, {b})")

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
