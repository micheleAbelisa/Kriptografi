# ==========================================
#   Konversi Bilangan Hexadesimal ke:
#   - Desimal
#   - Biner
#   - Oktal
# ==========================================

print("====================================")
print(" Konversi Bilangan Hexadesimal ke Desimal, Biner, dan Oktal")
print("====================================")

while True:
    heksa = input("Masukkan bilangan hexadesimal (atau ketik 'exit' untuk keluar): ")

    if heksa.lower() == "exit":
        print("Program selesai. Terima kasih!")
        break

    # Validasi: hanya karakter 0-9 dan A-F (besar/kecil)
    if not all(ch.upper() in '0123456789ABCDEF' for ch in heksa):
        print("❌ Error: Input bukan bilangan hexadesimal! Gunakan 0–9 atau A–F saja.\n")
        continue

    # Konversi ke desimal
    desimal = int(heksa, 16)

    # Konversi ke biner dan oktal
    biner = bin(desimal)[2:]
    oktal = oct(desimal)[2:]

    # Tampilkan hasil
    print("------------------------------------")
    print(f"Hexadesimal : {heksa.upper()}")
    print(f"Desimal     : {desimal}")
    print(f"Biner       : {biner}")
    print(f"Oktal       : {oktal}")
    print("------------------------------------\n")
