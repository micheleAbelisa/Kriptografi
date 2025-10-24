# ==========================================
#   Konversi Bilangan Oktal ke:
#   - Desimal
#   - Biner
#   - Hexadesimal
# ==========================================

print("====================================")
print(" Konversi Bilangan Oktal ke Desimal, Biner, dan Hexadesimal")
print("====================================")

while True:
    oktal = input("Masukkan bilangan oktal (atau ketik 'exit' untuk keluar): ")

    if oktal.lower() == "exit":
        print("Program selesai. Terima kasih!")
        break

    # Validasi: hanya boleh angka 0–7
    if not all(ch in '01234567' for ch in oktal):
        print("❌ Error: Input bukan bilangan oktal! Gunakan angka 0–7 saja.\n")
        continue

    # Konversi ke desimal
    desimal = int(oktal, 8)

    # Konversi ke biner dan hexadesimal
    biner = bin(desimal)[2:]
    heksa = hex(desimal)[2:].upper()

    # Tampilkan hasil
    print("------------------------------------")
    print(f"Oktal       : {oktal}")
    print(f"Desimal     : {desimal}")
    print(f"Biner       : {biner}")
    print(f"Hexadesimal : {heksa}")
    print("------------------------------------\n")
