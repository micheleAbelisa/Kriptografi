# Substitusi Cipher
def subtitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

# Transposisi Cipher 4 blok (statis, spasi dihitung)
def transposisi_cipher(plaintext):
    kolom = 4
    parts = [plaintext[i:i + kolom] for i in range(0, len(plaintext), kolom)]

    ciphertext = ""
    for c in range(kolom):
        for part in parts:
            if c < len(part):
                ciphertext += part[c]
    return ciphertext


# Aturan substitusi yang diberikan
aturan_subtitusi = {
    'U':'W',
    'N':'P',
    'I':'K',
    'K':'M',
    'A':'C',
    'S':'U',
    'T':'V',
    'O':'Q',
    'H':'J',
    'M':'O'
}

# Input
plaintext = input("Masukkan plaintext: ")

# Proses tahap 1: Substitusi
cipher_sub = subtitusi_cipher(plaintext, aturan_subtitusi)

# Proses tahap 2: Transposisi 4 blok
cipher_sub_trans = transposisi_cipher(cipher_sub)

# Output
print("\n=== HASIL ENKRIPSI ===")
print("Plaintext asli                 :", plaintext)
print("Ciphertext Substitusi         :", cipher_sub)
print("Substitusi + Transposisi (4 blok):", cipher_sub_trans)
